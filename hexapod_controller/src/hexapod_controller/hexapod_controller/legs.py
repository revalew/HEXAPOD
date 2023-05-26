#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from hexapod_controller.com_settings import *
from hexapod_controller_interfaces.msg import ServoPositionValues
from hexapod_controller_interfaces.msg import Leg

class MotorController(Node):
    def __init__(self, id):
        
        # Data Byte Length
        self.LEN_MX_GOAL_POSITION = 4
        
        name = f"pose_subscriber_{id}"
        super().__init__(name)
        
        # LEG ID
        self.id_id = id
        
        # IDs of the specific leg servos
        self.id_id_1 = id * 3 - 2
        self.id_id_2 = self.id_id_1 + 1
        self.id_id_3 = self.id_id_1 + 2
        
        # positions of the servos
        self.coxa = self.id_id_1 - 1
        self.femur = self.id_id_1
        self.tibia = self.id_id_1 + 1
        
        if (self.id_id == 4):
            self.coxa = 15
            self.femur = 16
            self.tibia = 17
            
        elif (self.id_id == 6):
            self.coxa = 9
            self.femur = 10
            self.tibia = 11
        
        # create the leg subscriber
        # self.pose_subsciber = self.create_subscription(
        #     ServoPositionValues, "bodyIK_topic", self.pose_callback_id,20)

        topic_name = "leg_" + str(self.id_id)
        self.leg_sub = self.create_subscription(Leg, topic_name, self.pose_callback_id, 10)  # FLAGA BLEDU
        
    def pose_callback_id(self, msg: Leg):
        # Sleep added to solve the problem of USB to TTL converter's overload
        # time.sleep(0.0125 * self.id_id)
        time.sleep(0.025 * (self.id_id - 1) + 0.000001)

        
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
