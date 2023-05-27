#!/usr/bin/env python3
# My first Node!
import rclpy
from rclpy.node import Node

from hexapod_controller.com_settings import *
import hexapod_controller.inverse_kinematics as ik
from hexapod_controller.inverse_kinematics_params import *

# importing our new message type
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
         Function dedicated to translate or rotate body of hexapod in 6 degrees of freedom, 
         calculate angles of each of all 18 axes
        '''
        data = [0,0,20,0,0,0]
        data1 = [0,0,20,0,0,0]
        data2 = [0,0,-20,0,0,0]
        data3 = [0,0,-20,0,0,0]
        
        goal_pos = [data, data1, data2, data3]
        
        # self.t = time.time()
        leg_values = ik.body_ik(goal_pos[self.index][0],
                                goal_pos[self.index][1],
                                goal_pos[self.index][2],
                                goal_pos[self.index][3],
                                goal_pos[self.index][4],
                                goal_pos[self.index][5])
        # self.elapsed = time.time() - self.t
        # self.get_logger().info('calculation took: %s' % (self.elapsed))
        
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
         Function dedicated to scheduling leg sequences depending on gait
         x = 1 # <-- move forward, change to -1 to go backward
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
        # Enable Dynamixel Torque
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
