#!/usr/bin/env python3
# My first Node!
import rclpy
from rclpy.node import Node


# importing our new message type
from hexapod_controller_interfaces.msg import BodyIKCalculate


class JoystickNode(Node):
    def __init__(self):
        super().__init__("body_IK")
       
        self.get_logger().info("HEXAPOD body Inverse Kinematics calculation has been started.")

        # create publisher
        self.joy_data_ = self.create_publisher(BodyIKCalculate, "joy_data_topic", 10)
        self.timer_ = self.create_timer(0.05, self.send_joystick) # FLAGA BLEDU -> zbyt szybki timer?
        
    def send_joystick(self):
        # create the msg with the specific type
        msg = BodyIKCalculate()
        
        
        # publish the message to topic joy_data_topic
        self.joy_data_.publish(msg)
        

def main(args=None):
    
    # NODE PART
    rclpy.init(args=args)
    nodePublish = JoystickNode()
    rclpy.spin(nodePublish)
    rclpy.shutdown()
    

if __name__ == "__main__":
    main()
