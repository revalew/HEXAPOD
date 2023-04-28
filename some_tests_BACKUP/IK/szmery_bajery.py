import math as mh
from com_settings import *
import numpy as np

# def body_ik(pos_x, pos_y, pos_z, rot_x, rot_y, rot_z):

sleep_time = 0.005

# DIRECT INPUTS - STEP 1
# robot geometry
COXA_LENGTH = 85
FEMUR_LENGTH = 68
TIBIA_LENGTH = 125

# control inputs
pos_x = 0
pos_y = 0
pos_z = 0
rot_x = 0
rot_y = 0
rot_z = 0


# PRIMARY GEOMETRIC CALCULATIONS - STEP 2

# body center offset x
BODY_CENTER_OFFSET_X_1 = 70
BODY_CENTER_OFFSET_X_2 = 100
BODY_CENTER_OFFSET_X_3 = 70
BODY_CENTER_OFFSET_X_4 = -70
BODY_CENTER_OFFSET_X_5 = -100
BODY_CENTER_OFFSET_X_6 = -70

# body center offset y
BODY_CENTER_OFFSET_Y_1 = 70
BODY_CENTER_OFFSET_Y_2 = 0
BODY_CENTER_OFFSET_Y_3 = -70
BODY_CENTER_OFFSET_Y_4 = -70
BODY_CENTER_OFFSET_Y_5 = 0
BODY_CENTER_OFFSET_Y_6 = 70


# INITIAL FEET POSITIONS - STEP 3

# leg 1
feet_pos_x_1 = mh.cos(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH)

feet_pos_z_1 = TIBIA_LENGTH
feet_pos_y_1 = mh.sin(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH)

# Leg 2
feet_pos_x_2 = COXA_LENGTH + FEMUR_LENGTH
feet_pos_z_2 = TIBIA_LENGTH
feet_pos_y_2 = 0

# leg 3
feet_pos_x_3 = mh.cos(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH)
feet_pos_z_3 = TIBIA_LENGTH
feet_pos_y_3 = -1 * (mh.sin(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH))

# leg 4
feet_pos_x_4 = -1 * (mh.cos(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH))
feet_pos_z_4 = TIBIA_LENGTH
feet_pos_y_4 = -1 * (mh.sin(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH))

# Leg 5
feet_pos_x_5 = -1 * (COXA_LENGTH + FEMUR_LENGTH)
feet_pos_z_5 = (TIBIA_LENGTH)
feet_pos_y_5 = 0

# leg 6
feet_pos_x_6 = -1 * (mh.cos(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH))
feet_pos_z_6 = TIBIA_LENGTH
feet_pos_y_6 = mh.sin(60 / 180 * mh.pi) * (COXA_LENGTH + FEMUR_LENGTH)

# BODY IK

# leg 1
total_y_1 = feet_pos_y_1 + BODY_CENTER_OFFSET_Y_1 + pos_y
total_x_1 = feet_pos_x_1 + BODY_CENTER_OFFSET_X_1 + pos_x
dist_body_center_feet_1 = mh.sqrt((total_y_1**2) + (total_x_1**2))
angle_body_center_x_1 = (mh.pi / 2) - mh.atan2(total_x_1, total_y_1)
roll_z_1 = mh.tan(rot_y * mh.pi/180) * total_x_1
pitch_z_1 = mh.tan(rot_x * mh.pi/180) * total_y_1

body_ik_x_1 = mh.cos(angle_body_center_x_1 + (rot_z * mh.pi / 180)) * dist_body_center_feet_1 - total_x_1
body_ik_y_1 = (mh.sin(angle_body_center_x_1 + (rot_z * mh.pi / 180))*dist_body_center_feet_1) - total_y_1
body_ik_z_1 = roll_z_1 + pitch_z_1

# leg 2
total_y_2 = feet_pos_y_2 + BODY_CENTER_OFFSET_Y_2 + pos_y
total_x_2 = feet_pos_x_2 + BODY_CENTER_OFFSET_X_2 + pos_x
dist_body_center_feet_2 = mh.sqrt((total_y_2**2) + (total_x_2**2))
angle_body_center_x_2 = (mh.pi / 2) - mh.atan2(total_x_2, total_y_2)
roll_z_2 = mh.tan(rot_y * mh.pi/180) * total_x_2
pitch_z_2 = mh.tan(rot_x * mh.pi/180) * total_y_2

body_ik_x_2 = mh.cos(angle_body_center_x_2 + (rot_z * mh.pi / 180)) * dist_body_center_feet_2 - total_x_2
body_ik_y_2 = (mh.sin(angle_body_center_x_2 + (rot_z * mh.pi / 180))*dist_body_center_feet_2) - total_y_2
body_ik_z_2 = roll_z_2 + pitch_z_2

# leg 3
total_y_3 = feet_pos_y_3 + BODY_CENTER_OFFSET_Y_3 + pos_y
total_x_3 = feet_pos_x_3 + BODY_CENTER_OFFSET_X_3 + pos_x
dist_body_center_feet_3 = mh.sqrt((total_y_3**2) + (total_x_3**2))
angle_body_center_x_3 = (mh.pi / 2) - mh.atan2(total_x_3, total_y_3)
roll_z_3 = mh.tan(rot_y * mh.pi/180) * total_x_3
pitch_z_3 = mh.tan(rot_x * mh.pi/180) * total_y_3

body_ik_x_3 = mh.cos(angle_body_center_x_3 + (rot_z * mh.pi / 180)) * dist_body_center_feet_3 - total_x_3
body_ik_y_3 = (mh.sin(angle_body_center_x_3 + (rot_z * mh.pi / 180))*dist_body_center_feet_3) - total_y_3
body_ik_z_3 = roll_z_3 + pitch_z_3

# leg 4
total_y_4 = feet_pos_y_4 + BODY_CENTER_OFFSET_Y_4 + pos_y
total_x_4 = feet_pos_x_4 + BODY_CENTER_OFFSET_X_4 + pos_x
dist_body_center_feet_4 = mh.sqrt((total_y_4**2) + (total_x_4**2))
angle_body_center_x_4 = (mh.pi / 2) - mh.atan2(total_x_4, total_y_4)
roll_z_4 = mh.tan(rot_y * mh.pi/180) * total_x_4
pitch_z_4 = mh.tan(rot_x * mh.pi/180) * total_y_4

body_ik_x_4 = mh.cos(angle_body_center_x_4 + (rot_z * mh.pi / 180)) * dist_body_center_feet_4 - total_x_4
body_ik_y_4 = (mh.sin(angle_body_center_x_4 + (rot_z * mh.pi / 180))*dist_body_center_feet_4) - total_y_4
body_ik_z_4 = roll_z_4 + pitch_z_4

# leg 5
total_y_5 = feet_pos_y_5 + BODY_CENTER_OFFSET_Y_5 + pos_y
total_x_5 = feet_pos_x_5 + BODY_CENTER_OFFSET_X_5 + pos_x
dist_body_center_feet_5 = mh.sqrt((total_y_5**2) + (total_x_5**2))
angle_body_center_x_5 = (mh.pi / 2) - mh.atan2(total_x_5, total_y_5)
roll_z_5 = mh.tan(rot_y * mh.pi/180) * total_x_5
pitch_z_5 = mh.tan(rot_x * mh.pi/180) * total_y_5

body_ik_x_5 = mh.cos(angle_body_center_x_5 + (rot_z * mh.pi / 180)) * dist_body_center_feet_5 - total_x_5
body_ik_y_5 = (mh.sin(angle_body_center_x_5 + (rot_z * mh.pi / 180))*dist_body_center_feet_5) - total_y_5
body_ik_z_5 = roll_z_5 + pitch_z_5

# leg 6
total_y_6 = feet_pos_y_6 + BODY_CENTER_OFFSET_Y_6 + pos_y
total_x_6 = feet_pos_x_6 + BODY_CENTER_OFFSET_X_6 + pos_x
dist_body_center_feet_6 = mh.sqrt((total_y_6**2) + (total_x_6**2))
angle_body_center_x_6 = (mh.pi / 2) - mh.atan2(total_x_6, total_y_6)
roll_z_6 = mh.tan(rot_y * mh.pi/180) * total_x_6
pitch_z_6 = mh.tan(rot_x * mh.pi/180) * total_y_6

body_ik_x_6 = mh.cos(angle_body_center_x_6 + (rot_z * mh.pi / 180)) * dist_body_center_feet_6 - total_x_6
body_ik_y_6 = (mh.sin(angle_body_center_x_6 + (rot_z * mh.pi / 180))*dist_body_center_feet_6) - total_y_6
body_ik_z_6 = roll_z_6 + pitch_z_6


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


# LEG ANGLES - STEP 6

# LEG ANGLES - STEP 6

# leg 1
coxa_angle_1 = ik_coxa_angle_1 - 90
femur_angle_1 = ik_femur_angle_1
tibia_angle_1 = ik_tibia_angle_1


# SERVO ANGLES

# Leg 1
coxa_servo_angle_1 =  coxa_angle_1 + 150
femur_servo_angle_1 = -1 * femur_angle_1 + 150
tibia_servo_angle_1 = tibia_angle_1 + 150

# Koncowe kąty
coxa_servo_value_1 = coxa_servo_angle_1 / 300 * 1023
femur_servo_value_1 = femur_servo_angle_1 / 300 * 1023
tibia_servo_value_1 = tibia_servo_angle_1 / 300 * 1023

## --------------------------------------------- ##

# leg 2
coxa_angle_2 = ik_coxa_angle_2
femur_angle_2 = ik_femur_angle_2
tibia_angle_2 = ik_tibia_angle_2


# SERVO ANGLES

# Leg 2
coxa_servo_angle_2 = coxa_angle_2 + 150
femur_servo_angle_2 = -1 * femur_angle_2 + 150
tibia_servo_angle_2 = tibia_angle_2 + 150

# Koncowe kąty
coxa_servo_value_2 = coxa_servo_angle_2 / 300 * 1023
femur_servo_value_2 = femur_servo_angle_2 / 300 * 1023
tibia_servo_value_2 = tibia_servo_angle_2 / 300 * 1023

## --------------------------------------------- ##

# leg 3
coxa_angle_3 = ik_coxa_angle_3 + 90
femur_angle_3 = ik_femur_angle_3
tibia_angle_3 = ik_tibia_angle_3


# SERVO ANGLES

# Leg 3
coxa_servo_angle_3 = coxa_angle_3 + 150
femur_servo_angle_3 = -1 * femur_angle_3 + 150
tibia_servo_angle_3 = tibia_angle_3 + 150

# Koncowe kąty
coxa_servo_value_3 = coxa_servo_angle_3 / 300 * 1023
femur_servo_value_3 = femur_servo_angle_3 / 300 * 1023
tibia_servo_value_3 = tibia_servo_angle_3 / 300 * 1023

# --------------------------------------------- ##

# leg 4
coxa_angle_4 = ik_coxa_angle_4 - 210
femur_angle_4 = ik_femur_angle_4
tibia_angle_4 = ik_tibia_angle_4


# SERVO ANGLES

# Leg 4
coxa_servo_angle_4 = coxa_angle_4 + 150
femur_servo_angle_4 = femur_angle_4 + 150
tibia_servo_angle_4 = -1 * tibia_angle_4 + 150

# Koncowe kąty
coxa_servo_value_4 = coxa_servo_angle_4 / 300 * 1023
femur_servo_value_4 = femur_servo_angle_4 / 300 * 1023
tibia_servo_value_4 = tibia_servo_angle_4 / 300 * 1023

# --------------------------------------------- ##

# leg 5
coxa_angle_5 = ik_coxa_angle_5 -180
femur_angle_5 = ik_femur_angle_5
tibia_angle_5 = ik_tibia_angle_5


# SERVO ANGLES

# Leg 5
coxa_servo_angle_5 = coxa_angle_5 + 150
femur_servo_angle_5 = femur_angle_5 + 150
tibia_servo_angle_5 = -1 * tibia_angle_5 + 150

# Koncowe kąty
coxa_servo_value_5 = coxa_servo_angle_5 / 300 * 1023
femur_servo_value_5 = femur_servo_angle_5 / 300 * 1023
tibia_servo_value_5 = tibia_servo_angle_5 / 300 * 1023

# --------------------------------------------- ##

# leg 6
coxa_angle_6 = ik_coxa_angle_6 - 150
femur_angle_6 = ik_femur_angle_6
tibia_angle_6 = ik_tibia_angle_6


# SERVO ANGLES

# Leg 6
coxa_servo_angle_6 = coxa_angle_6 + 150
femur_servo_angle_6 = femur_angle_6 + 150
tibia_servo_angle_6 = -1 * tibia_angle_6 + 150

# Koncowe kąty
coxa_servo_value_6 = coxa_servo_angle_6 / 300 * 1023
femur_servo_value_6 = femur_servo_angle_6 / 300 * 1023
tibia_servo_value_6 = tibia_servo_angle_6 / 300 * 1023
    
    # return ([(coxa_servo_value_1, femur_servo_value_1, tibia_servo_value_1)])





## TEST ##

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

DXL_ID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
print(type(DXL_ID[0]))



# ENABLE =================
for i in DXL_ID:
    # Enable Dynamixel Torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
        portHandler, i, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE
    )
    time.sleep(0.05)

# Write goal position

# Leg 1
# ------------------------------------------------------------
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[0], ADDR_MX_GOAL_POSITION, int(coxa_servo_value_1)
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[1], ADDR_MX_GOAL_POSITION, int(femur_servo_value_1)
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[2], ADDR_MX_GOAL_POSITION, int(tibia_servo_value_1)
)
time.sleep(sleep_time)

# Leg 2
# ------------------------------------------------------------
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[3], ADDR_MX_GOAL_POSITION, int(coxa_servo_value_2)
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[4], ADDR_MX_GOAL_POSITION, int(femur_servo_value_2)
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[5], ADDR_MX_GOAL_POSITION, int(tibia_servo_value_2)
)
time.sleep(sleep_time)

# Leg 3
# ------------------------------------------------------------
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[6], ADDR_MX_GOAL_POSITION, int(coxa_servo_value_3)
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[7], ADDR_MX_GOAL_POSITION, int(femur_servo_value_3)
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[8], ADDR_MX_GOAL_POSITION, int(tibia_servo_value_3)
)
time.sleep(sleep_time)

# Leg 4
# ------------------------------------------------------------
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[9], ADDR_MX_GOAL_POSITION, int(coxa_servo_value_4)
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[10], ADDR_MX_GOAL_POSITION, int(femur_servo_value_4)
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[11], ADDR_MX_GOAL_POSITION, int(tibia_servo_value_4)
)
time.sleep(sleep_time)

# Leg 5
# ------------------------------------------------------------
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[12], ADDR_MX_GOAL_POSITION, int(coxa_servo_value_5)
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[13], ADDR_MX_GOAL_POSITION, int(femur_servo_value_5)
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[14], ADDR_MX_GOAL_POSITION, int(tibia_servo_value_5)
)
time.sleep(sleep_time)

# Leg 6
# ------------------------------------------------------------
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[15], ADDR_MX_GOAL_POSITION, int(coxa_servo_value_6)
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[16], ADDR_MX_GOAL_POSITION, int(femur_servo_value_6)
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[17], ADDR_MX_GOAL_POSITION, int(tibia_servo_value_6)
)
time.sleep(sleep_time)




# DISABLE =================
# for i in range(1, 19):
#     DXL_ID = i
#     dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
#         portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE
#     )

#     time.sleep(0.05)
# ---------------------------------------------------------------------
# Close port
portHandler.closePort()



