#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import Int32

def cb(message):
    rospy.loginfo(message.data)
    ra = random.choice(list)
    print ra
    a = int(ra)
    if message.data == a:
        print "draw"
    elif (message.data == 3 and a == 1) or (message.data == 2 and a == 3) or (message.data == 1 and a == 2):
        print "You lose"
    elif (message.data == 1 and a == 3) or (message.data == 2 and a == 1) or (message.data == 3 and a == 2): 
        print "You won!"
    else:
        print "You mistyped the command"

if __name__ == '__main__': 
    while not rospy.is_shutdown():
        list = [1,2,3]
        rospy.init_node('twice')
        sub = rospy.Subscriber('count_up', Int32, cb)
        rospy.spin()
