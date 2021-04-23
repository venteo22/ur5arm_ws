#! /usr/bin/env python

import math
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import PoseStamped Pose

arm_x=0
def current_pose_callback(data):
    global arm_x
    current_pose = PoseStamped()
    #arm_x=data.position.x
    rospy.loginfo("Current pose arm x= %f\n",arm_x)

def control_arm():
    global arm_x
    pub = rospy.Publisher('/target_pose', PoseStamped, queue_size=10)
    rospy.Subscriber('/current_pose', PoseStamped, current_pose_callback)
    rate = rospy.Rate(10) # 10hz
    pose_target = geometry_msgs.msg.Pose()
    pose_target.position.x = -0.3
    pose_target.position.y = 0.5
    pose_target.position.z = 0.5
    r=math.radians(0)
    p=math.radians(0)
    w=math.radians(0)
    quat1=quaternion_from_euler(r,p,w)

    pose_target.orientation.x = quat1[0]
    pose_target.orientation.y = quat1[1]
    pose_target.orientation.z = quat1[2]
    pose_target.orientation.w = quat1[3]
    while not rospy.is_shutdown():
        print ("Target Pose:")
        #arm_x=current_pose.position.x
        rospy.loginfo("Target pose arm x= %f\n",arm_x)

        pub.publish(pose_target)
        rate.sleep()

if __name__ == '__main__':
    try:
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('pen_control', anonymous=True)
        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()    
        group = moveit_commander.MoveGroupCommander("manipulator")
        #d= rospy.get_param("~d")
        control_arm()
        moveit_commander.roscpp_shutdown()
    except rospy.ROSInterruptException:
        pass