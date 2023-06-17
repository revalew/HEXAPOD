# QuickStart Guide (EN)

## Hardware requirements

In order to run our application, the following hardware requirements must be met:
- Raspberry Pi 4B (the version we are using has 8GB RAM, but should work on 4GB and even 2GB models) with Ubuntu Server,
- "USB to TTL" converter, which is used to send messages to the servos,
- HEXAPOD platform with Robotis Dynamixel AX-12A motors.

---

## Software required

Install Docker and Git on the Raspberry Pi computer
- Git installation:
    ```bash
    sudo apt-get install git -y
    ```
- Docker installation:
    ```bash
    curl -fsSL https://get.docker.com -o get-docker.sh
    chmod +x get-docker.sh 
    sudo apt-get purge docker-ce docker-ce-cli containerd.io -y
    ./get-docker.sh
    # (pi is the user name)
    sudo usermod -aG docker pi
    sudo systemctl unmask docker
    sudo chmod 666 /var/run/docker.sock
    pip3 -v install docker-compose
    sudo systemctl start docker
    # or sudo reboot
    sudo init 6
    ```

---

## Starting the programme for the first time

Once the required software has been installed, follow the steps below:
- Navigate to the directory of your choice (e.g. `/home/pi/`, where pi is the username)
    ```bash
    cd /home/pi/
    ```
    or create your own in the desired location (e.g. `/root/`),
    ```bash
    mkdir ~/HEXAPOD/
    ```
- Clone the contents of the repository using git
    ```bash
    git clone https://github.com/revalew/HEXAPOD.git
    ```
- Navigate to the **docker** directory in the previously cloned repository
    ```bash
    cd ~/HEXAPOD/docker
    ```
- Ensure that the TTL converter is connected to the USB port and has the address `/dev/ttyUSB0`,
    ```bash
    dmesg | grep tty
    ```
    if the converter has a different address, change it to the appropriate one in the *docker-compose.yml* file in the *devices* section.
- Create docker image according to the instructions of the *dockerfile*
    ```bash
    docker build -t ros2 .
    ```
    *ros2* is the name of our container.
- Start our new container with the settings contained in *docker-compose.yml*
    ```bash
    docker-compose up -d
    ```
- Launch an interactive session for a running container
    ```bash
    docker exec -it docker_ros2_1 bash
    ```
    if there is a name error (docker_ros2_1 does not match), check the container name.
    ```bash
    docker ps
    ```
- Navigate to the *hexapod_controller* directory in the cloned repository if the container does not automatically start there.
    ```bash
    cd ~/HEXAPOD/hexapod_controller
    ```
- Compile the program into an executable version via the ROS2 environment
    ```bash
    colcon build
    ```
- Ensure that all sources are up to date (all dependent sources were added to the .bashrc file during docker image creation - *dockerfile* starting at line 45)
    ```bash
    source ~/.bashrc
    ```
- Start the robot's main module
    ```bash
    ros2 launch hexapod_controller hexapod.launch.py
    ```
- Start the keyboard control module in a new terminal (additional ssh session, split terminal using VSCode), in which you should also connect to an active docker session
    ```bash
    docker exec -it docker_ros2_1 bash
    ```
    ```bash
    ros2 run hexapod_controller keyboard_node
    ```
When you have finished playing with the robot, you can close the application in both terminals (each separately) using the "Ctrl + C" shortcut.

---

## Shutting down the programme

When you have finished playing with the robot, you can close the application in both terminals (each separately) using the "Ctrl + C" shortcut.
Once this is done, we can exit the container,
```bash
exit
```
and then we can stop the active image.
```bash
docker stop docker_ros2_1
```
Once the image has been stopped, we can safely switch off the Raspberry.
```bash
sudo shutdown now
```
Once the green LED is off (it flashes momentarily when switched off), which indicates active write to the SD card, we can disconnect the power cable.

---

## Subsequent launches

Once we have built the container and compiled the programme, we can run it much faster:
- Ensure that the TTL converter is connected to the USB port and has the address `/dev/ttyUSB0`,
    ```bash
    dmesg | grep tty
    ```
    if the converter has a different address, change it to the appropriate one in the *docker-compose.yml* file in the *devices* section.
- Navigate to the **docker** directory in the repository
    ```bash
    cd ~/HEXAPOD/docker
    ```
- Start our container with the settings contained in *docker-compose.yml*.
    ```bash
    docker-compose up -d
    ```
- Launch an interactive session for a running container
    ```bash
    docker exec -it docker_ros2_1 bash
    ```
- Start the robot's main module
    ```bash
    ros2 launch hexapod_controller hexapod.launch.py
    ```
- Start the keyboard control module in a new terminal (additional ssh session, split terminal using VSCode), in which you should also connect to an active docker session
    ```bash
    docker exec -it docker_ros2_1 bash
    ```
    ```bash
    ros2 run hexapod_controller keyboard_node
    ```

---

## Troubleshooting

---

**Q:** I changed the converter and the programme stopped working - now what?

**A:** Should a change to the TTL converter port be required or happen spontaneously, the number it has been given should be checked afterwards.
```bash
dmesg | grep tty
```
Once the number has been determined, change it in the settings (in the *docker-compose.yml* file) and restart the container. Here, however, it may turn out that our program does not work, despite the container running. In this case, use the file with the appropriate name "whyDoIhaveToDoThis.txt", located in the `docker/` directory, and copy its contents. Paste the copied content in the terminal window (in the container) and press "Enter".

---

**Q:** Calling the `colcon build` command results in errors and the application does not work

**A:** Remove the installation directories
```bash
rm -rf ~/HEXAPOD/hexapod_controller/build ~/HEXAPOD/hexapod_controller/install ~/HEXAPOD/hexapod_controller/log
```
and call the command again
```bash
colcon build
```