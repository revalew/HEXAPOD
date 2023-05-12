from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    body = Node(
        package = "hexapod_controller",
        executable = "body_IK_node",
        name = "body_IK_node",
    )
    
    servo_1 = Node(
        package = "hexapod_controller",
        executable = "servo_1_node",
        name = "servo_1_node",
    )
    
    servo_2 = Node(
        package = "hexapod_controller",
        executable = "servo_2_node",
        name = "servo_2_node",
    )
    
    servo_3 = Node(
        package = "hexapod_controller",
        executable = "servo_3_node",
        name = "servo_3_node",
    )
    
    servo_4 = Node(
        package = "hexapod_controller",
        executable = "servo_4_node",
        name = "servo_4_node",
    )
    
    servo_5 = Node(
        package = "hexapod_controller",
        executable = "servo_5_node",
        name = "servo_5_node",
    )
    
    servo_6 = Node(
        package = "hexapod_controller",
        executable = "servo_6_node",
        name = "servo_6_node",
    )
    
    servo_7 = Node(
        package = "hexapod_controller",
        executable = "servo_7_node",
        name = "servo_7_node",
    )
    
    servo_8 = Node(
        package = "hexapod_controller",
        executable = "servo_8_node",
        name = "servo_8_node",
    )
    
    servo_9 = Node(
        package = "hexapod_controller",
        executable = "servo_9_node",
        name = "servo_9_node",
    )
    
    servo_10 = Node(
        package = "hexapod_controller",
        executable = "servo_10_node",
        name = "servo_10_node",
    )
    
    servo_11 = Node(
        package = "hexapod_controller",
        executable = "servo_11_node",
        name = "servo_11_node",
    )
    
    servo_12 = Node(
        package = "hexapod_controller",
        executable = "servo_12_node",
        name = "servo_12_node",
    )
    
    servo_13 = Node(
        package = "hexapod_controller",
        executable = "servo_13_node",
        name = "servo_13_node",
    )
    
    servo_14 = Node(
        package = "hexapod_controller",
        executable = "servo_14_node",
        name = "servo_14_node",
    )
    
    servo_15 = Node(
        package = "hexapod_controller",
        executable = "servo_15_node",
        name = "servo_15_node",
    )
    
    servo_16 = Node(
        package = "hexapod_controller",
        executable = "servo_16_node",
        name = "servo_16_node",
    )
    
    servo_17 = Node(
        package = "hexapod_controller",
        executable = "servo_17_node",
        name = "servo_17_node",
    )
    
    servo_18 = Node(
        package = "hexapod_controller",
        executable = "servo_18_node",
        name = "servo_18_node",
    )
    
    return LaunchDescription([
        body,
        servo_1,
        servo_2,
        servo_3,
        servo_4,
        servo_5,
        servo_6,
        servo_7,
        servo_8,
        servo_9,
        servo_10,
        servo_11,
        servo_12,
        servo_13,
        servo_14,
        servo_15,
        servo_16,
        servo_17,
        servo_18
    ])