import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__('simple_subscriber')
        # 'counter' というトピックにデータが届いたら、listener_callback を実行する
        self.subscription = self.create_subscription(
            Int32,
            'counter',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        # データが届いたときに動く処理
        self.get_logger().info(f'受信しました: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = SimpleSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()