# ROS2 cheatseat

## Record `/ns1/*`, `/ns2/*`, `/topic1`, and  topics using `ros2 bag`

```bash
ros2 bag record -e "(/ns1/.*|/ns2/.*|/topic1)"
```