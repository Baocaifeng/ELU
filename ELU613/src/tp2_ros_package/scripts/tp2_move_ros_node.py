#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
def move():
# Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()    
    #Receiveing the user's input
    print("Let's move your robot")
    speed = input("Input your speed:")
    distance = input("Type your distance:")
    velocity_publisher.publish(vel_msg)
    vel_msg.linear.x = 100
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    
    while not rospy.is_shutdown():
	move = raw_input("T:go up\n :")
	velocity_publisher.publish(vel_msg)
 	vel_msg.linear.x = 100
	vel_msg.linear.y = 0
    	vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
    	#Checking movement
    	if(move == "T"):
	    vel_msg.linear.x = abs(speed)
	    vel_msg.linear.y = 0
    	    vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
 	    velocity_publisher.publish(vel_msg)

        elif(move == "G"):
 	    pass
	    velocity_publisher.publish(vel_msg)
        elif(move == "H"):
            pass
        elif(move == "F"):
            vel_msg.linear.x = -abs(speed)
    #Since we are moving just in x-axis

	velocity_publisher.publish(vel_msg)
    



if __name__ == '__main__':
    try:
#Testing our function
        move()
    except rospy.ROSInterruptException: 
	pass
