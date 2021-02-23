#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("manipulator")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

pose_target = geometry_msgs.msg.Pose()
pose_target.position.x = 0.5
pose_target.position.y = 0
pose_target.position.z = 0.9
pose_target.orientation.x = 0.0
pose_target.orientation.y = 0.0
pose_target.orientation.z = 0.0
pose_target.orientation.w = 1.0
group.set_pose_target(pose_target)

plan1 = group.plan()

rospy.sleep(5)
group.go(wait=True)
rospy.sleep(5)
print ("Current Joint Values:")
print (group.get_current_joint_values())
print ("Current Pose:")
print (group.get_current_pose())

moveit_commander.roscpp_shutdown()