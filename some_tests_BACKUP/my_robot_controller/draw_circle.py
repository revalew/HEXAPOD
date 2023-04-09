#!/usr/bin/env python3

'''
THIS IS MY FIRST PUBLISHER NODE
'''

import rclpy
from rclpy.node import Node

# message type defining package
from geometry_msgs.msg import Twist


class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle")

        # THIS IS A PUBLISHER NODE IN PYTHON CREATED BY ATTRIBUTE:
        # Twist => msg data type
        # /turtle1/cmd_vel => name of the topic
        #  10 => queue size --> the buffer size of 10 messages
        self.cmv_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        # create a timer to execute the callback func (spin(node) in main required to work)
        self.timer_ = self.create_timer(0.5, self.send_velocity_command)

        self.get_logger().info("Draw circle node has been started.")

    def send_velocity_command(self):
        # send the data to the topic with the publisher we just created:

        # create the msg with the specific type
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0

        # publish the created message:
        self.cmv_vel_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()

# we also have to install the node to the package in setup.py
# AND add the msg dependency to the "package.xml" file: <depend>geometry_msgs</depend> <depend>turtlesim</depend>
# after that we have to build it (because it is a new file) with colcon build --symlink-install