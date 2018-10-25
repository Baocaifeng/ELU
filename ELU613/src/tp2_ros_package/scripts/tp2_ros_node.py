#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('talking_topic', String, queue_size=10)
    rospy.init_node('talker_node', anonymous=True)
    rate = rospy.Rate(2) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "Hello ROS World %s" % rospy.get_time()
	info = "please input a command:"+"\n"+"T: go up"
	rospy.loginfo(info)
        pub.publish(info)
        rate.sleep()
	
	move = input(":")
	rospy.loginfo(move)
	print move
	if move == "T":
            print("go up")
	elif move == "G":
	    print("go down")
	elif move == ""	
	

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
