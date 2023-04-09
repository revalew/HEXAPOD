#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# subscriber msg type
from turtlesim.msg import Pose

# publisher msg type
from geometry_msgs.msg import Twist

# service client data type --> turtlesim/srv/SetPen
from turtlesim.srv import SetPen

# import partial
from functools import partial


class turtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.get_logger().info("Turtle controller has been started.")

        # keep track of the turtle position
        self.previous_x_ = 0

        # create publisher
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        # create the subscriber which will publish the information when he receives the msg
        self.pose_subscriber_ = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10
        )

    # subscriber callback
    def pose_callback(self, pose: Pose):
        cmd = Twist()

        if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            cmd.linear.x = 1.0
            cmd.angular.z = 0.9
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        self.cmd_vel_publisher_.publish(cmd)

        # use the service call to change the pen color based on the position of the turtle
        # left side => GREEN
        # right side => RED
        # this callback is called 60 times per second which is too much for our usage
        # we do not want to call the service 60 times / s !
        # we can modify this to run only when the turtle crosses the middle line to do that we add the "self.previous_x_ = 0" in the __init__ and modify it on crossing
        if pose.x > 5.5 and self.previous_x_ <= 5.5:
            self.previous_x_ = pose.x
            self.get_logger().info("Changing the color to RED.")
            self.call_set_pen_service(255, 0, 0, 3, 0)
        elif pose.x <= 5.5 and self.previous_x_ > 5.5:
            self.previous_x_ = pose.x
            self.get_logger().info("Changing the color to GREEN.")
            self.call_set_pen_service(0, 255, 0, 3, 0)

    # new service client which will change the color of the turtlesim pen
    def call_set_pen_service(self, r, g, b, width, off):
        # /turtle1/set_pen service takes 5 parameters

        # create a client of the server
        # SetPen => service type
        # /turtle1/set_pen => service name
        client = self.create_client(SetPen, "/turtle1/set_pen")

        # wait for the service because we do not want to call it when it is not up
        # 1.0 => timeout of 1s
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for the service...")

        # create a request
        request = SetPen.Request()
        # fill it with the values passed through the argunts
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        # call the service in asynchronous mode => immediate response
        # we use future for future update (?)
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))

    # callback for when the service replies with the response
    def callback_set_pen(self, future):
        try:
            response = future.result()
        except Exception as e:
            # print exceptions in ROS2 easily
            self.get_logger().error("Service call failed: %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = turtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
