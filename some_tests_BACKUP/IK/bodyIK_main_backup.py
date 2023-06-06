    #     create the leg subscriber
    #     self.pose_subsciber = self.create_subscription(ServoPositionValues, "bodyIK_topic", self.body_ik_inputs, 20)
        

    # def body_ik_inputs(self):
    #     '''
    #      Function to translate or rotate the body of the HEXAPOD in 6 degrees of freedom
    #      and calculate angles of all 18 axis
    #     '''
    #     data = [0,0,20,0,0,0]
    #     data1 = [0,0,20,0,0,0]
    #     data2 = [0,0,-20,0,0,0]
    #     data3 = [0,0,-20,0,0,0]
        
    #     goal_pos = [data, data1, data2, data3]
        
    #     leg_values = ik.body_ik(goal_pos[self.index][0],
    #                             goal_pos[self.index][1],
    #                             goal_pos[self.index][2],
    #                             goal_pos[self.index][3],
    #                             goal_pos[self.index][4],
    #                             goal_pos[self.index][5])
        
    #     # create the msg with the specific type
    #     cmd = ServoPositionValues()
        
    #     # sending the leg_values list returned from body_ik function
    #     # and publishing it to the bodyIK_topic topic as our custom msg type
    #     # eg. [0][1] leg one, second axis (femur)
    #     # eg. [1][2] leg two, third axis (tibia)
    #     j, k = 0, 0
    #     for i in range(0, 18, 1):
            
    #         if i % 3 == 0:
    #             j += 1
    #             k = 0
    #         else: k += 1
    #         cmd.id_pose[i] = leg_values[j - 1][k]
       
    #     # publish the message 
    #     self.body_IK_.publish(cmd)
        
    #     # change data for move demo -> top of function, data variables
    #     if self.index == 0:
    #         self.index = 1
    #     elif self.index == 1:
    #         self.index = 2
    #     elif self.index == 2:
    #         self.index = 3
    #     else: self.index = 0    