#!/usr/bin/env python
import rospy
from Tkinter import *
from std_msgs.msg import String
from geometry_msgs.msg import Twist



def stream(data):
	rospy.loginfo("It is %s", data.linear.x)
        root = Tk()
	myLabel = Label(root, text="")
	myLabel.pack()
	myLabel.configure(text=data.linear.x)
	root.update()
	root.mainloop()

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("atilay/cmd_vel", Twist, stream)	
	rospy.spin()

if __name__ == '__main__':
	listener()
