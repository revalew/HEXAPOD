#!/usr/bin/env python3

# ROS imports
import rclpy
from rclpy.node import Node

# communication settings
from hexapod_controller.com_settings import *

# Inverse Kinematics calculations
from hexapod_controller.inverse_kinematics_params import *
import hexapod_controller.inverse_kinematics as ik

# import custom message types
from hexapod_controller_interfaces.msg import ServoPositionValues
from hexapod_controller_interfaces.msg import Leg
from hexapod_controller_interfaces.msg import ControllStatus

class MotorController(Node):
    def __init__(self, id):
        
        # Data Byte Length
        self.LEN_MX_GOAL_POSITION = 4
        
        # Name of the node
        name = f"pose_subscriber_{id}"
        super().__init__(name)
        
        # LEG ID
        self.id_id = id
        self.id_index = id - 1
        
        # IDs of the specific leg servos
        self.id_id_1 = id * 3 - 2
        self.id_id_2 = self.id_id_1 + 1
        self.id_id_3 = self.id_id_1 + 2
        
        # index of the servos in the value array
        self.coxa = self.id_id_1 - 1
        self.femur = self.id_id_1
        self.tibia = self.id_id_1 + 1
        
        # Swap the 4th and 6th leg to maintain the numbering continuity and ensure the correct movement
        if (self.id_id == 4):
            self.coxa = 15
            self.femur = 16
            self.tibia = 17
            self.id_index = 5

        elif (self.id_id == 6):
            self.coxa = 9
            self.femur = 10
            self.tibia = 11
            self.id_index = 3
        
        # create the leg subscriber
        # self.pose_subsciber = self.create_subscription(
        #     ServoPositionValues, "bodyIK_topic", self.pose_callback_id,20)
        
        # create the leg specific topic and its publisher
        topic_name = "leg_" + str(self.id_id)
        # topic_name = f"leg_{self.id_id}" # this may be less resource-intensive
        self.leg_pub_ = self.create_publisher(Leg, topic_name, 10)

        self.leg_sub = self.create_subscription(Leg, topic_name, self.pose_callback_id, 20)
        self.controll_status_sub_ = self.create_subscription(ControllStatus, "control_status", self.gait_iteration, 10)
        
    def pose_callback_id(self, msg: Leg):
        '''
        Function responsible for sending the data packets to the servos
        We are sending data to 3 at a time as a bundle
        '''

        # Initialize Groupsyncwrite instance
        groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_MX_GOAL_POSITION, self.LEN_MX_GOAL_POSITION)
        
        # Allocate goal position value into byte array
        param_goal_position1 = [DXL_LOBYTE(DXL_LOWORD(msg.coxa)), DXL_HIBYTE(DXL_LOWORD(msg.coxa)), DXL_LOBYTE(DXL_HIWORD(msg.coxa)), DXL_HIBYTE(DXL_HIWORD(msg.coxa))]
    
        # Allocate goal position value into byte array
        param_goal_position2 = [DXL_LOBYTE(DXL_LOWORD(msg.femur)), DXL_HIBYTE(DXL_LOWORD(msg.femur)), DXL_LOBYTE(DXL_HIWORD(msg.femur)), DXL_HIBYTE(DXL_HIWORD(msg.femur))]
    
        # Allocate goal position value into byte array
        param_goal_position3 = [DXL_LOBYTE(DXL_LOWORD(msg.tibia)), DXL_HIBYTE(DXL_LOWORD(msg.tibia)), DXL_LOBYTE(DXL_HIWORD(msg.tibia)), DXL_HIBYTE(DXL_HIWORD(msg.tibia))]
        
        # Add Dynamixel#1 goal position value to the Syncwrite parameter storage
        dxl_addparam_result = groupSyncWrite.addParam(self.id_id_1, param_goal_position1)
        
        # Add Dynamixel#2 goal position value to the Syncwrite parameter storage
        dxl_addparam_result = groupSyncWrite.addParam(self.id_id_2, param_goal_position2)
        
        # Add Dynamixel#3 goal position value to the Syncwrite parameter storage
        dxl_addparam_result = groupSyncWrite.addParam(self.id_id_3, param_goal_position3)
        
        # Syncwrite goal position
        dxl_comm_result = groupSyncWrite.txPacket()

        # Clear syncwrite parameter storage
        groupSyncWrite.clearParam()
        
        # Sleep added to solve the problem of USB to TTL converter's overload
        # time.sleep(0.125 * (self.id_index) + 0.000001)
        time.sleep(0.025)
        
        
    def gait_iteration(self, msg: ControllStatus):
        '''
        Function to iterate through the indices of the gait pattern matrix to calculate the trajectory of each leg

        <TODO>
                DESCRIPTION!
        </TODO>
        '''

        # TRIPOD GAIT PATTERN
        if msg.status_name == "walk_tripod":
            GAIT_SIZE = 2
            x = msg.variable_1 # variable to determine the walking direction
            
            for gait_index in range(GAIT_SIZE):
                self.leg_trajectory(direction=x, up_or_down=tripod_gait[self.id_index][gait_index])
                
        
    def leg_trajectory(self, direction, up_or_down):
        '''
        Function responsible for moving a specific leg to walk forward / backward

        id : id of the leg
        x : 1 => move forward, -1 => move backward
        up_or_down : 1 => leg should be up, 0 => leg should be down

        <TODO>
            NEEDS EXPLAINING!!!:
            rot_angle : trajectory line rotation in space, for future development, hexa rotation
            leg_direction = leg direction in coxa axis swap, preventing wrong movement

            LOOSE INTERPRETATION WITH NO CONTEXT:
            rot_angle : rotate the line representing trajectory in space (for future development)
            leg_direction : switch the direction of the coxa motor axis to prevent wrong movements
        </TODO>
        '''
        
        # msg initialization with default values
        cmd = Leg()
        
        # variables
        trajectory_variant      = 0  
        WAIT_TIME               = 0.005
        
        # step logic
        if up_or_down:
            # leg in the air - ellipse movement
            trajectory_variant  = 0
            points              = [p for p in range(20,-21,-10)]
        else:
            # leg on the ground - line movement
            trajectory_variant  = 1
            points              = [p for p in range(-20,21,10)]
            
        # leg inverse kinematics calculation and msg publication for every point in trajectory
        for x in points:

            # calculate the angles of the servos
            leg_value = ik.leg_ik(x*LEG_DIRECTION_SWAP[self.id_index]*direction, self.id_index, trajectory_variant)
            cmd.coxa = leg_value[0] # coxa leg value
            cmd.femur = leg_value[1] # femur leg value
            cmd.tibia = leg_value[2] # tibia leg value
            
            """
            <TODO>
                TIDY THE SWAPS!!! THEY CAN BE FOUND in "inverse_kinematics_params.py" IN LINE 5
            </TODO>
            """
            
            # publishing values of leg axes for current point each iteration 
            time.sleep(WAIT_TIME)
            self.leg_pub_.publish(cmd)
            
        
# NODE FUNCTIONS called from setup.py / hexapod.launch.py
def leg1(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(1)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def leg2(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(2)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def leg3(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(3)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def leg4(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(4)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def leg5(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(5)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def leg6(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(6)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
