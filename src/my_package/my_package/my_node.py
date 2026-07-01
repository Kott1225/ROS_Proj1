import rclpy
from rclpy.node import Node


def main():
    rclpy.init()
    node = Node("hello_node")
    node.get_logger().info("Hello, ROS2! SUCCESSFUL")
    rclpy.shutdown()


if __name__ == "__main__":
    main()
