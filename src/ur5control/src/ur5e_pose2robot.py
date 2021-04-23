#! /usr/bin/env python

import math
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import PoseStamped

arm_x=0
def target_pose_callback(data):
    global arm_x
    group.set_pose_target(data)
    plan1 = group.plan()
    #rospy.sleep(1)
    group.go(wait=True)
    #rospy.sleep(1)
    #arm_x=data.position.x
    rospy.loginfo("Robot subscriber arm x= %f\n",arm_x)

def move_arm():
    global arm_x
    pub = rospy.Publisher('/current_pose', PoseStamped, queue_size=10)
    rospy.Subscriber('/target_pose', PoseStamped, target_pose_callback)
    rate = rospy.Rate(10) # 10hz
    current_pose = PoseStamped()
    while not rospy.is_shutdown():
        print ("Current Pose:")
        current_pose=group.get_current_pose()
        #arm_x=current_pose.position.x
        rospy.loginfo("Robot publisher arm x= %f\n",arm_x)

        pub.publish(current_pose)
        rate.sleep()

if __name__ == '__main__':
    try:
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('ur5e_node', anonymous=True)
        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()    
        group = moveit_commander.MoveGroupCommander("manipulator")
        #d= rospy.get_param("~d")
        move_arm()
        moveit_commander.roscpp_shutdown()
    except rospy.ROSInterruptException:
        pass