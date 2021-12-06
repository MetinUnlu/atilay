#!/usr/bin/env python
import rospy
from Tkinter import *
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time


def tkinter():	
	def stream(data):
		rospy.loginfo("It is %s", data.linear.x)
		root = Tk()	
		myLabel= Label(root, text="")
		myLabel.pack()
		def update_clock():
			vel = data.linear.x
			myLabel.configure(text=vel)
			root.after(1000, update_clock)
		update_clock()

		root.mainloop()	

	def listener():
		rospy.init_node('listener', anonymous=True)
		rospy.Subscriber("atilay/cmd_vel", Twist, stream)	
		rospy.spin()

	a = listener()
	a.spin()

if __name__ == '__main__':
	tkinter()


