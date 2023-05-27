import math as mh


## --------------------------------------------- ##
# OTHER PARAMS
LEG_DIRECTION_SWAP = [-1,1,1,1,1,-1] 

## --------------------------------------------- ##
# DIRECT INPUTS - STEP 1
# robot geometry
COXA_LENGTH = 85
FEMUR_LENGTH = 68
TIBIA_LENGTH = 125

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
# body_ik_z = [0,0,0,0,0,0]
body_ik_z = [-20,-20,-20,-20,-20,-20] # changed bcs it look cool!
 
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
leg_rot_angle = [-90, 0 , 90, -270, -180, -90] # FLAGA ZAMIANA NOG!!!!
# leg_rot_angle = [-90, 0 , 90, -90 -180, -270]
leg_rot_angle_offset = [30, 60, -30, 30, -60, -30] # FLAGA ZAMIANA NOG!!!!
# leg_rot_angle_offset = [30, 60, -30, -30, -60, 30]

# specyfic leg angle inverse, if "-1" that means it rotates servo angle in for loop
# you can simply give all ones here, and rotate phisical motor
coxa_angle_inverse_flag = [1, 1, 1, 1, 1, 1]
femur_angle_inverse_flag = [-1, -1, -1, 1, 1, 1]
tibia_angle_inverse_flag = [1, 1, 1, -1, -1, -1]

# return array init
leg_values = [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]]
