#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from some_tests_BACKUP.IK.com_settings import *

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


# ENABLE =================
for i in range(1, 19):
    DXL_ID = i
    # Enable Dynamixel Torque
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
        portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE
    )
    time.sleep(0.05)

for i in range(1, 19):
    DXL_ID = i

    # Write goal position
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
        portHandler, DXL_ID, ADDR_MX_GOAL_POSITION, dxl_goal_position[index]
    )

    time.sleep(0.1)

    # Read present position
    dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(
        portHandler, DXL_ID, ADDR_MX_PRESENT_POSITION
    )
    print("ID: %03d \t PresPos: %03d" % (DXL_ID, dxl_present_position))

    time.sleep(0.05)


# Change goal position
if index == 0:
    index = 1
else:
    index = 0

while 1:
    print("Press ESC key to continue!")
    if getch() == chr(0x1B):
        break

for i in range(1, 19):
    DXL_ID = i

    # Write goal position
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
        portHandler, DXL_ID, ADDR_MX_GOAL_POSITION, dxl_goal_position[index]
    )

    time.sleep(0.1)

    # Read present position
    dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(
        portHandler, DXL_ID, ADDR_MX_PRESENT_POSITION
    )
    print("ID: %03d \t PresPos: %03d" % (DXL_ID, dxl_present_position))

    time.sleep(0.05)


# DISABLE =================
for i in range(1, 19):
    DXL_ID = i
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
        portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE
    )

    time.sleep(0.05)
# ---------------------------------------------------------------------
# Close port
portHandler.closePort()
