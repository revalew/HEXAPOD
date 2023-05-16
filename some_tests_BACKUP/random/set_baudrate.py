#!/usr/bin/env python3

from dynamixel_sdk import * 


# from dynamixel_sdk import *                 # Uses Dynamixel SDK library

# Control table address
ADDR_MX_BAUDRATE            = 4                 # Control table address is different in Dynamixel model

# Protocol version
PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL_ID                      = 11                 # Dynamixel ID : 1
BAUDRATE                    = 115200             # Dynamixel default baudrate : 57600
DEVICENAME                  = '/dev/ttyUSB1'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

FACTORYRST_DEFAULTBAUDRATE  = 115200             # Dynamixel baudrate set by factoryreset
NEW_BAUDNUM                 = 1                 # New baudnum to recover Dynamixel baudrate as it was
OPERATION_MODE              = 0x00              # Mode is unavailable in Protocol 1.0 Reset

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

# Read Dynamixel baudnum
dxl_baudnum_read, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL_ID, ADDR_MX_BAUDRATE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("[ID:%03d] DXL baudnum is now : %d" % (DXL_ID, dxl_baudnum_read))

# Write new baudnum
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_BAUDRATE, NEW_BAUDNUM)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("[ID:%03d] Set Dynamixel baudnum to : %d" % (DXL_ID, NEW_BAUDNUM))

# Set port baudrate to BAUDRATE
if portHandler.setBaudRate(FACTORYRST_DEFAULTBAUDRATE):
    print("Succeeded to change the controller baudrate to : %d" % FACTORYRST_DEFAULTBAUDRATE)
else:
    print("Failed to change the controller baudrate")
    print("Press any key to terminate...")
    quit()


# Read Dynamixel baudnum
dxl_baudnum_read, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL_ID, ADDR_MX_BAUDRATE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("[ID:%03d] Dynamixel Baudnum is now : %d" % (DXL_ID, dxl_baudnum_read))