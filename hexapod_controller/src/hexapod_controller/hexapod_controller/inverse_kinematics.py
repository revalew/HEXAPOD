import math as mh
# from com_settings import *

def body_ik(pos_x_input, pos_y_input, pos_z_input, rot_x_input, rot_y_input, rot_z_input):
    # INFO - function calculate a body inverse kinematics
    # INPUTS - desire positions in 6 def of freedom
    # OUTPUT - angle for each motor ex. leg_value[1][2] is a tibia angle for seccond leg


    ## --------------------------------------------- ##
    # DIRECT INPUTS - STEP 1
    # robot geometry
    COXA_LENGTH = 85
    FEMUR_LENGTH = 68
    TIBIA_LENGTH = 125

    # control inputs
    pos_x = pos_x_input
    pos_y = pos_y_input
    pos_z = pos_z_input
    
    rot_x = rot_x_input
    rot_y = rot_y_input
    rot_z = rot_z_input


    ## --------------------------------------------- ##
    # PRIMARY GEOMETRIC CALCULATIONS - STEP 2

    # body center offset x
    BODY_CENTER_OFFSET_X = (70,100,70,-70,-100,-70)

    # body center offset y
    BODY_CENTER_OFFSET_Y = (70,0,-70,-70,0,70)


    ## --------------------------------------------- ##
    # INITIAL FEET POSITIONS - STEP 3

    feet_pos_x = [0,0,0,0,0,0]
    feet_pos_z = [0,0,0,0,0,0]
    feet_pos_y = [0,0,0,0,0,0]

    # leg 1
    feet_pos_x[0] = mh.cos(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH)
    feet_pos_z[0] = TIBIA_LENGTH
    feet_pos_y[0] = mh.sin(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH)


    # Leg 2
    feet_pos_x[1] = COXA_LENGTH + FEMUR_LENGTH
    feet_pos_z[1] = TIBIA_LENGTH
    feet_pos_y[1] = 0

    # leg 3
    feet_pos_x[2] = mh.cos(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH)
    feet_pos_z[2] = TIBIA_LENGTH
    feet_pos_y[2] = -1 * (mh.sin(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH))

    # leg 4
    feet_pos_x[3] = -1 * (mh.cos(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH))
    feet_pos_z[3] = TIBIA_LENGTH
    feet_pos_y[3] = -1 * (mh.sin(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH))

    # Leg 5
    feet_pos_x[4] = -1 * (COXA_LENGTH + FEMUR_LENGTH)
    feet_pos_z[4] = (TIBIA_LENGTH)
    feet_pos_y[4] = 0

    # leg 6
    feet_pos_x[5] = -1 * (mh.cos(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH))
    feet_pos_z[5] = TIBIA_LENGTH
    feet_pos_y[5] = mh.sin(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH)


    ## --------------------------------------------- ##
    # BODY IK - STEP 4

    # list init
    total_x = [0,0,0,0,0,0]
    total_y = [0,0,0,0,0,0]
    dist_body_center_feet = [0,0,0,0,0,0]
    angle_body_center_x = [0,0,0,0,0,0]
    roll_z = [0,0,0,0,0,0]
    pitch_z = [0,0,0,0,0,0]
    body_ik_x = [0,0,0,0,0,0]
    body_ik_y = [0,0,0,0,0,0]
    body_ik_z = [0,0,0,0,0,0]

    # body ik
    for leg in range(0, 6, 1):
        total_y[leg] = feet_pos_y[leg] + BODY_CENTER_OFFSET_Y[leg] + pos_y
        total_x[leg] = feet_pos_x[leg] + BODY_CENTER_OFFSET_X[leg] + pos_x
        dist_body_center_feet[leg] = mh.sqrt((total_y[leg]**2) + (total_x[leg]**2))
        angle_body_center_x[leg] = (mh.pi / 2) - mh.atan2(total_x[leg], total_y[leg])
        roll_z[leg] = mh.tan(rot_y * mh.pi/180) * total_x[leg]
        pitch_z[leg] = mh.tan(rot_x * mh.pi/180) * total_y[leg]

        body_ik_x[leg] = mh.cos(angle_body_center_x[leg] + (rot_z * mh.pi / 180)) * dist_body_center_feet[leg] - total_x[leg]
        body_ik_y[leg] = (mh.sin(angle_body_center_x[leg] + (rot_z * mh.pi / 180))*dist_body_center_feet[leg]) - total_y[leg]
        body_ik_z[leg] = roll_z[leg] + pitch_z[leg]


    ## --------------------------------------------- ##
    # LEG IK - STEP 5

    # list init
    new_pos_x = [0,0,0,0,0,0]
    new_pos_y = [0,0,0,0,0,0]
    new_pos_z = [0,0,0,0,0,0]
    coxa_feet_dist = [0,0,0,0,0,0]
    ik_sw = [0,0,0,0,0,0]
    ik_a1 = [0,0,0,0,0,0]
    ik_a2 = [0,0,0,0,0,0]
    t_angle = [0,0,0,0,0,0]
    ik_tibia_angle = [0,0,0,0,0,0]
    ik_femur_angle = [0,0,0,0,0,0]
    ik_coxa_angle = [0,0,0,0,0,0]

    # leg ik
    for leg in range(0, 6, 1):
        new_pos_x[leg] = pos_x + feet_pos_x[leg] + body_ik_x[leg]
        new_pos_y[leg] = pos_y + feet_pos_y[leg] + body_ik_y[leg]
        new_pos_z[leg] = pos_z + feet_pos_z[leg] + body_ik_z[leg]
        coxa_feet_dist[leg] = mh.sqrt(new_pos_x[leg]**2 + new_pos_y[leg]**2)
        ik_sw[leg] = mh.sqrt((coxa_feet_dist[leg] - COXA_LENGTH)**2 + new_pos_z[leg]**2)
        ik_a1[leg] = mh.atan((coxa_feet_dist[leg] - COXA_LENGTH) / new_pos_z[leg])
        ik_a2[leg] = mh.acos((TIBIA_LENGTH**2 - FEMUR_LENGTH**2 - ik_sw[leg]**2) / (-2 * ik_sw[leg] * FEMUR_LENGTH))
        t_angle[leg] = mh.acos((ik_sw[leg]**2 - TIBIA_LENGTH**2 - FEMUR_LENGTH**2) / (-2 * ik_sw[leg] * FEMUR_LENGTH))

        ik_tibia_angle[leg] = 90 - (ik_a1[leg] + ik_a2[leg]) * 180 / mh.pi
        ik_femur_angle[leg] = 90 - (ik_a1[leg] + ik_a2[leg]) * 180 / mh.pi
        ik_coxa_angle[leg] = 90 - mh.atan2(new_pos_x[leg], new_pos_y[leg]) * 180 / mh.pi


    ## --------------------------------------------- ##
    # LEG ANGLES - STEP 6

    # list init
    coxa_angle = [0,0,0,0,0,0]
    femur_angle = [0,0,0,0,0,0]
    tibia_angle = [0,0,0,0,0,0]
    coxa_servo_angle = [0,0,0,0,0,0]
    femur_servo_angle = [0,0,0,0,0,0]
    tibia_servo_angle = [0,0,0,0,0,0]
    coxa_servo_value = [0,0,0,0,0,0]
    femur_servo_value = [0,0,0,0,0,0]
    tibia_servo_value = [0,0,0,0,0,0]

    # specyfic leg rotation angle
    leg_rot_angle = [-90, 0 , 90, -270, -180, -90]

    # specyfic leg angle inverse, if "-1" that means it rotates servo angle in for loop
    # you can simply give all ones here, and rotate phisical motor
    coxa_angle_inverse_flag = [1, 1, 1, 1, 1, 1]
    femur_angle_inverse_flag = [-1, -1, -1, 1, 1, 1]
    tibia_angle_inverse_flag = [1, 1, 1, -1, -1, -1]

    # return array init
    leg_values = [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]]

    # leg angles
    for leg in range(0, 6, 1):
        
        # leg inverse kinematics angles
        coxa_angle[leg] = ik_coxa_angle[leg] + leg_rot_angle[leg]
        femur_angle[leg] = ik_femur_angle[leg]
        tibia_angle[leg] = ik_tibia_angle[leg]

        # servo angles
        coxa_servo_angle[leg] =  coxa_angle_inverse_flag[leg] * coxa_angle[leg] + 150
        femur_servo_angle[leg] = femur_angle_inverse_flag[leg] * femur_angle[leg] + 150
        tibia_servo_angle[leg] = tibia_angle_inverse_flag[leg] * tibia_angle[leg] + 150

        # servo values Dynamixel motors A12, rates (0 - 1023), min-max angles (0 - 300deg)
        coxa_servo_value[leg] = coxa_servo_angle[leg] / 300 * 1023
        femur_servo_value[leg] = femur_servo_angle[leg] / 300 * 1023
        tibia_servo_value[leg] = tibia_servo_angle[leg] / 300 * 1023

        # saves values for return
        leg_values[leg][0] = int(coxa_servo_value[leg])
        leg_values[leg][1] = int(femur_servo_value[leg])
        leg_values[leg][2] = int(tibia_servo_value[leg])


    ## --------------------------------------------- ##
    return leg_values