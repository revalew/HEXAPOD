#!/usr/bin/env python3

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
        self.get_logger().info("HEXAPOD body Inverse Kinematics calculation has been started.")
        self.index = 0
        self.controll_status_pub_ = self.create_publisher(ControllStatus, "control_status", 10)
        self.timer_ = self.create_timer(2, self.group_walk)

        # create the leg subscriber
        # self.pose_subsciber = self.create_subscription(ServoPositionValues, "bodyIK_topic", self.body_ik_inputs, 20)
        

    def body_ik_inputs(self):
        '''
         Function to translate or rotate the body of the HEXAPOD in 6 degrees of freedom
         and calculate angles of all 18 axis
        '''
        data = [0,0,20,0,0,0]
        data1 = [0,0,20,0,0,0]
        data2 = [0,0,-20,0,0,0]
        data3 = [0,0,-20,0,0,0]
        
        goal_pos = [data, data1, data2, data3]
        
        leg_values = ik.body_ik(goal_pos[self.index][0],
                                goal_pos[self.index][1],
                                goal_pos[self.index][2],
                                goal_pos[self.index][3],
                                goal_pos[self.index][4],
                                goal_pos[self.index][5])
        
        # create the msg with the specific type
        cmd = ServoPositionValues()
        
        # sending the leg_values list returned from body_ik function
        # and publishing it to the bodyIK_topic topic as our custom msg type
        # eg. [0][1] leg one, second axis (femur)
        # eg. [1][2] leg two, third axis (tibia)
        j, k = 0, 0
        for i in range(0, 18, 1):
            
            if i % 3 == 0:
                j += 1
                k = 0
            else: k += 1
            cmd.id_pose[i] = leg_values[j - 1][k]
       
        # publish the message 
        self.body_IK_.publish(cmd)
        
        # change data for move demo -> top of function, data variables
        if self.index == 0:
            self.index = 1
        elif self.index == 1:
            self.index = 2
        elif self.index == 2:
            self.index = 3
        else: self.index = 0       
    
    
    def group_walk(self, x=1):
        '''
         Function to schedule the leg sequences depending on the chosen gait pattern
         
         x : 1 => move forward, -1 => move backward
        '''
        cmd = ControllStatus()
        cmd.status_name = "walk_tripod"
        cmd.variable_1 = x
        self.controll_status_pub_.publish(cmd) 
        
        
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
