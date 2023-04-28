import math as mh
"""
LEG IK - STEP 5

This is the 5th step of the Inverse Kinematics
"""
# LEG 1
new_pos_x_1 = pos_x + feet_pos_x_1 + body_ik_x_1
new_pos_y_1 = pos_y + feet_pos_y_1 + body_ik_y_1
new_pos_z_1 = pos_z + feet_pos_z_1 + body_ik_z_1
coxa_feet_dist_1 = mh.sqrt(new_pos_x_1**2 + new_pos_y_1**2)
ik_sw_1 = mh.sqrt((coxa_feet_dist_1 - COXA_LENGTH)**2 + new_pos_z_1**2)
ik_a1_1 = mh.atan((coxa_feet_dist_1 - COXA_LENGTH) / new_pos_z_1)
ik_a2_1 = mh.acos((TIBIA_LENGTH**2 - FEMUR_LENGTH**2 - ik_sw_1**2) / (-2 * ik_sw_1 * FEMUR_LENGTH))
t_angle_1 = mh.acos((ik_sw_1**2 - TIBIA_LENGTH**2 - FEMUR_LENGTH**2) / (-2 * ik_sw_1 * FEMUR_LENGTH))
ik_tibia_angle_1 = 90 - (ik_a1_1 + ik_a2_1) * 180 / mh.pi
ik_femur_angle_1 = 90 - (ik_a1_1 + ik_a2_1) * 180 / mh.pi
ik_coxa_angle_1 = 90 - mh.atan2(new_pos_x_1, new_pos_y_1) * 180 / mh.pi

# LEG 2
new_pos_x_2 = pos_x + feet_pos_x_2 + body_ik_x_2
new_pos_y_2 = pos_y + feet_pos_y_2 + body_ik_y_2
new_pos_z_2 = pos_z + feet_pos_z_2 + body_ik_z_2
coxa_feet_dist_2 = mh.sqrt(new_pos_x_2**2 + new_pos_y_2**2)
ik_sw_2 = mh.sqrt((coxa_feet_dist_2 - COXA_LENGTH)**2 + new_pos_z_2**2)
ik_a1_2 = mh.atan((coxa_feet_dist_2 - COXA_LENGTH) / new_pos_z_2)
ik_a2_2 = mh.acos((TIBIA_LENGTH**2 - FEMUR_LENGTH**2 - ik_sw_2**2) / (-2 * ik_sw_2 * FEMUR_LENGTH))
t_angle_2 = mh.acos((ik_sw_2**2 - TIBIA_LENGTH**2 - FEMUR_LENGTH**2) / (-2 * ik_sw_2 * FEMUR_LENGTH))
ik_tibia_angle_2 = 90 - (ik_a1_2 + ik_a2_2) * 180 / mh.pi
ik_femur_angle_2 = 90 - (ik_a1_2 + ik_a2_2) * 180 / mh.pi
ik_coxa_angle_2= 90 - mh.atan2(new_pos_x_2, new_pos_y_2) * 180 / mh.pi

# LEG 3
new_pos_x_3 = pos_x + feet_pos_x_3 + body_ik_x_3
new_pos_y_3 = pos_y + feet_pos_y_3 + body_ik_y_3
new_pos_z_3 = pos_z + feet_pos_z_3 + body_ik_z_3
coxa_feet_dist_3 = mh.sqrt(new_pos_x_3**2 + new_pos_y_3**2)
ik_sw_3 = mh.sqrt((coxa_feet_dist_3 - COXA_LENGTH)**2 + new_pos_z_3**2)
ik_a1_3 = mh.atan((coxa_feet_dist_3 - COXA_LENGTH) / new_pos_z_3)
ik_a2_3 = mh.acos((TIBIA_LENGTH**2 - FEMUR_LENGTH**2 - ik_sw_3**2) / (-2 * ik_sw_3 * FEMUR_LENGTH))
t_angle_3 = mh.acos((ik_sw_3**2 - TIBIA_LENGTH**2 - FEMUR_LENGTH**2) / (-2 * ik_sw_3 * FEMUR_LENGTH))
ik_tibia_angle_3 = 90 - (ik_a1_3 + ik_a2_3) * 180 / mh.pi
ik_femur_angle_3 = 90 - (ik_a1_3 + ik_a2_3) * 180 / mh.pi
ik_coxa_angle_3 = 90 - mh.atan2(new_pos_x_3, new_pos_y_3) * 180 / mh.pi

# LEG 4
new_pos_x_4 = pos_x + feet_pos_x_4 + body_ik_x_4
new_pos_y_4 = pos_y + feet_pos_y_4 + body_ik_y_4
new_pos_z_4 = pos_z + feet_pos_z_4 + body_ik_z_4
coxa_feet_dist_4 = mh.sqrt(new_pos_x_4**2 + new_pos_y_4**2)
ik_sw_4 = mh.sqrt((coxa_feet_dist_4 - COXA_LENGTH)**2 + new_pos_z_4**2)
ik_a1_4 = mh.atan((coxa_feet_dist_4 - COXA_LENGTH) / new_pos_z_4)
ik_a2_4 = mh.acos((TIBIA_LENGTH**2 - FEMUR_LENGTH**2 - ik_sw_4**2) / (-2 * ik_sw_4 * FEMUR_LENGTH))
t_angle_4 = mh.acos((ik_sw_4**2 - TIBIA_LENGTH**2 - FEMUR_LENGTH**2) / (-2 * ik_sw_4 * FEMUR_LENGTH))
ik_tibia_angle_4 = 90 - (ik_a1_4 + ik_a2_4) * 180 / mh.pi
ik_femur_angle_4 = 90 - (ik_a1_4 + ik_a2_4) * 180 / mh.pi
ik_coxa_angle_4 = 90 - mh.atan2(new_pos_x_4, new_pos_y_4) * 180 / mh.pi

# LEG 5
new_pos_x_5 = pos_x + feet_pos_x_5 + body_ik_x_5
new_pos_y_5 = pos_y + feet_pos_y_5 + body_ik_y_5
new_pos_z_5 = pos_z + feet_pos_z_5 + body_ik_z_5
coxa_feet_dist_5 = mh.sqrt(new_pos_x_5**2 + new_pos_y_5**2)
ik_sw_5 = mh.sqrt((coxa_feet_dist_5 - COXA_LENGTH)**2 + new_pos_z_5**2)
ik_a1_5 = mh.atan((coxa_feet_dist_5 - COXA_LENGTH) / new_pos_z_5)
ik_a2_5 = mh.acos((TIBIA_LENGTH**2 - FEMUR_LENGTH**2 - ik_sw_5**2) / (-2 * ik_sw_5 * FEMUR_LENGTH))
t_angle_5 = mh.acos((ik_sw_5**2 - TIBIA_LENGTH**2 - FEMUR_LENGTH**2) / (-2 * ik_sw_5 * FEMUR_LENGTH))
ik_tibia_angle_5 = 90 - (ik_a1_5 + ik_a2_5) * 180 / mh.pi
ik_femur_angle_5 = 90 - (ik_a1_5 + ik_a2_5) * 180 / mh.pi
ik_coxa_angle_5 = 90 - mh.atan2(new_pos_x_5, new_pos_y_5) * 180 / mh.pi

# LEG 6
new_pos_x_6 = pos_x + feet_pos_x_6 + body_ik_x_6
new_pos_y_6 = pos_y + feet_pos_y_6 + body_ik_y_6
new_pos_z_6 = pos_z + feet_pos_z_6 + body_ik_z_6
coxa_feet_dist_6 = mh.sqrt(new_pos_x_6**2 + new_pos_y_6**2)
ik_sw_6 = mh.sqrt((coxa_feet_dist_6 - COXA_LENGTH)**2 + new_pos_z_6**2)
ik_a1_6 = mh.atan((coxa_feet_dist_6 - COXA_LENGTH) / new_pos_z_6)
ik_a2_6 = mh.acos((TIBIA_LENGTH**2 - FEMUR_LENGTH**2 - ik_sw_6**2) / (-2 * ik_sw_6 * FEMUR_LENGTH))
t_angle_6 = mh.acos((ik_sw_6**2 - TIBIA_LENGTH**2 - FEMUR_LENGTH**2) / (-2 * ik_sw_6 * FEMUR_LENGTH))
ik_tibia_angle_6 = 90 - (ik_a1_6 + ik_a2_6) * 180 / mh.pi
ik_femur_angle_6 = 90 - (ik_a1_6 + ik_a2_6) * 180 / mh.pi
ik_coxa_angle_6 = 90 - mh.atan2(new_pos_x_6, new_pos_y_6) * 180 / mh.pi
