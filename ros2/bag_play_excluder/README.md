# ROS2 Bag Play Excluder

ROS2 Bag Play Excluder is a simple shell script for filtering and playing back ROS2 bag files while excluding specified topics.

## Prerequisites

- ROS2 (Humble Hawksbill or later is recommended)

## Usage
To use the script, simply run it with the path to your bag file and the topics you wish to exclude as arguments. For example:

```bash
./filter_bag2.sh <path_to_your_bag_file> /topic_to_exclude1 /topic_to_exclude2 ...
```
This command will play back the bag file with the specified topics excluded.
