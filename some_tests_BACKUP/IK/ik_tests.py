from com_settings import *
from inverse_kinematics import body_ik

sleep_time = 0.01
leg_values = body_ik(0, 0, -25, 0, 0, 0)

# should be ??? idk yet
print(leg_values)

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

DXL_ID = [1,2,3,4,5,6,7,8,9,16,17,18,13,14,15,10,11,12]
# print(type(DXL_ID[0]))



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
    portHandler, DXL_ID[0], ADDR_MX_GOAL_POSITION, leg_values[0][0]
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[1], ADDR_MX_GOAL_POSITION, leg_values[0][1]
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[2], ADDR_MX_GOAL_POSITION, leg_values[0][2]
)
time.sleep(sleep_time)

# Leg 2
# ------------------------------------------------------------
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[3], ADDR_MX_GOAL_POSITION, leg_values[1][0]
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[4], ADDR_MX_GOAL_POSITION, leg_values[1][1]
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[5], ADDR_MX_GOAL_POSITION, leg_values[1][2]
)
time.sleep(sleep_time)

# Leg 3
# ------------------------------------------------------------
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[6], ADDR_MX_GOAL_POSITION, leg_values[2][0]
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[7], ADDR_MX_GOAL_POSITION, leg_values[2][1]
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[8], ADDR_MX_GOAL_POSITION, leg_values[2][2]
)
time.sleep(sleep_time)

# Leg 4
# ------------------------------------------------------------
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[9], ADDR_MX_GOAL_POSITION, leg_values[3][0]
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[10], ADDR_MX_GOAL_POSITION, leg_values[3][1]
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[11], ADDR_MX_GOAL_POSITION, leg_values[3][2]
)
time.sleep(sleep_time)

# Leg 5
# ------------------------------------------------------------
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[12], ADDR_MX_GOAL_POSITION, leg_values[4][0]
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[13], ADDR_MX_GOAL_POSITION, leg_values[4][1]
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[14], ADDR_MX_GOAL_POSITION, leg_values[4][2]
)
time.sleep(sleep_time)

# Leg 6
# ------------------------------------------------------------
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[15], ADDR_MX_GOAL_POSITION, leg_values[5][0]
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[16], ADDR_MX_GOAL_POSITION, leg_values[5][1]
)
time.sleep(sleep_time)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
    portHandler, DXL_ID[17], ADDR_MX_GOAL_POSITION, leg_values[5][2]
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
