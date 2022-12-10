# UCR-EE283-2022-Fall-Analytical-Project
UCR EE283 2022 Fall Analytical Project

Co-author: Rohit Lal 


****Robot arm conﬁguration****
![testapriltagdetector](https://github.com/lineojcd/UCR-EE283-2022-Fall-Analytical-Project/blob/main/img/config.png)


## Demo
Click on the image below to display the video
<a href="https://www.youtube.com/watch?v=Z8zErxgSJNk" target="_blank"><img src="https://github.com/lineojcd/UCR-EE283-2022-Fall-Analytical-Project/blob/main/img/simulation.png" 
alt="IMAGE ALT TEXT HERE" width="1299" height="600"  /></a>

## How to run the code
move the whole folder "mobile_manipulator_body" to your catkin workspace and then type ****catkin_make**** to build the package

## Launch in Rviz
```roscd mobile_manipulator_body/urdf/```

```roslaunch urdf_tutorial display.launch model:=robot_arm.urdf```
## Launch in Gazebo
```roscd mobile_manipulator_body/launch/```

```roslaunch mobile_manipulator_body arm_gazebo_control.launch```

 
