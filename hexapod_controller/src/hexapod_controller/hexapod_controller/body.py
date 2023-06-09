#!/usr/bin/env python3

'''
    File info:
    Hexapod's main file. This is a brain of our robot. 
    By publishing a state status we can control our robot.
'''


# ROS imports
import rclpy
from rclpy.node import Node

# communication settings
from hexapod_controller.com_settings import *

# Inverse Kinematics calculations
from hexapod_controller.inverse_kinematics_params import *
import hexapod_controller.inverse_kinematics as ik

# import custom message types
from hexapod_controller_interfaces.msg import ServoPositionValues
from hexapod_controller_interfaces.msg import Leg
from hexapod_controller_interfaces.msg import ControllStatus
from hexapod_controller_interfaces.msg import BodyIKCalculate

class BodyIKNode(Node):    
    def __init__(self):
        super().__init__("body_IK")
        self.get_logger().info("HEXAPOD's brain has started.")
        
        self.index       = 0
        self.robot_state = "idle"
        
        self.controll_status_pub_ = self.create_publisher(ControllStatus, "control_status", 10)
        self.keyboard_callback_sub_ = self.create_subscription(BodyIKCalculate, "body_IK_calculations", self.keyboard_callback, 20)
        
        self.timer_ = self.create_timer(1.8, self.robot_state_machine_callback)
    
    
    def group_walk(self, x=1):
        '''
         Function to schedule the leg sequences depending on the chosen gait pattern
         x : 1 => move forward, -1 => move backward
        '''
        cmd = ControllStatus()
        cmd.status_name = "walk_tripod"
        self.controll_status_pub_.publish(cmd) 
        
        
    def group_rotate_left(self, x=1):
        '''
            Rotate the robot anti-clockwise
        '''
        cmd = ControllStatus()
        cmd.status_name = "rotate_left_tripod"
        # cmd.variable_1 = x
        self.controll_status_pub_.publish(cmd) 
        
        
    def group_rotate_right(self, x=1):
        '''
            Rotate the robot clockwise
        '''
        cmd = ControllStatus()
        cmd.status_name = "rotate_right_tripod"
        # cmd.variable_1 = x
        self.controll_status_pub_.publish(cmd)
        
        
    def group_body_manipulation(self):
        '''
            Manipulate the position of the body
        '''
        cmd = ControllStatus()
        cmd.status_name = "body_manipulation"
        self.controll_status_pub_.publish(cmd)
        
        
    def keyboard_callback(self, msg: BodyIKCalculate):
        self.robot_state = msg.robot_state
        
    # !!! --- WORK IN PROGRESS BELOW ---
    def robot_state_machine_callback(self):
        
        
        # walk
        if (self.robot_state == "walk"):
            self.get_logger().info("HEXAPOD's status: walk.")
            self.group_walk()
        
        # rotate_left
        elif (self.robot_state == "rotate_left"):
            self.get_logger().info("HEXAPOD's status: rotate_left.")
            self.group_rotate_left()
        
        # rotate_right
        elif (self.robot_state == "rotate_right"):
            self.get_logger().info("HEXAPOD's status: rotate_right.")
            self.group_rotate_right()
        
        # ?? initialize
        
        # ?? demo
        
        # ?? reset
        
        # manipulate the body
        elif (self.robot_state == "body_manipulation"):
            self.get_logger().info("HEXAPOD's status: body_manipulation.")
            self.group_body_manipulation()
            
        # idle
        else:
            self.get_logger().info("HEXAPOD's status: idle.")
    # !!! -----------------------------
        
        
def gain_strength(DXL_ID):
    '''
     Enable torque on all 18 axes
    '''
    for i in DXL_ID:
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, i, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
        time.sleep(0.1)
   
        
def loose_strength(DXL_ID):
    '''
     Disable torque on all 18 axes
    '''
    for i in range(1, 19):
        DXL_ID = i
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
        time.sleep(0.05)


def main(args=None):
    # LIST OF IDs
    DXL_ID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    
    # ENABLE TORQUE
    gain_strength(DXL_ID)
    
    # CREATE THE NODE
    rclpy.init(args=args)
    nodePublish = BodyIKNode()    
    rclpy.spin(nodePublish)
    rclpy.shutdown()

    # DISABLE TORQUE
    loose_strength(DXL_ID)
    
    # CLOSE PORT
    portHandler.closePort()
    

if __name__ == "__main__":
    main()
