# Overview
autonomous drone...

- Current Features
    - semi
- Future Features
    - Obstacle Avoidance
    - Precision landing 

- Hardware/Sensors
    - Pixhawk Flight Controller
    - Jetson/Raspberry Pi Companion Computer
    - 

# Simulation Setup
- Preqs
    1. Ubuntu Noble 24.04
    2. [ROS 2 Jazzy Jalisco](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html#resources)
    3. [Gazebo Harmonic](https://gazebosim.org/docs/harmonic/ros_installation/)
    4. [Ardupilot SITL](https://medium.com/@sanjana_dev9/how-to-set-up-ardupilot-sitl-with-gazebo-for-drone-simulation-a0d15e19b8e3)
    5. [ardupilot_gazebo plugin](https://medium.com/@sanjana_dev9/how-to-set-up-ardupilot-sitl-with-gazebo-for-drone-simulation-a0d15e19b8e3)
    6. [MAVROS](https://medium.com/@sanjana_dev9/setting-up-mavros-on-raspberry-pi-4b-a6a26b8b987f)

1. Run these 3 commands/programs in seperate terminals
```
gz sim -v4 -r iris_runway.sdf
```
```bash
# ardupilot/Tools/autotest
./sim_vehicle.py -v ArduCopter -f gazebo-iris --model JSON --map --console
```
```bash
ros2 launch mavros apm.launch fcu_url:="udp://:14550@127.0.0.1:14555" gcs_url:="udp://@"
```
2. Now you can excute the MAVROS script (fly.py) 

# IRL Setup
- 
