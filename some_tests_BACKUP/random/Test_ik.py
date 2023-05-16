#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
# Copyright 2017 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

# Author: Ryu Woon Jung (Leon)

#
# *********     Read and Write Example      *********
#
#
# Available DXL model on this example : All models using Protocol 1.0
# This example is tested with a DXL MX-28, and an USB2DYNAMIXEL
# Be sure that DXL MX properties are already set as %% ID : 1 / Baudnum : 34 (Baudrate : 57600)
#

import os
import Leg_IK
from dynamixel_sdk import *  # Uses Dynamixel SDK library


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


# Control table address
ADDR_MX_TORQUE_ENABLE = 24  # Control table address is different in Dynamixel model
ADDR_MX_GOAL_POSITION = 30
ADDR_MX_PRESENT_POSITION = 36

# Protocol version
PROTOCOL_VERSION = 1.0  # See which protocol version is used in the Dynamixel

# Default setting
# DXL_ID                      = 1                 # Dynamixel ID : 1
DXL_ID = 1
DXL_ID1 = 2
DXL_ID2 = 3
# BAUDRATE                    = 57600             # Dynamixel default baudrate : 57600
BAUDRATE = 9600
DEVICENAME = "/dev/ttyUSB1"  # Check which port is being used on your controller
# DEVICENAME                  = '/dev/ttyAMA0'    # Check which port is being used on your controller
# ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE = 1  # Value for enabling the torque
TORQUE_DISABLE = 0  # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE = 500  # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE = 525  # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL_MOVING_STATUS_THRESHOLD = 10  # Dynamixel moving status threshold

index = 0
dxl_goal_position = [
    DXL_MINIMUM_POSITION_VALUE,
    DXL_MAXIMUM_POSITION_VALUE,
]  # Goal position

portHandler = PortHandler(DEVICENAME)
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

# Enable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE
)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")

# INVERSE KINEMATICS TEST
angles_leg1 = Leg_IK.IK_leg([18, 12, 5], 6)
print(
    f"Leg = {1}, theta1 = {angles_leg1[0]}, theta2 = {angles_leg1[1]}, theta3 = {angles_leg1[2]}"
)

while 1:
    print("Press any key to continue! (or press ESC to quit!)")
    if getch() == chr(0x1B):
        break
    else:
        while 1:
            print("Press any key to continue! (or press ESC to quit!)")
            if getch() == chr(0x1B):
                break

            # Write goal position
            dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
                portHandler, DXL_ID, ADDR_MX_GOAL_POSITION, angles_leg1[0]
            )
            dxl_comm_result1, dxl_error1 = packetHandler.write2ByteTxRx(
                portHandler, DXL_ID1, ADDR_MX_GOAL_POSITION, angles_leg1[1]
            )
            dxl_comm_result2, dxl_error2 = packetHandler.write2ByteTxRx(
                portHandler, DXL_ID2, ADDR_MX_GOAL_POSITION, angles_leg1[2]
            )
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % packetHandler.getRxPacketError(dxl_error))

# while 1:
#     # Read present position
#     dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(
#         portHandler, DXL_ID, ADDR_MX_PRESENT_POSITION
#     )
#     if dxl_comm_result != COMM_SUCCESS:
#         print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
#     elif dxl_error != 0:
#         print("%s" % packetHandler.getRxPacketError(dxl_error))

#     print(
#         "[ID:%03d] GoalPos:%03d  PresPos:%03d"
#         % (DXL_ID, dxl_goal_position[index], dxl_present_position)
#     )

#     if (
#         not abs(dxl_goal_position[index] - dxl_present_position)
#         > DXL_MOVING_STATUS_THRESHOLD
#     ):
#         break

# Change goal position
# if index == 0:
#     index = 1
# else:
#     index = 0


# Disable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
    portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE
)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Close port
portHandler.closePort()
