#!/usr/bin/env python
import rospy
import serial
import os
from std_msgs.msg import Int32

ROS_NODE = os.getenv('ROS_NODE')

def encoder():
    leftWheel = rospy.Publisher('left_wheel', Int32, queue_size=0)
    rightWheel = rospy.Publisher('right_wheel', Int32, queue_size=0)
    rospy.init_node(ROS_NODE)
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=.2)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # make sure serial data is clean
        ser.flushInput()
        ser.readline()
        # read data
        line = ser.readline()[:-2].decode('utf-8')
        # Publish data
        data = line.split(",")
        leftWheel.publish(int(data[0]))
        rightWheel.publish(int(data[1]))
        rate.sleep()

if __name__ == '__main__':
    try:
        encoder()
    except rospy.ROSInterruptException:
        pass