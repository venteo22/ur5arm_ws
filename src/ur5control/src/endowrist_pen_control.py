#! /usr/bin/env python

import math
import numpy as np
from tf.transformations import euler_from_quaternion, quaternion_from_euler, quaternion_matrix
import rospy
from geometry_msgs.msg import Pose, PoseStamped
from std_msgs.msg import Float32MultiArray, Bool


pose_pen=[-0.45,0.55,0.55]
rpw=[0,0,0]
movex=False

def pose_current_callback(data):
    current_pose = PoseStamped()
    arm_x=data.pose.position.x
    #rospy.loginfo("Current pose arm x= %f\n",arm_x)
def pen_orientation_callback(data):
    global rpw
    rpw = Float32MultiArray()
    rpw=data
    rospy.loginfo("Pen orientation rpw= %s\n",rpw)
def pen_position_callback(data):
    global movex
    move_x = Bool()
    move_x=data
    rospy.loginfo("Pen is moveing? %s\n",move_x)
def pen_open_callback(data):
    open = Bool()
    open=data
    rospy.loginfo("Endowrist is opening? %s\n",open)

def control_arm():
    global pose_pen
    pub = rospy.Publisher('/pose_target', Pose, queue_size=10)
    rospy.Subscriber('/pose_current', PoseStamped, pose_current_callback)
    rospy.Subscriber('/pen_orientation', Float32MultiArray, pen_orientation_callback)
    rospy.Subscriber('/pen_position', Bool, pen_position_callback)
    rospy.Subscriber('/pen_open', Bool, pen_open_callback)

    rate = rospy.Rate(10) # 10hz
    pose_target = Pose()
    pose_target.position.x = pose_pen[0]
    pose_target.position.y = pose_pen[1]
    pose_target.position.z = pose_pen[2]
    r=math.radians(rpw[0])
    p=math.radians(rpw[1])
    w=math.radians(rpw[2])
    quat1=quaternion_from_euler(r,p,w)
    endo_frame= quaternion_matrix(quat1)
    pose_target.orientation.x = quat1[0]
    pose_target.orientation.y = quat1[1]
    pose_target.orientation.z = quat1[2]
    pose_target.orientation.w = quat1[3]
    while not rospy.is_shutdown():
        print ("Target Pose arm TCP:")
        rospy.loginfo("Target arm position = %s\n",pose_pen)
        rospy.loginfo("Target Endowrist rpw = %s\n",rpw)

        pub.publish(pose_target)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('endowrist_pen_control', anonymous=True)
        #d= rospy.get_param("~d")
        control_arm()        
    except rospy.ROSInterruptException:
        pass