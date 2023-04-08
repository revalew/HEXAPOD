#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# create a node class which inherits from the rcl class
class MyNode(Node):

    # creating the constructor
    def __init__(self):
        # set the name of the node
        super().__init__("first_node")
        
        # do something => writing the log
        self.get_logger().info("Hello from ROS2 on RPi")


def main(args=None):
    # initialize ROS2 communication
    rclpy.init(args=args)

    # create the node based on the class we created
    node = MyNode()

    # keep the node alive until we send a SIGINT
    rclpy.spin(node)

    # shut down the ROS2 communication and destroy the node
    rclpy.shutdown()

if __name__ == '__main__':
    main()