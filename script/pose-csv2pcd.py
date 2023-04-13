import numpy as np
import open3d as o3d
import sys
import csv

def csv2pcd(input_csv, output_pcd):
    poses = []
    with open(input_csv, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)

        for row in csv_reader:
            x = float(row[4])
            y = float(row[5])
            z = float(row[6])
            poses.append([x, y, z])

    if len(poses) > 0:
        point_cloud = o3d.geometry.PointCloud()
        point_cloud.points = o3d.utility.Vector3dVector(np.asarray(poses))
        o3d.io.write_point_cloud(output_pcd, point_cloud)
        print("Saved {} poses to {}".format(len(poses), output_pcd))
    else:
        print("No poses found in the input CSV file")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python csv2pcd.py <input_csv> <output_pcd>")
        exit(1)

    input_csv = sys.argv[1]
    output_pcd = sys.argv[2]
    csv2pcd(input_csv, output_pcd)