#! /usr/bin/env python

import math
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('omni_pose', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("omni")
omni_pose_pub = rospy.Publisher('/omni_pose', geometry_msgs.msg.Pose, queue_size=10)

print ("Current Joint Values:")
omni_joint=group.get_current_joint_values()
print ("q1 = "+str(round(math.degrees(omni_joint[0]),0)))
print ("q2 = "+str(round(math.degrees(omni_joint[1]),0)))
print ("q3 = "+str(round(math.degrees(omni_joint[2]),0)))
print ("q4 = "+str(round(math.degrees(omni_joint[3]),0)))
print ("q5 = "+str(round(math.degrees(omni_joint[4]),0)))
print ("q6 = "+str(round(math.degrees(omni_joint[5]),0)))

print ("Current Pose:")
omni_pose=group.get_current_pose()
px=round(omni_pose.pose.position.x,1)
py=round(omni_pose.pose.position.y,1)
pz=round(omni_pose.pose.position.z,1)
qx=round(omni_pose.pose.orientation.x,2)
qy=round(omni_pose.pose.orientation.y,2)
qz=round(omni_pose.pose.orientation.z,2)
qw=round(omni_pose.pose.orientation.w,2)
print ("x = "+str(px))
print ("y = "+str(py))
print ("z = "+str(pz))
print ("qx = "+str(qx))
print ("qy = "+str(qy))
print ("qz = "+str(qz))
print ("qw = "+str(qw))
quat=[qx, qy, qz, qw]
(roll, pitch, yaw)=euler_from_quaternion(quat)
print ("roll = "+str(math.degrees(roll)))
print ("pitch = "+str(math.degrees(pitch)))
print ("yaw = "+str(math.degrees(yaw)))
# omni_pose conversions

# omni_pose msg generation and publishing
omni_pose_target = geometry_msgs.msg.Pose()
omni_pose_target.position.x = px
omni_pose_target.position.y = py
omni_pose_target.position.z = pz
omni_pose_target.orientation.x = qx
omni_pose_target.orientation.y = qy
omni_pose_target.orientation.z = qz
omni_pose_target.orientation.w = qw

omni_pose_pub.pub(omni_pose_target)

moveit_commander.roscpp_shutdown()