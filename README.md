# UCR-EE283-2022-Fall-Analytical-Project
UCR EE283 2022 Fall Analytical Project

Author: 1 - Xiaoao Song  2- Rohit Lal 

## Description
We present a 4 DOF pesticide spraying robot structure. The goal of this robot is to spray pesticides in a nursery where there are shrubs and trees of variable sizes. For maximum spraying efficiency, our robot arm should spray all around the plant leaves which might be at different heights. To tackle this problem we propose a RPRR robot with a spraying nozzle attached to the end effector. For practical purposes, we took realistic link lengths and masses for kinematics and statics calculation.


****Robot arm conﬁguration****
![testapriltagdetector](https://github.com/lineojcd/UCR-EE283-2022-Fall-Analytical-Project/blob/main/img/config.png)


## Demo
* Click on the image below to display the video on youtube
<a href="https://www.youtube.com/watch?v=Z8zErxgSJNk" target="_blank"><img src="https://github.com/lineojcd/UCR-EE283-2022-Fall-Analytical-Project/blob/main/img/simulation.png" 
alt="IMAGE ALT TEXT HERE" width="1299" height="600"  /></a>

## Install dependencies
Our code works on Ubuntu 16 + Ros kinetic + python 3.6. Except for that, the below packages are also needed(type the commands in terminal):

```sudo apt-get install ros-kinetic-ros-control```

```sudo apt-get install ros-kinetic-ros-controllers```

```sudo apt-get install ros-kinetic-gazebo-ros-control```

## How to install this repository
* move the whole folder "**mobile_manipulator_body**" to your catkin workspace under **src** folder
* type ****catkin_make**** to build the package, or use the command:
```catkin_make --only-pkg-with-deps mobile_manipulator_body```
* make sure you install other needed dependency packages

## Test the Robot Arm in Rviz
```roscd mobile_manipulator_body/urdf/```

```roslaunch urdf_tutorial display.launch model:=robot_arm.urdf```

Change the Fixed Frame to **world**. Next, you can move the arm using the sliders.

Here are the active ROS topics. ```rostopic list```
![rostopic_rivz](https://github.com/lineojcd/UCR-EE283-2022-Fall-Analytical-Project/blob/main/img/rostopic_rivz.png)


## Launch the Robot Arm in Gazebo
Open a new terminal window, and go to the package then launch file.

```roscd mobile_manipulator_body/launch/```

```roslaunch mobile_manipulator_body arm_gazebo_control.launch```

Open another terminal window, then go to the folder **~/catkin_ws/src/mobile_nanipulator_body/src**, and run the command below:

```python test_kinematics.py```

Here are the active ROS topics. ```rostopic list```
![rostopic_gazebo](https://github.com/lineojcd/UCR-EE283-2022-Fall-Analytical-Project/blob/main/img/rostopic_gazebo.png)

****Quick approach (alternative)****
Instead of running the python script, one can also type this command to move the robot arm and see the result quickly:

```rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["arm_base_joint","shoulder_joint", "bottom_wrist_joint", "top_wrist_joint"], points: [{positions: [-0.1, 0.5, 0.02, 0], time_from_start: [1,0]}]}' -1```

Or type the below command to bring the robot back to the home position.

```rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["arm_base_joint","shoulder_joint", "bottom_wrist_joint", "top_wrist_joint"], points: [{positions: [0, 0, 0, 0], time_from_start: [1,0]}]}' -1```

## Future work
* Add joint limits in Gazebo simulation 
* Attach this robot arm onto a mobile robot base
 
