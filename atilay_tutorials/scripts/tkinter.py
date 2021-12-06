#!/usr/bin/env python
import rospy
from Tkinter import *
from std_msgs.msg import String
from geometry_msgs.msg import Twist


root = Tk()
x = 2000000000000000000000000
myLabel = Label(root, text=x)

myLabel.pack()

root.mainloop()

