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
    def __init__(self, id):
        super().__init__("pose_subscriber")
        
        self.id_id = id
        self.id_index = self.id_id - 1
        
        # -- LEGWAN -- 
        self.pose_subsciber = self.create_subscription(
            ServoPositionValues, "bodyIK_topic", self.pose_callback_id,10)
        
    # servo 1
    def pose_callback_id(self, msg: ServoPositionValues):
        print(f"Subscriber MotorController: received msg = {msg.id_pose[self.id_index]}")
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, self.id_id, ADDR_MX_GOAL_POSITION, msg.id_pose[self.id_index])
    
        
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
    
    executor = rclpy.executors.MultiThreadedExecutor()
    
    nodeSubscribers = [1,...,18]
    for i in range(18):
        nodeSubscribers[i] = MotorController(DXL_ID[i])
        executor.add_node(nodeSubscribers[i])
    
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
