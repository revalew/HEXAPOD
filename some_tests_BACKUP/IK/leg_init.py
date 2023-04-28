from some_tests_BACKUP.IK.com_settings import *

def leg_initialization(leg_num):
    
    leg_id = (leg_num - 1 ) * 3
    
    # Leg 1
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
        portHandler, leg_id + 1, ADDR_MX_GOAL_POSITION, dxl_goal_position[index]
    )
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
        portHandler, leg_id + 2, ADDR_MX_GOAL_POSITION, dxl_goal_position[index]
    )
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(
        portHandler, leg_id + 3, ADDR_MX_GOAL_POSITION, dxl_goal_position[index]
    )