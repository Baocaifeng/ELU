#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
def move():
	#starts a new node
	rospy.init_node('robot_move', anonymous=True)
	velocity_publisher = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=10)
	vel_msg=Twist()
	rate = rospy.Rate(2) #10hz	
	
	init(vel_msg)	
	rospy.loginfo('move your robot !')
	rospy.loginfo('use 1~9 to change speed from 0.1~0.9m/s')
	rospy.loginfo('T:go up G:go down H:turn left F:turn right')
	speed = input("speed:")
	speed = speed*100
	while not rospy.is_shutdown():
		move = raw_input('move:')
		if(move == 'T') :
			vel_msg.linear.x = speed
		elif(move == 'G') :
			vel_msg.linear.x = -speed
		elif(move == 'H') :
			vel_msg.angular.z = 1.57
		elif(move == 'F') :
	   		vel_msg.angular.z = -1.57
		else :
			rospy.loginfo('try again !')			

		velocity_publisher.publish(vel_msg)
		init(vel_msg)
		rate.sleep()


def init(vel_msg):
	# vel_msg: type Twist()	
	vel_msg.linear.x = 0
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0	

if __name__ == '__main__' :
	try:
		move()
	except rospy.ROSInterruptException :
		pass


