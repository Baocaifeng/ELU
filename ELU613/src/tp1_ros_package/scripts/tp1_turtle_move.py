#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
def move():
	#starts a new node
	rospy.init_node('robot_move', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg=Twist()
	rate = rospy.Rate(2) #10hz	
	
	init(vel_msg)	

	while not rospy.is_shutdown():
		move = raw_input('move:')
		if(move == 'T') :
			vel_msg.linear.x = 4
		elif(move == 'G') :
			vel_msg.linear.x = -4
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


