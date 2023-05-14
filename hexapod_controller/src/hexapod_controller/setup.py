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
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "body_IK_node = hexapod_controller.body:main",
            # "servo_1_node = hexapod_controller.servos:servo1",
            # "servo_2_node = hexapod_controller.servos:servo2",
            # "servo_3_node = hexapod_controller.servos:servo3",
            # "servo_4_node = hexapod_controller.servos:servo4",
            # "servo_5_node = hexapod_controller.servos:servo5",
            # "servo_6_node = hexapod_controller.servos:servo6",
            # "servo_7_node = hexapod_controller.servos:servo7",
            # "servo_8_node = hexapod_controller.servos:servo8",
            # "servo_9_node = hexapod_controller.servos:servo9",
            # "servo_10_node = hexapod_controller.servos:servo10",
            # "servo_11_node = hexapod_controller.servos:servo11",
            # "servo_12_node = hexapod_controller.servos:servo12",
            # "servo_13_node = hexapod_controller.servos:servo13",
            # "servo_14_node = hexapod_controller.servos:servo14",
            # "servo_15_node = hexapod_controller.servos:servo15",
            # "servo_16_node = hexapod_controller.servos:servo16",
            # "servo_17_node = hexapod_controller.servos:servo17",
            # "servo_18_node = hexapod_controller.servos:servo18"
            # "keyboard_node = hexapod_controller.keyboard:main"
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

body_IK_node => executable name
hexapod_controller => package name
body => file to run
main => function from within said file which we want to run
'''
