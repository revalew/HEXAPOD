# MESSAGE TO COMMUNICATE BETWEEN THE KEYBOARD AND BODY TO CALCLATE THE IK

# INITIALIZE ALL OF THE VALUES WITH 0 - STARTING POSSITION
int16[6] position_of_the_body [0, 0, 0, 0, 0, 0]
int16 move_direction 0

# position_of_the_body:
#     0: transX
#     1: transY
#     2: transZ
#     3: rotX
#     4: rotY
#     5: rotZ

# move_direction
#     1: forward
#    -1: backward
#     0: STOP