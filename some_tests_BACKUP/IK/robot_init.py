from some_tests_BACKUP.IK.com_settings import *

def robot_initialization(portHandler, packetHandler):  
    # THIS FUNCTION REQUIRE OPENED PORT
    
    # ENABLE =================
    for i in range(1, 19):
        DXL_ID = i
        # Enable Dynamixel Torque
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(
            portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE
        )
        time.sleep(0.05)
        
    # Write goal position
    # Leg 1
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
        portHandler, , ADDR_MX_GOAL_POSITION, dxl_goal_position[index]
    )
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
        portHandler, DXL_ID, ADDR_MX_GOAL_POSITION, dxl_goal_position[index]
    )
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
        portHandler, DXL_ID, ADDR_MX_GOAL_POSITION, dxl_goal_position[index]
    )
        
    