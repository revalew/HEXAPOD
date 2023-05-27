#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from hexapod_controller.com_settings import *
from hexapod_controller_interfaces.msg import ServoPositionValues
from hexapod_controller_interfaces.msg import Leg
from hexapod_controller_interfaces.msg import ControllStatus

from hexapod_controller.inverse_kinematics_params import *
import hexapod_controller.inverse_kinematics as ik

class MotorController(Node):
    def __init__(self, id):
        
        # Data Byte Length
        self.LEN_MX_GOAL_POSITION = 4
        
        name = f"pose_subscriber_{id}"
        super().__init__(name)
        
        # LEG ID
        self.id_id = id
        self.id_index = id - 1
        
        if self.id_index == 3: self.id_index = 5
        elif self.id_index == 5: self.id_index = 3
        
        # IDs of the specific leg servos
        self.id_id_1 = id * 3 - 2
        self.id_id_2 = self.id_id_1 + 1
        self.id_id_3 = self.id_id_1 + 2
        
        # positions of the servos
        self.coxa = self.id_id_1 - 1
        self.femur = self.id_id_1
        self.tibia = self.id_id_1 + 1
        
        if (self.id_id == 4):
            # self.id_index == 5
            self.coxa = 15
            self.femur = 16
            self.tibia = 17
            
        elif (self.id_id == 6):
            # self.id_index == 3
            self.coxa = 9
            self.femur = 10
            self.tibia = 11
        
        # create the leg subscriber
        # self.pose_subsciber = self.create_subscription(
        #     ServoPositionValues, "bodyIK_topic", self.pose_callback_id,20)
        
        topic_name = "leg_" + str(self.id_id)
        
        self.leg_pub_ = self.create_publisher(Leg, topic_name, 10)

        # self.leg_sub = self.create_subscription(Leg, topic_name, self.pose_callback_id, 20)
        self.controll_status_sub_ = self.create_subscription(ControllStatus, "control_status", self.gait_iteration, 10)
        
    def pose_callback_id(self, msg: Leg):
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
        time.sleep(0.025 * (self.id_id - 1) + 0.000001)
        
        
    def gait_iteration(self, msg: ControllStatus):
        if msg.status_name == "walk_tripod":
            GITE_SIZE = 2
            
            x = msg.variable_1 # variable to determin to walk forward or backward
            
            for gait_index in range(GITE_SIZE):
                time.sleep(0.2)
                self.leg_trajectory(forward=x, up_or_down=tripod_gait[self.id_index][gait_index])

                
        
    def leg_trajectory(self, forward, up_or_down):
        '''
         Function dedicated to move specyfic leg in meaning of walking forward / backward
         id = id of leg
         x = forward -> 1, backward -> -1
         up_or_down = if 1 it means that leg should be in air
         rot_angle = trajectory line rotation in space, for future development, hexa rotation
         leg_direction = leg direction in coxa axis swap, preventing wrong movement
        '''
        
        # empty msg type initialization, with default values
        cmd = Leg()
        
        # variables
        trajectory_variant      = 0  
        WAIT_TIME               = 0.005
        LEG_SLEEP_TIME          = [0,0.075,0.1,0.125,0.150,0.025,0.05]
        
        # step logic
        if up_or_down:
            # leg in the air - elipse move
            trajectory_variant     = 0
            points      = [p for p in range(20,-21,-10)]
        else:
            # leg on the ground - line move
            trajectory_variant     = 1
            points      = [p for p in range(-20,21,10)]
            
        # leg inverse kinematics calculations and msg publications
        # do this for every point in trajectory
        
        for x in points:

            leg_value = ik.leg_ik(x*LEG_DIRECTION_SWAP[self.id_index]*forward, self.id_index, trajectory_variant)
            cmd.coxa = leg_value[0] # coxa leg value
            cmd.femur = leg_value[1] # femur leg value
            cmd.tibia = leg_value[2] # tibia leg value
            
            # publishing values of leg axises for every iteration, for every point
            """
             leg swap, we need to tidy those swaps!
            """
            # time.sleep(WAIT_TIME)
            # self.leg_pub_.publish(cmd)
            
            
            
            # CODE BELOW JUST FOR TESTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # CODE BELOW JUST FOR TESTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # CODE BELOW JUST FOR TESTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            
            groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_MX_GOAL_POSITION, self.LEN_MX_GOAL_POSITION)
            
            # Allocate goal position value into byte array
            param_goal_position1 = [DXL_LOBYTE(DXL_LOWORD(leg_value[0])), DXL_HIBYTE(DXL_LOWORD(leg_value[0])), DXL_LOBYTE(DXL_HIWORD(leg_value[0])), DXL_HIBYTE(DXL_HIWORD(leg_value[0]))]
        
            # Allocate goal position value into byte array
            param_goal_position2 = [DXL_LOBYTE(DXL_LOWORD(leg_value[1])), DXL_HIBYTE(DXL_LOWORD(leg_value[1])), DXL_LOBYTE(DXL_HIWORD(leg_value[1])), DXL_HIBYTE(DXL_HIWORD(leg_value[1]))]
        
            # Allocate goal position value into byte array
            param_goal_position3 = [DXL_LOBYTE(DXL_LOWORD(leg_value[2])), DXL_HIBYTE(DXL_LOWORD(leg_value[2])), DXL_LOBYTE(DXL_HIWORD(leg_value[2])), DXL_HIBYTE(DXL_HIWORD(leg_value[2]))]
            
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
            time.sleep(0.02 * (self.id_index) + 0.000001)
            # time.sleep(LEG_SLEEP_TIME[self.id_index])
            
        
        
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
