#!/usr/bin/env python3

"""
THIS IS A SIMPLE EXAMPLE NODE TO LEARN ABOUT THE ENV
"""

import rclpy
from rclpy.node import Node


# create a node class which inherits from the rcl class
class MyNode(Node):
    # creating the constructor
    def __init__(self):
        # set the name of the node
        super().__init__("first_node")

        # create a counter
        self.counter_ = 1

        # do something => writing the log
        # self.get_logger().info("Hello from ROS2 on RPi")

        # create the timer, where
        # 1.0 => time in seconfds (float)
        # timer_callback => callback function
        self.create_timer(1.0, self.timer_callback)

    # create a timer callback inside the node
    def timer_callback(self):
        self.get_logger().info("Hello from timer " + str(self.counter_))
        self.counter_ += 1


def main(args=None):
    # initialize ROS2 communication
    rclpy.init(args=args)

    # create the node based on the class we created
    node = MyNode()

    # keep the node alive until we send a SIGINT and the most important: it enables the actual callbacks for the node
    rclpy.spin(node)

    # shut down the ROS2 communication and destroy the node
    rclpy.shutdown()


if __name__ == "__main__":
    main()
