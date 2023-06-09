def leg_ik(x, id, variant):    
    leg = id
    
    # ellipse parameters
    b = 40
    a = 20
    
    # calculate the trajectory using the ellipse function
    # we need the ellipse / circle without the x translation
    if variant : z = 0 
    else : z = mh.sqrt((b ** 2) - ((x ** 2) * (b ** 2) / (a ** 2)))

    alpha = mh.radians(leg_rot_angle[leg] + leg_rot_angle_offset[leg])
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