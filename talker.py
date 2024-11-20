

import rospy
from std_msgs.msg import String # 
import sys
import time
import os

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) 
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    count = 0
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % count
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        count += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass