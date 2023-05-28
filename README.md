# HEXAPOD Robot 🤖🕷
<p align='center'>
<img src="./img/hexapod.png" width="375" height="260" />
<img src="./img/hexapod_walk.gif" width="375" height="260" />
</p>

## Table of Contents
* [About](https://github.com/revalew/HEXAPOD/tree/master#about)
* [Progress report](https://github.com/revalew/HEXAPOD/edit/master/README.md#progress-report)
  * [First success](https://github.com/revalew/HEXAPOD/tree/master#first-success)
  * [Successful connection](https://github.com/revalew/HEXAPOD/tree/master#successful-connection)
  * [First Stand up](https://github.com/revalew/HEXAPOD/tree/master#first-stand-up)
  * [Controlling all of the servos w/ Inverse Kinematics](https://github.com/revalew/HEXAPOD/tree/master#controlling-all-of-the-servos-w-inverse-kinematics)
  * [First walk](https://github.com/revalew/HEXAPOD/tree/master#first-walk)
* [Issues & plans](https://github.com/revalew/HEXAPOD/edit/master/README.md#issues--plans)
  * [Current problems](https://github.com/revalew/HEXAPOD/edit/master/README.md#current-problems)
  * [Future improvements and plans of development](https://github.com/revalew/HEXAPOD/edit/master/README.md#future-improvements-and-plans-of-development)
<!--   * []() -->
<!--   * []() -->

## About
This is the repository of the academic project which my friends and I are developing. By any means is it perfect, but we will work **HARD** to improve the functionality and make it work! 

What we want to achieve:

- Develop a functional control system for the **HEXAPOD** robot,
- Learn more about Raspberry Pi (i.e. HALF-Duplex UART communication),
- Learn about ROS2 software,
- Learn about Docker and contenerized environments,
- Learn about robotics (especially inverse kinematics),
- Learn about OOP programming in python and ROS2,
- Learn how to use Git & GitHub to collaborate.

## Progress report

### First success:
We created a closed loop control system utilizing:
- Publisher node,
- Subscriber node,
- ROS2 service,
- Turtlesim demo.

<p align='center'>
<img src="./img/turtle.png" width="375" height="260" />
</p>

----

### Successful connection:
We managed to connect the servos and made sure that all 18 of them were working! 🥳

<p align='center'>
<img src="./img/first_move.gif" width="375" height="260" />
</p>

----

### First Stand up:
After few attempts HEXAPOD can finaly stand up easily! Still a lot of work to do, but we are ready to migrate the prototype Python scripts to ROS2 to control all of the servos simultaneously.

<p align='center'>
<img src="./img/hexapod_standup.gif" width="375" height="260" />
</p>

----

### Controlling all of the servos w/ Inverse Kinematics:
Many hours and iterations later we finally managed to use the ROS2 capabilities to move every leg simultaneously! To achieve this we used:
- improved code structure - we moved every leg into one file and made separate functions for each leg,
- custom interface, which is basically an array of positions for the servos,
- different packet structure for controlling the servos - we used a Dynamixel's class called "GroupSyncWrite" to minimize the number of the messages sent (just 6 now!),
- launch file, which spawns a separate process for each of the legs and for the body, allowing us to execute them at the same time.

<p align='center'>
<img src="./img/hexapod_synchro_test.gif" width="375" height="260" />
<span>&ensp;</span>
<img src="./img/hexapod_pushups.gif" width="375" height="260" />
<br>
<img src="./img/custom_interface.png" height="105" />
</p>

----

### First walk:
After a while, we implemented the leg trajectory calculation using the inverse kinematics of the leg and succesfully added a gait pattern. For now, we use only one walking pattern, but we may need more in the future, so we prepared the code's architecture for this scenario. Right now, we want to improve the speed of UART communication to move faster or change the ROS publisher / subscriber to services.

Summary:
- implemented leg trajectory and gait patterns,
- added custom messages, e.g. controll_status to monitor the status of the robot in the future,
- changed the code's architecture.

<p align='center'>
<img src="./img/hexapod_walk.gif" width="375" height="260" />
<img src="./img/hexapod_tripod.gif" width="375" height="260" />
</p>


## Issues & plans

### Current problems:
- Communication using half-duplex UART is too slow for 18 axes to work as fast as we would like to,
- Feet of the robot are really smooth and slippery so there is no friction when walking, which causes the robot to slide all over the place.

### Future improvements and plans of development:
- changing mechanical parts, e.g. 3D printed less slippery feet,
- teleoperation using keyboard or Xbox controller,
- changing the pitch and roll of the body while walking,
- turning while standing still,
- turning while walking,
- implementation of the IMU sensor and body roll pitch compensation,
- code optimization,
- faster communication,
- environment scanning using LIDAR - room mapping.
