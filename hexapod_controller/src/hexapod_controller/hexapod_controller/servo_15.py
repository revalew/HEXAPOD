#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from hexapod_controller.com_settings import *
from hexapod_controller_interfaces.msg import ServoPositionValues

class MotorController(Node):
    def __init__(self, id):
        name = f"pose_subscriber_{id}"
        super().__init__(name)
        
        self.id_id = id
        self.id_index = self.id_id - 1
        
        # -- LEGWAN -- 
        self.pose_subsciber = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id,10)
        
    # servo 15
    def pose_callback_id(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController id={self.id_id}: received msg = {msg.id_pose[self.id_index]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, self.id_id, ADDR_MX_GOAL_POSITION, msg.id_pose[self.id_index])

def main(args=None):
    rclpy.init(args=args)
    nodeSubscriber = MotorController(15)
    rclpy.spin(nodeSubscriber)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
