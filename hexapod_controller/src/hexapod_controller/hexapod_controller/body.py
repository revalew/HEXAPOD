#!/usr/bin/env python3
# My first Node!
import rclpy
from rclpy.node import Node

from hexapod_controller.com_settings import *
import hexapod_controller.inverse_kinematics as ik

# importing our new message type
from hexapod_controller_interfaces.msg import ServoPositionValues


class BodyIKNode(Node):
    def __init__(self):
        super().__init__("body_IK")
       
        self.get_logger().info("HEXAPOD body Inverse Kinematics calculation has been started.")

        # create publisher
        self.body_IK_ = self.create_publisher(ServoPositionValues, "bodyIK_topic", 10) # FLAGA BLEDU
        self.timer_ = self.create_timer(1, self.test_leg_ik)
        
        self.index = 0
        
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
    
    
    def test_leg_ik(self):
        cmd = ServoPositionValues()
        for x in range(20, -30, -10):
            time.sleep(0.1)
            leg_value_1 = ik.leg_ik_test(-x, 0)
            leg_value_2 = ik.leg_ik_test(-x, 1)
            leg_value_3 = ik.leg_ik_test(x, 2)
            leg_value_4 = ik.leg_ik_test(x, 3)
            leg_value_5 = ik.leg_ik_test(x, 4)
            leg_value_6 = ik.leg_ik_test(x, 5)
        
            # cmd.id_pose[0] = leg_value_1[0]
            # cmd.id_pose[1] = leg_value_1[1]
            # cmd.id_pose[2] = leg_value_1[2]
        
            cmd.id_pose[3] = leg_value_2[0]
            cmd.id_pose[4] = leg_value_2[1]
            cmd.id_pose[5] = leg_value_2[2]
            
            # cmd.id_pose[6] = leg_value_3[0]
            # cmd.id_pose[7] = leg_value_3[1]
            # cmd.id_pose[8] = leg_value_3[2]
            
            cmd.id_pose[15] = leg_value_4[0]
            cmd.id_pose[16] = leg_value_4[1]
            cmd.id_pose[17] = leg_value_4[2]
            
            # cmd.id_pose[12] = leg_value_5[0]
            # cmd.id_pose[13] = leg_value_5[1]
            # cmd.id_pose[14] = leg_value_5[2]
            
            cmd.id_pose[9] = leg_value_6[0]
            cmd.id_pose[10] = leg_value_6[1]
            cmd.id_pose[11] = leg_value_6[2]
            
            self.body_IK_.publish(cmd)
        
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
