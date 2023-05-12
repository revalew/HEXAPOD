#!/usr/bin/env python3
# My first Node!
import rclpy
from rclpy.node import Node

import threading

from hexapod_controller.com_settings import *
import hexapod_controller.inverse_kinematics as ik

# importing our new message type
from hexapod_controller_interfaces.msg import ServoPositionValues

# Class dedicated to operate specyfic axis as objects
class PoseCallback():
    
    def __init__(self, index, msg: ServoPositionValues):
        self.index1 = index
        self.position1 = msg.id_pose[index]
    
    def rotateAxis(self, index, position1):
        print(f"Subscriber MotorController: received msg = {self.position1}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, self.index1 + 1, ADDR_MX_GOAL_POSITION, self.position1)


class BodyIKNode(Node):
    def __init__(self):
        super().__init__("body_IK")
       
        self.get_logger().info("HEXAPOD body Inverse Kinematics calculation has been started.")

        # create publisher
        self.body_IK_ = self.create_publisher(ServoPositionValues, "bodyIK_topic", 10) # FLAGA BLEDU
        self.timer_ = self.create_timer(2.0, self.send_data)
        
    def send_data(self):
        leg_values = ik.body_ik(0, 0, -5, 0, 0, 0)
        
        # create the msg with the specific type
        cmd = ServoPositionValues()
        
        j, k = 0, 0
        for i in range(0, 18, 1):
            
            if i % 3 == 0:
                j += 1
                k = 0
            else: k += 1
            cmd.id_pose[i] = leg_values[j - 1][k]
            # cmd.id_pose[i] = 512

        # publish the message 
        self.body_IK_.publish(cmd)
        
        print(f"\n {leg_values}")
        # print(cmd)
        

class MotorController(Node):
    def __init__(self):
        super().__init__("pose_subscriber")
        
        
        # ---------- REZERWAT PRZYTODY - NAUKA SENIORA TOP OOP PYTHON DELOPER ------------
        # self.poseCallback_id1 = PoseCallback(index=0, msg=msg.)
        # self.poseCallback_id2 = PoseCallback(index=1, msg=ServoPositionValues)
        # self.poseCallback_id3 = PoseCallback(index=2, msg=ServoPositionValues)
        # self.pose_subscriber_1 = self.create_subscription(
        #     ServoPositionValues, "bodyIK_topic", self.poseCallback_id1.rotateAxis(0,ServoPositionValues), 10)
        
        # self.pose_subscriber_2 = self.create_subscription(
        #     ServoPositionValues, "bodyIK_topic", self.poseCallback_id2.rotateAxis(1,ServoPositionValues), 10)
        
        # self.pose_subscriber_3 = self.create_subscription(
        #     ServoPositionValues, "bodyIK_topic", self.poseCallback_id3.rotateAxis(2,ServoPositionValues), 10)
        # ----------------------------------------------------------------------------------  
        
        
        # create an attribute to set subscriber:
        # Pose => msg type --> what kind of msg do we expect to receive
        # /turtle1/pose => topic we want to listen to
        # pose_callback => callback function to process the received msg
        # 10 => queue size
        
        # -- LEGWAN -- 
        self.pose_subsciber_1 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_1,10)
        self.pose_subsciber_2 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_2,10)
        self.pose_subsciber_3 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_3,10)
        
        # -- LEGTO -- 
        self.pose_subsciber_4 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_4,10)
        self.pose_subsciber_5 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_5,10)
        self.pose_subsciber_6 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_6,10)
        
        # -- LECHFREE -- 
        self.pose_subsciber_7 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_7,10)
        self.pose_subsciber_8 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_8,10)
        self.pose_subsciber_9 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_9,10)
        
        # -- LEG 4 -- 
        self.pose_subsciber_10 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_10,10)
        self.pose_subsciber_11 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_11,10)
        self.pose_subsciber_12 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_12,10)
        
        # -- LEGFAJF -- 
        self.pose_subsciber_13 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_13,10)
        self.pose_subsciber_14 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_14,10)
        self.pose_subsciber_15 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_15,10)
        
        # -- LEXUS -- 
        self.pose_subsciber_16 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_16,10)
        self.pose_subsciber_17 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_17,10)
        self.pose_subsciber_18 = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id_18,10)
        

    # servo 1
    def pose_callback_id_1(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[0]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 1, ADDR_MX_GOAL_POSITION, msg.id_pose[0])
    # servo 2
    def pose_callback_id_2(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[1]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 2, ADDR_MX_GOAL_POSITION, msg.id_pose[1])
    # servo 3
    def pose_callback_id_3(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[2]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 3, ADDR_MX_GOAL_POSITION, msg.id_pose[2])
        
    # servo 4
    def pose_callback_id_4(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[3]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 4, ADDR_MX_GOAL_POSITION, msg.id_pose[3])
    # servo 5
    def pose_callback_id_5(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[4]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 5, ADDR_MX_GOAL_POSITION, msg.id_pose[4])
    # servo 6
    def pose_callback_id_6(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[5]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 6, ADDR_MX_GOAL_POSITION, msg.id_pose[5])
    
    # servo 7
    def pose_callback_id_7(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[6]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 7, ADDR_MX_GOAL_POSITION, msg.id_pose[6])
    # servo 8
    def pose_callback_id_8(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[7]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 8, ADDR_MX_GOAL_POSITION, msg.id_pose[7])
    # servo 9
    def pose_callback_id_9(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[8]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 9, ADDR_MX_GOAL_POSITION, msg.id_pose[8])
    
    # servo 10
    def pose_callback_id_10(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[9]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 16, ADDR_MX_GOAL_POSITION, msg.id_pose[9])
    # servo 11
    def pose_callback_id_11(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[10]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 17, ADDR_MX_GOAL_POSITION, msg.id_pose[10])
    # servo 12
    def pose_callback_id_12(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[11]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 18, ADDR_MX_GOAL_POSITION, msg.id_pose[11])
    
    # servo 13
    def pose_callback_id_13(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[12]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 13, ADDR_MX_GOAL_POSITION, msg.id_pose[12])
    # servo 14
    def pose_callback_id_14(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[13]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 14, ADDR_MX_GOAL_POSITION, msg.id_pose[13])
    # servo 15
    def pose_callback_id_15(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[14]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 15, ADDR_MX_GOAL_POSITION, msg.id_pose[14])
    
    # servo 16
    def pose_callback_id_16(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[15]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 10, ADDR_MX_GOAL_POSITION, msg.id_pose[15])
    # servo 17
    def pose_callback_id_17(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[16]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 11, ADDR_MX_GOAL_POSITION, msg.id_pose[16])
    # servo 18
    def pose_callback_id_18(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[17]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, 12, ADDR_MX_GOAL_POSITION, msg.id_pose[17])
    
   
        
        
def gain_strength(DXL_ID):
    # global packetHandler, portHandler, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE
    # ENABLE =================
    for i in DXL_ID:
        # Enable Dynamixel Torque
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, i, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
        time.sleep(0.05)
   
        
def loose_strength(DXL_ID):
    # global packetHandler, portHandler, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE
    # DISABLE =================
    for i in range(1, 19):
        DXL_ID = i
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
        time.sleep(0.05)
    
    
def stewpid_init():
    global packetHandler, portHandler, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE
    # Open port
    if portHandler.openPort():
        print("Succeeded to open the port")
    else:
        print("Failed to open the port")
        print("Press any key to terminate...")
        getch()
        quit()

    # Set port baudrate
    if portHandler.setBaudRate(BAUDRATE):
        print("Succeeded to change the baudrate")
    else:
        print("Failed to change the baudrate")
        print("Press any key to terminate...")
        getch()
        quit()
    # ------------------------------------------------------------


def main(args=None):
    stewpid_init()
    
    # LIST OF IDs
    DXL_ID = [1,2,3,4,5,6,7,8,9,16,17,18,13,14,15,10,11,12]
    
    # ENABLE TORQUE
    gain_strength(DXL_ID)
    
    rclpy.init(args=args)
    nodePublish = BodyIKNode()
    nodeSubscribers = MotorController()
    
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(nodePublish)
    executor.add_node(nodeSubscriber_1)
    executor.add_node(nodeSubscriber_2)
    executor.add_node(nodeSubscriber_3)
    executor.add_node(nodeSubscriber_4)
    executor.add_node(nodeSubscriber_5)
    executor.add_node(nodeSubscriber_6)
    executor.add_node(nodeSubscriber_7)
    executor.add_node(nodeSubscriber_8)
    executor.add_node(nodeSubscriber_9)
    executor.add_node(nodeSubscriber_10)
    executor.add_node(nodeSubscriber_11)
    executor.add_node(nodeSubscriber_12)
    executor.add_node(nodeSubscriber_13)
    executor.add_node(nodeSubscriber_14)
    executor.add_node(nodeSubscriber_15)
    executor.add_node(nodeSubscriber_16)
    executor.add_node(nodeSubscriber_17)
    executor.add_node(nodeSubscriber_18)
    
    # Spin in a separate thread
    # you spin me right now, baby right now
    # https://www.youtube.com/watch?v=PGNiXGX2nLU&ab_channel=DeadOrAliveVEVO
    executor_thread = threading.Thread(target=executor.spin(), daemon=True)
    executor_thread.start()
    rclpy.shutdown()
    executor_thread.join()

    # DISABLE TORQUE
    loose_strength(DXL_ID)
    
    # Close port
    portHandler.closePort()

if __name__ == "__main__":
    main()
