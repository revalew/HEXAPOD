from hexapod_controller.inverse_kinematics_params import *

def body_ik(pos_x_input, pos_y_input, pos_z_input, rot_x_input, rot_y_input, rot_z_input):
    # INFO - function calculate a body inverse kinematics
    # INPUTS - desire positions in 6 def of freedom
    # OUTPUT - angle for each motor ex. leg_value[1][2] is a tibia angle for seccond leg

    # control inputs
    pos_x = pos_x_input
    pos_y = pos_y_input
    pos_z = pos_z_input
    
    rot_x = rot_x_input
    rot_y = rot_y_input
    rot_z = rot_z_input
    
    ## --------------------------------------------- ##
    # BODY IK - STEP 4
   
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

def leg_ik(x, id, variant):    
    leg = id
    b = 40
    a = 20
    
    # we need the elipse / circle without the x translation
    if variant : z = 0 
    else : z = mh.sqrt((b ** 2) - ((x ** 2) * (b ** 2) / (a ** 2)))

    # positions iks kurde belka de
    # alpha = mh.radians(leg_rot_angle[leg])
    alpha = mh.radians(leg_rot_angle[leg] + leg_rot_angle_offset[leg])
    # alpha = leg_rot_angle[leg] + 30
    pos_x = x * mh.cos(alpha)
    pos_y = x * mh.sin(alpha)
    pos_z = -z
    
    # leg ik
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

    
    # leg angles
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

    
    # print(f"coxa_angle: {coxa_angle}")
    # print(f"ik_coxa_angle: {ik_coxa_angle}")
    return leg_values[leg]
