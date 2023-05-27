#!/usr/bin/env python3
# My first Node!
import rclpy
from rclpy.node import Node

from hexapod_controller.com_settings import *
import hexapod_controller.inverse_kinematics as ik

# importing our new message type
from hexapod_controller_interfaces.msg import ServoPositionValues
from hexapod_controller_interfaces.msg import Leg

class BodyIKNode(Node):    
    def __init__(self):
        super().__init__("body_IK")
       
        self.get_logger().info("HEXAPOD body Inverse Kinematics calculation has been started.")
        
        self.index = 0
        
        # first walking gait
        self.walking_gait = "tripod"
        
        # row -> leg
        # column -> if leg of leg is in the air
        # leg1 === --- === --- === ---
        # leg2 --- === --- === --- ===
        # leg3 === --- === --- === ---
        # leg4 --- === --- === --- ===
        # leg5 === --- === --- === ---
        # leg6 --- === --- === --- ===
        
        # index = ax number, value = leg up or down, 
        # === means up, --- means down
        # 1 means up, 0 means down
        
        if self.walking_gait == "tripod":                               # FLAGA BLEDU 
            self.leg_gait_status = [[1,0,1,0,1,0],
                                    [0,1,0,1,0,1],
                                    [1,0,1,0,1,0],
                                    [0,1,0,1,0,1],
                                    [1,0,1,0,1,0],
                                    [0,1,0,1,0,1],]

        # create publishers for each leg
        # self.body_IK_ = self.create_publisher(ServoPositionValues, "bodyIK_topic", 10)
        
        self.leg_pub = [None] * 6 # FLAGA BLEDU
        for leg in range(6):
            topic_name = "leg_" + str(leg + 1)
            self.leg_pub[leg] = self.create_publisher(Leg, topic_name, 10)  # FLAGA BLEDU
        
        self.timer_ = self.create_timer(3, self.group_walk)

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
        
        # change data for move demo -> top of function, data variables
        if self.index == 0:
            self.index = 1
        elif self.index == 1:
            self.index = 2
        elif self.index == 2:
            self.index = 3
        else: self.index = 0       
    
    
    def group_walk(self):
        '''
         Function dedicated to scheduling leg sequences depending on gait
        '''
        # constants
        GITE_SIZE = 6
        NUMBER_OF_LEGS = 6
                      # leg direction in coxa axis swap, preventing wrong movement
        
        # variables
        x = 1 # <-- move forward, change to -1 to go backward
        
        # iterating over gait table - column
        for gait_index in range(GITE_SIZE):
            # iterating over legs gait table - rows
            for gait_leg in range(NUMBER_OF_LEGS):
                self.leg_trajectory(id=gait_leg, forward=x, up_or_down=self.leg_gait_status[gait_leg][gait_index]) # FLAGA BLEDU
            
            
    def leg_trajectory(self, id, forward, up_or_down):
        '''
         Function dedicated to move specyfic leg in meaning of walking forward / backward
         id = id of leg
         x = forward -> 1, backward -> -1
         up_or_down = if 1 it means that leg should be in air
         rot_angle = trajectory line rotation in space, for future development, hexa rotation
         leg_direction = leg direction in coxa axis swap, preventing wrong movement
        '''
        
        # empty msg type initialization, with default values
        cmd = Leg()
        
        # variables
        variant     = 0
        WAIT_TIME   = 0.2                                   # FLAGA BLEDU zwiekszyc?
        LEG_DIRECTION_SWAP = [1,-1,1,-1,1,-1] 
        points      = [p for p in range(20,-25,-5)]  # FLAGA BLEDU
        
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
        
        # step logic
        if up_or_down:
            variant     = 0
            # points      = [p for p in range(20,-25,-5)]  # FLAGA BLEDU
        else:
            variant     = 1
            # points      = [p for p in range(-20,25,5)]   # FLAGA BLEDU tak listować punkty?
            
        # leg inverse kinematics calculations and msg publications
        # do this for every point in trajectory
        for x in points:
            # give some time for hardware to move
            time.sleep(WAIT_TIME)

            leg_value = ik.leg_ik(x*LEG_DIRECTION_SWAP[id], id, variant)      # FLAGA BLEDU x * forward?
            cmd.coxa = leg_value[0] # coxa leg value
            cmd.femur = leg_value[1] # femur leg value
            cmd.tibia = leg_value[2] # tibia leg value
            print(id)
            print(cmd)
            
            # publishing values of leg axises for every iteration, for every point
            self.leg_pub[id].publish(cmd)
        
        
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
