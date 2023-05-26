from setuptools import setup
import os
from glob import glob

package_name = 'hexapod_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch/'), glob('launch/*launch.[pxy][yma]*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='KKKDevTeam',
    maintainer_email='root@todo.todo',
    description='This package is responsible for controlling our HEXAPOD robot using the DynamixelSDK and ROS2 inside of the custom Docker container',
    license='Free for all',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "body_IK_node = hexapod_controller.body:main",
            "keyboard_node = hexapod_controller.teleop_keyboard_test:main",
            "joystick_node = hexapod_controller.joystick:main",
            "leg_1_node = hexapod_controller.legs:leg1",
            "leg_2_node = hexapod_controller.legs:leg2",
            "leg_3_node = hexapod_controller.legs:leg3",
            "leg_4_node = hexapod_controller.legs:leg4",
            "leg_5_node = hexapod_controller.legs:leg5",
            "leg_6_node = hexapod_controller.legs:leg6"
        ],
    },
)
'''
INSTALLING THE CUSTOM NODE:

body_IK_node => executable name / node name
hexapod_controller => package name
body => file to run without the ".py" extension
main => function from within said file which we want to run
'''
