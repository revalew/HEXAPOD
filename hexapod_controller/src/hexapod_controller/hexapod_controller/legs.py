#!/usr/bin/env python3

'''
    File info:
    Class MotorController implementation. Class provide separate calculations for each leg, that solution solves converter's overload and speeds up inverse kinematics calculations.
'''


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
from hexapod_controller_interfaces.msg import BodyIKCalculate


class MotorController(Node):
    def __init__(self, id):
        
        # Data Byte Length
        self.LEN_MX_GOAL_POSITION   = 4
        self.goal_pos               = [0,0,0,0,0,0]
        self.move_direction         = 0
        
        
        self.points                 = [20, 10, 0, -10, -20, -20, -10, 0, 10, 20]
        self.index                  = 0
        self.trajectory_variant     = 0
        self.gait_index             = 0 
        
        
        
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
            
        self.up_or_down = tripod_gait[self.id_index][self.gait_index]
        
        if self.up_or_down:
            self.trajectory_variant  = 0
            self.index               = 0
        else:
            self.trajectory_variant  = 1
            self.index               = 5
        
        # create the leg specific topic and its publisher
        topic_name = "leg_" + str(self.id_id)
        # topic_name = f"leg_{self.id_id}" # this may be less resource-intensive
        self.leg_pub_ = self.create_publisher(Leg, topic_name, 10)

        # create the leg subscribers
        self.leg_sub = self.create_subscription(Leg, topic_name, self.pose_callback_id, 20)
        self.controll_status_sub_ = self.create_subscription(ControllStatus, "control_status", self.gait_iteration, 20)
        self.keyboard_callback_sub_ = self.create_subscription(BodyIKCalculate, "body_IK_calculations", self.keyboard_callback, 20)
       
       
    def keyboard_callback(self, msg: BodyIKCalculate):
        '''
        Function responsible for receiving data from topic "body_IK_calculations", 
        pub. file: teleop_keyboard_test.py
        '''
        self.goal_pos[0] = msg.position_of_the_body[0]
        self.goal_pos[1] = msg.position_of_the_body[1]
        self.goal_pos[2] = msg.position_of_the_body[2]
        self.goal_pos[3] = msg.position_of_the_body[3]
        self.goal_pos[4] = msg.position_of_the_body[4]
        self.goal_pos[5] = msg.position_of_the_body[5]
        self.move_direction = msg.move_direction
        
        
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
        time.sleep(0.025)
        
        
    def gait_iteration(self, msg: ControllStatus):
        '''
        Function to iterate through the indices of the gait pattern matrix to calculate the trajectory of each leg

        # TODO descritption
        '''

        # TRIPOD GAIT PATTERN
        if msg.status_name == "walk_tripod":
            # for gait_index in range(GAIT_SIZE):
            self.leg_trajectory(direction=self.move_direction)
            
            # self.leg_trajectory(direction=self.move_direction, up_or_down=tripod_gait[self.id_index][self.gait_index])
                
        if msg.status_name == "rotate_left_tripod":
            # for gait_index in range(GAIT_SIZE):
                
            if (self.id_index == 0 or self.id_index == 1 or self.id_index == 2 ):
                self.move_direction = -1
                
            self.leg_trajectory(direction=self.move_direction)
                
        if msg.status_name == "rotate_right_tripod":
            # for gait_index in range(GAIT_SIZE):
                
            if (self.id_index == 3 or self.id_index == 4 or self.id_index == 5 ):
                self.move_direction = -1
                
            self.leg_trajectory(direction=self.move_direction)
                
        if msg.status_name == "body_manipulation":
            self.body_manipulation()
                
        
    def leg_trajectory(self, direction):
        '''
        Function responsible for moving a specific leg to walk forward / backward

        id : id of the leg
        x : 1 => move forward, -1 => move backward
        up_or_down : 1 => leg should be up, 0 => leg should be down

        # TODO descritption     
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
        WAIT_TIME               = 0.05
        
        # step logic
        # if up_or_down:
        #     # leg in the air - ellipse movement
        #     trajectory_variant  = 0
        #     # points              = [p for p in range(20,-21,-10)]
        #     points              = [20, 10, 0, -10, -20]
        # else:
        #     # leg on the ground - line movement
        #     trajectory_variant  = 1
        #     # points              = [p for p in range(-20,21,10)]
        #     points              = [-20, -10, 0, 10, 20]
        
        
            
            

        # leg inverse kinematics calculation and msg publication for every point in trajectory
        # if (self.index > 4 and not up_or_down):
        if (self.index > 4):
            self.trajectory_variant  = 1

        
        # if (self.index >= 9 and up_or_down): 
        if (self.index >= 9): 
            self.index = 0
            self.trajectory_variant = 0
        
            # if (self.gait_index == 0): self.gait_index = 1
            # else: self.gait_index = 0
            
        x = self.points[self.index]

        # calculate the angles of the servos
        leg_value = ik.body_move(self.goal_pos[0],
                            self.goal_pos[1],
                            self.goal_pos[2],
                            self.goal_pos[3],
                            self.goal_pos[4],
                            self.goal_pos[5],
                            x*LEG_DIRECTION_SWAP[self.id_index]*direction,
                            self.id_index,
                            self.trajectory_variant)
        
        cmd.coxa = leg_value[0] # coxa leg value
        cmd.femur = leg_value[1] # femur leg value
        cmd.tibia = leg_value[2] # tibia leg value
        
        # publishing values of leg axes for current point each iteration 
        # time.sleep(WAIT_TIME)
        self.leg_pub_.publish(cmd)
        
        self.index += 1
        

    
    def body_manipulation(self):
        '''
            Change the position of the body based on the keyboard input
        '''
        
        # msg initialization with default values
        cmd = Leg()
        
        leg_value = ik.body_ik(self.id_index,
                                self.goal_pos[0],
                                self.goal_pos[1],
                                self.goal_pos[2],
                                self.goal_pos[3],
                                self.goal_pos[4],
                                self.goal_pos[5])
        
        cmd.coxa = leg_value[0] # coxa leg value
        cmd.femur = leg_value[1] # femur leg value
        cmd.tibia = leg_value[2] # tibia leg value
        
        # publishing values of leg axes for current point each iteration 
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
