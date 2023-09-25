#!/usr/bin/env python3

import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations


def create_pose_stamped(navigator,position_x,position_y,orientation_z):
    q_x,q_y,q_z,q_w=tf_transformations.quaternion_from_euler(0.0,0.0,0.0)
    pose=PoseStamped()
    pose.header.frame_id ='map'
    pose.header.stamp=navigator.get_clock().now().to_msg()
    pose.pose.position.x=position_x
    pose.pose.position.y=position_y
    pose.pose.position.z= 0.0
    pose.pose.orientation.x=q_x
    pose.pose.orientation.y=q_y
    pose.pose.orientation.z=q_z
    pose.pose.orientation.w=q_w

    return pose


def main():
    # initilaizing rclpy
    rclpy.init()
    nav=BasicNavigator()

    # lets set initial poses
    initial_pose=create_pose_stamped(nav, 0.0, 0.0, 0.0)
    nav.setInitialPose(initial_pose)
    # wait for nav2
    nav.waitUntilNav2Active()
    
    # send the nav2 goal
    goal_pose_1=create_pose_stamped(nav, 3.5, 1.0,1.57)
    goal_pose_2=create_pose_stamped(nav, 2.0, 2.5,3.14)
    goal_pose_3=create_pose_stamped(nav, 0.5, 1.0,-1.57)
    goal_pose_4=create_pose_stamped(nav, 0.0, 0.0,0.0)

    # for one goal pose 
    # nav.goToPose(goal_pose_1)
    # while not nav.isTaskComplete():
    #     feedback=nav.getFeedback()
    #     # print(feedback)

    # for waypoints
    waypoints=[goal_pose_1, goal_pose_2, goal_pose_3, goal_pose_4]
    nav.followWaypoints(waypoints)
    while not nav.isTaskComplete():
        feedback=nav.getFeedback()
        # print(feedback)

    print(nav.getResult())

    rclpy.shutdown()



if __name__ == '__main__':
    main()