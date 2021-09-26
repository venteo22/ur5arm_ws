#! /usr/bin/env python


import sys
from lib_pose import*
from lib_ur5e_python_interface import MoveGroupPythonInterfaceTutorial

import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

ur5e=MoveGroupPythonInterfaceTutorial()
ur5e.go_to_joint_state(0,-pi/3,pi/3,0,0,0)
rospy.sleep(1)
ur5e.go_to_pose_goal(0.6,0,0.2,0,0,0)
rospy.sleep(1)
cartesian_plan,fraction=ur5e.plan_cartesian_path(0.1,0.2,0.3)
ur5e.display_trajectory(cartesian_plan)
ur5e.execute_plan(cartesian_plan)
ur5e_pose=ur5e.move_group.get_current_pose()
pose1=xyzrpy(ur5e_pose)
print ("Cureent Pose: "+ str(pose1))
ur5e_joints=ur5e.move_group.get_current_joints_values()
print ("Current Joint" + str(ur5e_joints))
