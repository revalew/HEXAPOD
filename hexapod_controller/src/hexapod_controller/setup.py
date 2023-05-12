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
            "servo_1_node = hexapod_controller.servo_1:main",
            "servo_2_node = hexapod_controller.servo_2:main",
            "servo_3_node = hexapod_controller.servo_3:main",
            "servo_4_node = hexapod_controller.servo_4:main",
            "servo_5_node = hexapod_controller.servo_5:main",
            "servo_6_node = hexapod_controller.servo_6:main",
            "servo_7_node = hexapod_controller.servo_7:main",
            "servo_8_node = hexapod_controller.servo_8:main",
            "servo_9_node = hexapod_controller.servo_9:main",
            "servo_10_node = hexapod_controller.servo_10:main",
            "servo_11_node = hexapod_controller.servo_11:main",
            "servo_12_node = hexapod_controller.servo_12:main",
            "servo_13_node = hexapod_controller.servo_13:main",
            "servo_14_node = hexapod_controller.servo_14:main",
            "servo_15_node = hexapod_controller.servo_15:main",
            "servo_16_node = hexapod_controller.servo_16:main",
            "servo_17_node = hexapod_controller.servo_17:main",
            "servo_18_node = hexapod_controller.servo_18:main"
            # "keyboard_node = hexapod_controller.keyboard:main"
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
