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

class BodyIKNode(Node):    
    def __init__(self):
        super().__init__("body_IK")
        self.get_logger().info("HEXAPOD's brain has started.")
        self.index = 0
        self.controll_status_pub_ = self.create_publisher(ControllStatus, "control_status", 10)
        self.timer_ = self.create_timer(1.8, self.group_walk)   
        #self.timer_ = self.create_timer(0.1, self.robot_state_machine_callback)
    
    def group_walk(self, x=1):
        '''
         Function to schedule the leg sequences depending on the chosen gait pattern
         x : 1 => move forward, -1 => move backward
        '''
        cmd = ControllStatus()
        cmd.status_name = "walk_tripod"
        # cmd.variable_1 = x
        self.controll_status_pub_.publish(cmd) 
        
        
    # !!! --- WORK IN PROGRESS BELOW ---
    
    # TODO think about robot state machine
    def robot_state_machine_callback(self):
        
        # ?? walk
        
        # ?? rotate
        
        # ?? initialize
        
        # ?? demo
        
        # ?? reset
        
        # ?? idle
        
        pass
    
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
