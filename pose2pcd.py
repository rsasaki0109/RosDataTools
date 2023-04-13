import rospy
import rosbag
import open3d as o3d
import sys
import numpy as np
from geometry_msgs.msg import PoseStamped

def pose2pcd(input_bag, output_pcd, target_topic):
    poses = []
    with rosbag.Bag(input_bag, 'r') as bag:
        for topic, msg, t in bag.read_messages():
            if topic == target_topic:
                if type(msg).__name__ == '_geometry_msgs__PoseStamped':
                    position = msg.pose.position
                elif type(msg).__name__ == '_geometry_msgs__PoseWithCovarianceStamped':
                    position = msg.pose.pose.position
                else:
                    continue

                poses.append([position.x, position.y, position.z])

    if len(poses) > 0:
        point_cloud = o3d.geometry.PointCloud()
        point_cloud.points = o3d.utility.Vector3dVector(np.asarray(poses))
        o3d.io.write_point_cloud(output_pcd, point_cloud)
        print("Saved {} poses to {}".format(len(poses), output_pcd))
    else:
        print("No PoseStamped messages found in the input bag file for the specified topic")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python pose2pcd.py <input_bag> <output_pcd> <target_topic>")
        exit(1)

    input_bag = sys.argv[1]
    output_pcd = sys.argv[2]
    target_topic = sys.argv[3]
    pose2pcd(input_bag, output_pcd, target_topic)
