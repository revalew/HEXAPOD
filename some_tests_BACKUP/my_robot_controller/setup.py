from setuptools import setup

package_name = 'my_robot_controller'

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
            # INSTALLING THE CUSTOM NODE:

            # test_node => executable name
            # my_robot_controller => package name
            # my_first_node => file to run
            # main => function from within said file which we want to run
            "test_node = my_robot_controller.my_first_node:main"
        ],
    },
)
