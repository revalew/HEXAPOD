#!/usr/bin/env python3

"""
THIS IS MY FIRST SUBSCRIBER NODE
"""

import rclpy
from rclpy.node import Node

# impoort the msg type
from turtlesim.msg import Pose


class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__("pose_subscriber")

        # create an attribute to set subscriber:
        # Pose => msg type --> what kind of msg do we expect to receive
        # /turtle1/pose => topic we want to listen to
        # pose_callback => callback function to process the received msg
        # 10 => queue size
        self.pose_subscriber_ = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10
        )

    def pose_callback(self, msg: Pose):
        # we can do a "msg: Pose" to specify the type of the msg - like "long long d" ;)

        self.get_logger().info(
            "position of the turtle: (" + str(msg.x) + ", " + str(msg.y) + ")"
        )


def main(args=None):
    rclpy.init(args=args)

    node = PoseSubscriberNode()
    rclpy.spin(node)

    rclpy.shutdown()


# here we have to add the turtlesim pkg to .xml file
# AND install the node to enable "ros2 run ... " execution style
