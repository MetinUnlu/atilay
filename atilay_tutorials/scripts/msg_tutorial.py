#!/usr/bin/env python
import rospy
from atilay_tutorials.msg import Num

def talker():
	pub = rospy.Publisher('chatter', Num, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10)
	order = Num()
	order.automation = 1
	order.manuel = 1
	order.test_case_1=1
	order.test_case_2=0
	while not rospy.is_shutdown():
		rospy.loginfo(order)
		pub.publish(order)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
