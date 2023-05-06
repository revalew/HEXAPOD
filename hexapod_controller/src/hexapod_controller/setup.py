from setuptools import setup

package_name = 'hexapod_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            "body_IK_node = hexapod_controller.body:main"
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
