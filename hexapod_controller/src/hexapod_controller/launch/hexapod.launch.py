from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    body = Node(
        package = "hexapod_controller",
        executable = "body_IK_node",
        name = "body_IK_node",
    )
    
    leg_1 = Node(
        package = "hexapod_controller",
        executable = "leg_1_node",
        name = "leg_1_node",
    )
    
    leg_2 = Node(
        package = "hexapod_controller",
        executable = "leg_2_node",
        name = "leg_2_node",
    )
    
    leg_3 = Node(
        package = "hexapod_controller",
        executable = "leg_3_node",
        name = "leg_3_node",
    )
    
    leg_4 = Node(
        package = "hexapod_controller",
        executable = "leg_4_node",
        name = "leg_4_node",
    )
    
    leg_5 = Node(
        package = "hexapod_controller",
        executable = "leg_5_node",
        name = "leg_5_node",
    )
    
    leg_6 = Node(
        package = "hexapod_controller",
        executable = "leg_6_node",
        name = "leg_6_node",
    )
    
    return LaunchDescription([
        body,
        leg_1,
        leg_2,
        leg_3,
        leg_4,
        leg_5,
        leg_6
    ])