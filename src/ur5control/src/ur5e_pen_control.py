#! /usr/bin/env python

import math
import numpy as np
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import rospy
import geometry_msgs.msg
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseStamped

pose_pen=[-0.45,0.55,0.55,0,90,180]

def pose_current_callback(data):
    current_pose = PoseStamped()
    arm_x=data.pose.position.x
    #rospy.loginfo("Current pose arm x= %f\n",arm_x)

def control_arm():
    global pose_pen
    pub = rospy.Publisher('/pose_target', Pose, queue_size=10)
    rospy.Subscriber('/pose_current', PoseStamped, pose_current_callback)
    rate = rospy.Rate(10) # 10hz
    pose_target = Pose()
    pose_target.position.x = pose_pen[0]
    pose_target.position.y = pose_pen[1]
    pose_target.position.z = pose_pen[2]
    r=math.radians(pose_pen[3])
    p=math.radians(pose_pen[4])
    w=math.radians(pose_pen[5])
    quat1=quaternion_from_euler(r,p,w)
    pose_target.orientation.x = quat1[0]
    pose_target.orientation.y = quat1[1]
    pose_target.orientation.z = quat1[2]
    pose_target.orientation.w = quat1[3]
    while not rospy.is_shutdown():
        print ("Target Pose arm TCP:")
        rospy.loginfo("Target pose arm = %s\n",pose_pen)

        pub.publish(pose_target)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('pen_control', anonymous=True)
        #d= rospy.get_param("~d")
        control_arm()        
    except rospy.ROSInterruptException:
        pass