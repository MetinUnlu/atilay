#!/usr/bin/env python
import rospy
from atilay_tutorials.msg import Num
from geometry_msgs.msg import Twist


def callback(data):
	order = data.automation
	rospy.loginfo(order)
	def stream(data):
		if order == 1:
        		rospy.loginfo("It is %s", data.linear.x)
		else:
			rospy.loginfo("No automation")



def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("chatter", Num, callback)
	rospy.Subscriber("atilay/cmd_vel", Twist, stream)
	rospy.spin()

if __name__ == '__main__':
	listener()
