#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist



def turtle_circle(radius):
    rospy.init_node('circle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
    rate = rospy.Rate(1)
    vel = Twist()

    for i in range (0,10):
        vel.linear.x = radius
        vel.angular.z = 1.0
        rospy.loginfo("Radius = %f",radius)
        pub.publish(vel)
        rate.sleep()


if name == 'main':
    for i in range (2,7,2):
      turtle_circle(i)
