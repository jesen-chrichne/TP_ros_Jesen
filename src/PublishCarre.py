#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool
Button = [False]
def talker(Button):
    pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(15) # 15hz
    msg = PoseStamped()
    dist = 5
    msg.header.frame_id = "map"
    msg.pose.position.x = 0
    msg.pose.position.y = 0
    boucle = True
    add = 1
    j = 0
    while not rospy.is_shutdown():
        i = 0
        if j % 2 == 0:
            add *= -1
        
        
        while i < 5:
            listener(Button)
            if not Button[0]:
                continue
                
            if boucle:
                msg.pose.position.x += add
                
        
            else:
                msg.pose.position.y += add
                
            i += 1
            pub.publish(msg)
	    rate.sleep()
        else:
            
            boucle = not boucle   
            j += 1
         
        #hello_str = "hello world %s" % rospy.get_time()
       
        

		

def callback(button,data):
    button[0] = data.data
    

def listener(Button):

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    rospy.Subscriber('button_state', Bool, lambda data,button=Button:callback(button,data))

if __name__ == '__main__':
    try:
	
        talker(Button)
    except rospy.ROSInterruptException:
        pass
