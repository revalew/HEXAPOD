#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import time

if os.name == "nt":
    import msvcrt

    def getch():
        return msvcrt.getch().decode()

else:
    import sys, tty, termios

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


from dynamixel_sdk import *  # Uses Dynamixel SDK library

# Control table address
ADDR_MX_TORQUE_ENABLE = 24  # Control table address is different in Dynamixel model
ADDR_MX_GOAL_POSITION = 30
ADDR_MX_PRESENT_POSITION = 36

# Protocol version
PROTOCOL_VERSION = 1.0  # See which protocol version is used in the Dynamixel

# Default setting
BAUDRATE = 9600
DEVICENAME = "/dev/ttyUSB1"  # Check which port is being used on your controller

TORQUE_ENABLE = 1  # Value for enabling the torque
TORQUE_DISABLE = 0  # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE = 500  # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE = 550  # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL_MOVING_STATUS_THRESHOLD = 10  # Dynamixel moving status threshold

index = 0
dxl_goal_position = [
    DXL_MINIMUM_POSITION_VALUE,
    DXL_MAXIMUM_POSITION_VALUE,
]  # Goal position


# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)

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
