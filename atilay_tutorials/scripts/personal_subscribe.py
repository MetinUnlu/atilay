#!/usr/bin/env python
import rospy
from atilay_tutorials.msg import Num


def callback(data):
	order = data.automation
	rospy.loginfo(order)



def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("chatter", Num, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
