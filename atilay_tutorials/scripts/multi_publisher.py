#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	pub2 = rospy.Publisher('atilay/cmd_vel', Twist, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10)
	twist = Twist()
	while not rospy.is_shutdown():
		hello_str = " hello world %s" % rospy.get_time()
		twist.linear.x=1
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		pub2.publish(twist)
		rate.sleep()

def stream():
	pub=rospy.Publisher('atilay/cmd_vel', Twist, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10)
	twist = Twist()
	while not rospy.is_shutdown():
		twist.linear.x=1
		rospy.loginfo(twist) 
		pub.publish(twist)
		rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
