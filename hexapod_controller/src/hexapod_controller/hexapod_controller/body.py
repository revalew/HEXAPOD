#!/usr/bin/env python3
# My first Node!
import rclpy
from rclpy.node import Node

# from com_settings import *
from inverse_kinematics import body_ik

# impoort the msg type
# from turtlesim.msg import Pose

class AxlePoses():
    '''
    MESSAGE TYPE
    '''
    ID_pose = [0, ..., 18]
    def __init__(self):
        for i in self.ID_pose:
            i = 512


class BodyIKNode(Node):
    def __init__(self):
        super().__init__("body_IK")
       
        # self.get_logger().info("HEXAPOD body Inverse Kinematics calculation has been started.")

        # create publisher
        self.body_IK_ = self.create_publisher(AxlePoses, "/bodyIK_topic", 30) # FLAGA BLEDU
        self.timer_ = self.create_timer(2.0, self.send_data)
        
    def send_data(self):
        leg_values = body_ik(0, 0, 0, 0, 0, 0)
        
        # create the msg with the specific type
        cmd = AxlePoses()
        
        j, k = 0, 0
        for i in range(0, 18, 1):
            
            if i % 3 == 0:
                j += 1
                k = 0
            else: k += 1
            cmd.ID_pose[i + 1] = leg_values[j - 1][k]

        # publish the message 
        self.cmd_vel_publisher_.publish(cmd)
        
        # print(leg_values)
        

# class MotorControler(Node):
#     def __init__(self):
#         super().__init__("pose_subscriber")

#         # create an attribute to set subscriber:
#         # Pose => msg type --> what kind of msg do we expect to receive
#         # /turtle1/pose => topic we want to listen to
#         # pose_callback => callback function to process the received msg
#         # 10 => queue size
#         self.pose_subscriber_ = self.create_subscription(
#             Pose, "/bodyIK_topic", self.pose_callback, 10
#         )

#     def pose_callback(self, msg: Pose):
#         # we can do a "msg: Pose" to specify the type of the msg - like "long long d" ;)

#         self.get_logger().info(
#             "position of the turtle: (" + str(msg.x) + ", " + str(msg.y) + ")"
#         )

def main(args=None):
    rclpy.init(args=args)

    node = BodyIKNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()
