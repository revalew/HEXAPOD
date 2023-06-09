'''
    File info:
    Inverse Kinematics calculations including walking trajectory
'''


# import custom message types
from hexapod_controller.inverse_kinematics_params import *


def body_move(pos_x_input, pos_y_input, pos_z_input, rot_x_input, rot_y_input, rot_z_input, x, id, variant):
    
    # TODO change description, add walking description!
    '''
    DESCRIPTION - function calculating the inverse kinematics of HEXAPOD's body

    INPUTS - desired positions represented with 6 degrees of freedom
    
    OUTPUT - angle for each motor ex. leg_value[1][2] is a tibia angle of the seccond leg
    '''
    leg = id

    # control inputs
    pos_x = pos_x_input
    pos_y = pos_y_input
    pos_z = pos_z_input
    
    rot_x = rot_x_input
    rot_y = rot_y_input
    rot_z = rot_z_input
    
    ## --------------------------------------------- ##
    # BODY IK - STEP 1
   
    # body ik
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
    # LEG IK - STEP 2

    # ?? change elipse parameters => faster movement, a = 30? a = 35?
    # ellipse parameters
    b = 40
    a = 20
    
    
    # if x == 0:
    #     pos_x_leg = 0
    #     pos_y_leg = 0
    #     pos_z_leg = 0
    # else:
    
    # calculate the trajectory using the ellipse function
    # we need the ellipse / circle without the x translation 
    if variant : z = 0 
    else : z = mh.sqrt((b ** 2) - ((x ** 2) * (b ** 2) / (a ** 2)))

    alpha = mh.radians(leg_rot_angle[leg] + leg_rot_angle_offset[leg])
    pos_x_leg = x * mh.cos(alpha)
    pos_y_leg  = x * mh.sin(alpha)
    pos_z_leg  = -z
    
    # leg ik
    new_pos_x[leg] = pos_x + feet_pos_x[leg] + body_ik_x[leg] + pos_x_leg
    new_pos_y[leg] = pos_y + feet_pos_y[leg] + body_ik_y[leg] + pos_y_leg
    new_pos_z[leg] = pos_z + feet_pos_z[leg] + body_ik_z[leg] + pos_z_leg
    coxa_feet_dist[leg] = mh.sqrt(new_pos_x[leg]**2 + new_pos_y[leg]**2)
    ik_sw[leg] = mh.sqrt((coxa_feet_dist[leg] - COXA_LENGTH)**2 + new_pos_z[leg]**2)
    ik_a1[leg] = mh.atan((coxa_feet_dist[leg] - COXA_LENGTH) / new_pos_z[leg])
    ik_a2[leg] = mh.acos((TIBIA_LENGTH**2 - FEMUR_LENGTH**2 - ik_sw[leg]**2) / (-2 * ik_sw[leg] * FEMUR_LENGTH))
    t_angle[leg] = mh.acos((ik_sw[leg]**2 - TIBIA_LENGTH**2 - FEMUR_LENGTH**2) / (-2 * ik_sw[leg] * FEMUR_LENGTH))

    ik_tibia_angle[leg] = 90 - (ik_a1[leg] + ik_a2[leg]) * 180 / mh.pi
    ik_femur_angle[leg] = 90 - (ik_a1[leg] + ik_a2[leg]) * 180 / mh.pi
    ik_coxa_angle[leg] = 90 - mh.atan2(new_pos_x[leg], new_pos_y[leg]) * 180 / mh.pi


    ## --------------------------------------------- ##
    # LEG ANGLES - STEP 3
    
    # leg angles
    coxa_angle[leg] = ik_coxa_angle[leg] + leg_rot_angle[leg]
    femur_angle[leg] = ik_femur_angle[leg]
    tibia_angle[leg] = ik_tibia_angle[leg]

    # servo angles
    coxa_servo_angle[leg] =  coxa_angle_inverse_flag[leg] * coxa_angle[leg] + 150
    femur_servo_angle[leg] = femur_angle_inverse_flag[leg] * femur_angle[leg] + 150
    tibia_servo_angle[leg] = tibia_angle_inverse_flag[leg] * tibia_angle[leg] + 150

    # servo values for Dynamixel motors AX-12A, avalible steps (0 - 1023), min-max angles (0 - 300deg)
    coxa_servo_value[leg] = coxa_servo_angle[leg] / 300 * 1023
    femur_servo_value[leg] = femur_servo_angle[leg] / 300 * 1023
    tibia_servo_value[leg] = tibia_servo_angle[leg] / 300 * 1023

    # save values for return
    leg_values[leg][0] = int(coxa_servo_value[leg])
    leg_values[leg][1] = int(femur_servo_value[leg])
    leg_values[leg][2] = int(tibia_servo_value[leg])

    return leg_values[leg]




def body_ik(id, pos_x_input, pos_y_input, pos_z_input, rot_x_input, rot_y_input, rot_z_input):
    '''
    DESCRIPTION - function calculating the inverse kinematics of HEXAPOD's body

    INPUTS - desired positions represented with 6 degrees of freedom
    
    OUTPUT - angle for each motor ex. leg_value[1][2] is a tibia angle of the seccond leg
    '''
    leg = id

    # control inputs
    pos_x = pos_x_input
    pos_y = pos_y_input
    pos_z = pos_z_input
    
    rot_x = rot_x_input
    rot_y = rot_y_input
    rot_z = rot_z_input
    
    ## --------------------------------------------- ##
    # BODY IK - STEP 1
   
    # body ik
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
    # LEG IK - STEP 2

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


    ## --------------------------------------------- ##
    # LEG ANGLES - STEP 3
    
    # leg angles
    coxa_angle[leg] = ik_coxa_angle[leg] + leg_rot_angle[leg]
    femur_angle[leg] = ik_femur_angle[leg]
    tibia_angle[leg] = ik_tibia_angle[leg]

    # servo angles
    coxa_servo_angle[leg] =  coxa_angle_inverse_flag[leg] * coxa_angle[leg] + 150
    femur_servo_angle[leg] = femur_angle_inverse_flag[leg] * femur_angle[leg] + 150
    tibia_servo_angle[leg] = tibia_angle_inverse_flag[leg] * tibia_angle[leg] + 150

    # servo values for Dynamixel motors AX-12A, avalible steps (0 - 1023), min-max angles (0 - 300deg)
    coxa_servo_value[leg] = coxa_servo_angle[leg] / 300 * 1023
    femur_servo_value[leg] = femur_servo_angle[leg] / 300 * 1023
    tibia_servo_value[leg] = tibia_servo_angle[leg] / 300 * 1023

    # save values for return
    leg_values[leg][0] = int(coxa_servo_value[leg])
    leg_values[leg][1] = int(femur_servo_value[leg])
    leg_values[leg][2] = int(tibia_servo_value[leg])

    return leg_values[leg]