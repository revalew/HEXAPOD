#!/usr/bin/env python3
# My first Node!
import rclpy
from rclpy.node import Node

from hexapod_controller.com_settings import *
import hexapod_controller.inverse_kinematics as ik

# importing our new message type
from hexapod_controller_interfaces.msg import ServoPositionValues
from hexapod_controller_interfaces.msg import LegGroup

class BodyIKNode(Node):    
    def __init__(self):
        super().__init__("body_IK")
       
        self.get_logger().info("HEXAPOD body Inverse Kinematics calculation has been started.")
        
        self.index = 0
        
        self.g_group_1_legs_up = 1
        self.g_group_2_legs_up = 0

        # create publisher
        # self.body_IK_ = self.create_publisher(ServoPositionValues, "bodyIK_topic", 10)
        self.group_1_pub_ = self.create_publisher(LegGroup, "leg_group_1", 10)
        self.group_2_pub_ = self.create_publisher(LegGroup, "leg_group_2", 10)
        # self.timer_ = self.create_timer(1, self.walking)
        self.timer_1_ = self.create_timer(3, self.group_1_walk)
        self.timer_2_ = self.create_timer(1, self.group_2_walk)
        
        # create the leg subscriber
        # self.pose_subsciber = self.create_subscription(ServoPositionValues, "bodyIK_topic", self.send_data, 20)
        
        # self.group_1_sub_ = self.create_subscription(LegGroup, "leg_group_1", self.group_1_walk, 20)
        # self.group_2_sub_ = self.create_subscription(LegGroup, "leg_group_2", self.group_2_walk, 20)
        
    def send_data(self):
        data = [0,0,20,0,0,0]
        data1 = [0,0,20,0,0,0]
        data2 = [0,0,-20,0,0,0]
        data3 = [0,0,-20,0,0,0]
        
        goal_pos = [data, data1, data2, data3]
        
        self.t = time.time()
        leg_values = ik.body_ik(goal_pos[self.index][0],
                                goal_pos[self.index][1],
                                goal_pos[self.index][2],
                                goal_pos[self.index][3],
                                goal_pos[self.index][4],
                                goal_pos[self.index][5])
        self.elapsed = time.time() - self.t
        self.get_logger().info('calculation took: %s' % (self.elapsed))
        
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
        
        if self.index == 0:
            self.index = 1
        elif self.index == 1:
            self.index = 2
        elif self.index == 2:
            self.index = 3
        else: self.index = 0       
    
    def group_1_walk(self, x_sign=1):
        cmd = LegGroup()
        index = 0
        variant = 0
        points = [20, 0, -20, -20, 0, 20]
        for x in points:
            time.sleep(0.2)
            '''
            forward: 
                leg_1: x < 0
                leg_3: x > 0
                leg_5: x > 0
            
            backward: 
                leg_1: x > 0
                leg_3: x < 0
                leg_5: x < 0
            '''
            
            if index > len(points) / 2 - 1 :
                variant = 1
                self.g_group_1_legs_up = 1
            else:
                self.g_group_1_legs_up = 0
            
            leg_value_1 = ik.leg_ik_test(-x * x_sign, 0, variant)
            leg_value_3 = ik.leg_ik_test(x * x_sign, 2, variant)
            leg_value_5 = ik.leg_ik_test(x * x_sign, 4, variant)
            
            cmd.group[0] = leg_value_1[0]
            cmd.group[1] = leg_value_1[1]
            cmd.group[2] = leg_value_1[2]
            
            cmd.group[3] = leg_value_3[0]
            cmd.group[4] = leg_value_3[1]
            cmd.group[5] = leg_value_3[2]
            
            cmd.group[6] = leg_value_5[0]
            cmd.group[7] = leg_value_5[1]
            cmd.group[8] = leg_value_5[2]
            
            self.group_1_pub_.publish(cmd)
            index += 1
            
    def group_2_walk(self, x_sign=1):
        cmd = LegGroup()
        index = 0
        variant = 0
        points = [20, 0, -20, -20, 0, 20]
        for x in points:
            time.sleep(0.2)
            '''
            forward: 
                leg_1: x > 0
                leg_3: x < 0
                leg_5: x > 0
            
            backward: 
                leg_1: x < 0
                leg_3: x > 0
                leg_5: x < 0
            '''
            
            if index > len(points) / 2 - 1 :
                variant = 1
                self.g_group_2_legs_up = 1
            else:
                self.g_group_2_legs_up = 0
            
            leg_value_2 = ik.leg_ik_test(x * x_sign, 1, variant)
            leg_value_4 = ik.leg_ik_test(-x * x_sign, 5, variant)
            leg_value_6 = ik.leg_ik_test(x * x_sign, 3, variant)
        
            cmd.group[0] = leg_value_2[0]
            cmd.group[1] = leg_value_2[1]
            cmd.group[2] = leg_value_2[2]
            
            cmd.group[3] = leg_value_4[0]
            cmd.group[4] = leg_value_4[1]
            cmd.group[5] = leg_value_4[2]
            
            cmd.group[6] = leg_value_6[0]
            cmd.group[7] = leg_value_6[1]
            cmd.group[8] = leg_value_6[2]
            
            self.group_2_pub_.publish(cmd)
            index += 1
    
    def walking(self, msg: ServoPositionValues):
        cmd = ServoPositionValues()
        
        index = 0
        index_2 = 0
        
        variant = 0
        variant_2 = 0
        
        points = [20, 0, -20, -20, 0, 20]
        x_sign = 1
        
        sleep_time = 0.1
        
        if (self.g_group_2_legs_up): 
            # self.group_2_walk(msg)
            for x in points:
                time.sleep(sleep_time)
                '''
                forward: 
                    leg_1: x < 0
                    leg_3: x > 0
                    leg_5: x > 0
                
                backward: 
                    leg_1: x > 0
                    leg_3: x < 0
                    leg_5: x < 0
                '''
                
                if index > len(points) / 2 - 1 :
                    variant = 1
                    self.g_group_1_legs_up = 1
                else:
                    self.g_group_1_legs_up = 0
                
                leg_value_1 = ik.leg_ik_test(-x * x_sign, 0, variant)
                leg_value_3 = ik.leg_ik_test(x * x_sign, 2, variant)
                leg_value_5 = ik.leg_ik_test(x * x_sign, 4, variant)
                
                cmd.id_pose[0] = leg_value_1[0]
                cmd.id_pose[1] = leg_value_1[1]
                cmd.id_pose[2] = leg_value_1[2]
                
                cmd.id_pose[6] = leg_value_3[0]
                cmd.id_pose[7] = leg_value_3[1]
                cmd.id_pose[8] = leg_value_3[2]
                
                cmd.id_pose[12] = leg_value_5[0]
                cmd.id_pose[13] = leg_value_5[1]
                cmd.id_pose[14] = leg_value_5[2]
                
                cmd.id_pose[3] = msg.id_pose[3]
                cmd.id_pose[4] = msg.id_pose[4]
                cmd.id_pose[5] = msg.id_pose[5]
                
                cmd.id_pose[15] = msg.id_pose[15]
                cmd.id_pose[16] = msg.id_pose[16]
                cmd.id_pose[17] = msg.id_pose[17]
                
                cmd.id_pose[9] = msg.id_pose[9]
                cmd.id_pose[10] = msg.id_pose[10]
                cmd.id_pose[11] = msg.id_pose[11]
                
                self.body_IK_.publish(cmd)
                index += 1
                
        elif (self.g_group_1_legs_up): 
            # self.group_1_walk(msg)
            for y in points:
                time.sleep(sleep_time)
                '''
                forward: 
                    leg_1: x > 0
                    leg_3: x < 0
                    leg_5: x > 0
                
                backward: 
                    leg_1: x < 0
                    leg_3: x > 0
                    leg_5: x < 0
                '''
                
                if index_2 > len(points) / 2 - 1 :
                    variant_2 = 1
                    self.g_group_2_legs_up = 1
                else:
                    self.g_group_2_legs_up = 0
                
                leg_value_2 = ik.leg_ik_test(y * x_sign, 1, variant_2)
                leg_value_4 = ik.leg_ik_test(-y * x_sign, 5, variant_2)
                leg_value_6 = ik.leg_ik_test(y * x_sign, 3, variant_2)
            
                cmd.id_pose[3] = leg_value_2[0]
                cmd.id_pose[4] = leg_value_2[1]
                cmd.id_pose[5] = leg_value_2[2]
                
                cmd.id_pose[15] = leg_value_4[0]
                cmd.id_pose[16] = leg_value_4[1]
                cmd.id_pose[17] = leg_value_4[2]
                
                cmd.id_pose[9] = leg_value_6[0]
                cmd.id_pose[10] = leg_value_6[1]
                cmd.id_pose[11] = leg_value_6[2]
                
                cmd.id_pose[0] = msg.id_pose[0]
                cmd.id_pose[1] = msg.id_pose[1]
                cmd.id_pose[2] = msg.id_pose[2]
                
                cmd.id_pose[6] = msg.id_pose[6]
                cmd.id_pose[7] = msg.id_pose[7]
                cmd.id_pose[8] = msg.id_pose[8]
                
                cmd.id_pose[12] = msg.id_pose[12]
                cmd.id_pose[13] = msg.id_pose[13]
                cmd.id_pose[14] = msg.id_pose[14]
                
                self.body_IK_.publish(cmd)
                index_2 += 1
        
        
def gain_strength(DXL_ID):
    # ENABLE TORQUE
    for i in DXL_ID:
        # Enable Dynamixel Torque
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, i, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
        time.sleep(0.1)
   
        
def loose_strength(DXL_ID):
    # DISABLE TORQUE
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
