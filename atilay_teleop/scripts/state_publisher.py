#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from atilay_msg.msg import State

def talker():
	pub = rospy.Publisher('chatter', State, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		state = State()
		state.automation=0
		rospy.loginfo(state.automation)
		pub.publish(state)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
