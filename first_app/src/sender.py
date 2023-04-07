#!/usr/bin/env python3
# My first Node!
import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node = Node("py_test")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()