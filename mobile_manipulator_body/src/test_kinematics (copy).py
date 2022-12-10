#!/usr/bin/env python

import rospy
import numpy as np
from math import pi
from std_msgs.msg import Header
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory
#from forward_kinematics import forward_kinematics
#from inverse_kinematics import inverse_kinematics


class Manipulator():
    def __init__(self):
        rospy.init_node('manipulator')
        rospy.loginfo("Press Ctrl + C to terminate")
        self.rate = rospy.Rate(10)

        ## PLease fill in your code here
        #self.joint_pub = rospy.Publisher("/arm_controller/command", JointState, queue_size=10)
	self.joint_pub = rospy.Publisher("/arm_controller/command", JointTrajectory, queue_size=10)

        # prepare joint message to publish
        #joint_msg = JointState()
	joint_msg = JointTrajectory()
        joint_msg.header = Header()
	print(dir(joint_msg))
        joint_msg.joint_names = ['arm_base_joint', 'shoulder_joint', 'bottom_wrist_joint', 'top_wrist_joint']
	#joint_msg.position = [0.0, 0.0, 0.0, 0.0]
	joint_msg.points.positions = [0.0, 0.0, 0.0, 0.0]
        #joint_msg.position = [-0.1, 0.5, 0.12, 0.3]

        # test cases
        angles = [pi / 6, -pi / 3, -pi / 6]  # joint angle in radian
        pos = [0.02165, 0.01250, 0.29721]
        #position = forward_kinematics(angles)
        #joint_angle = inverse_kinematics(pos)
        #print('Position of end-effector = ', position)
        #print('Joint angles = ', joint_angle)
	
	print("for this project")
	angles = [-0.1, 0.5, 0.12, 0.3]

        while not rospy.is_shutdown():
            joint_msg.header.stamp = rospy.Time.now()
            joint_msg.points.positions = angles
            self.joint_pub.publish(joint_msg)
            self.rate.sleep()

            #print("in in in")
            ###########
            #str = input("please type number:")
            #value = float(str) + 1
            #print("your input is:", value)


if __name__ == '__main__':
    whatever = Manipulator()
