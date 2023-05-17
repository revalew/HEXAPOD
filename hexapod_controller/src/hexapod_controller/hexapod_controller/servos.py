#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from hexapod_controller.com_settings import *
from hexapod_controller_interfaces.msg import ServoPositionValues


class MotorController(Node):
    def __init__(self, id, pos_index):
        name = f"pose_subscriber_{id}"
        super().__init__(name)
        
        self.id_id = id
        self.id_index = pos_index - 1
        
        # -- LEGWAN -- 
        self.pose_subsciber = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id,10)
        
    # servo
    def pose_callback_id(self, msg: ServoPositionValues):
        # print(f"Subscriber MotorController id={self.id_id}: received msg = {msg.id_pose[self.id_index]}")
        # time.sleep(0.1)
        time.sleep(0.025*self.id_id)
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, self.id_id, ADDR_MX_GOAL_POSITION, msg.id_pose[self.id_index])
        self.get_logger().info("woit")


def servo1(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(1,1)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo2(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(2,2)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo3(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(3,3)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo4(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(4,4)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo5(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(5,5)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo6(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(6,6)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo7(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(7,7)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo8(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(8,8)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo9(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(9,9)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo10(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(10,16)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo11(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(11,17)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo12(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(12,18)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo13(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(13,13)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo14(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(14,14)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo15(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(15,15)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo16(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(16,10)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo17(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(17,11)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    
def servo18(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(18,12)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()
    

if __name__ == "__main__":
    main()
