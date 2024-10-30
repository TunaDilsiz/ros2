#!/usr/bin/env python3
import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
import time
from turtlesim.srv import SetPen
import random
class Mdraw(Node):
    def __init__(self):
        super().__init__("draw_recc")
        self.turtle_mvr = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.client = self.create_client(SetPen,"/turtle1/set_pen")
        self.timer = self.create_timer(1.0,self.mover)
        self.get_logger().info("drawing a colorful rectangle")
        self.step = 0
    
    def mover(self):
        
        color = [(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))]
        req = SetPen.Request()
        req.r = color[0][0]
        req.g = color[0][1]
        req.b = color[0][2]
        req.width = 2
        self.client.call_async(req)
        msg = Twist()
        req.width = 2
        if self.step % 2 == 0:
            msg.linear.x = 3.0
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = 1.57
            
            
        
        self.turtle_mvr.publish(msg)
        
        self.step += 1
        if self.step == 8:
            self.destroy_node()
        
    
    

def main(args=None):
    rclpy.init(args=args)
    node = Mdraw()
    rclpy.spin(node)


    rclpy.shutdown()

if __name__=="__main__":
    main()
