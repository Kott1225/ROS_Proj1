import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32  # 整数を扱うための型（メッセージ）

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        # 'counter' という名前のトピックで、Int32型のデータを送る準備（キューサイズ: 10）
        self.publisher_ = self.create_publisher(Int32, 'counter', 10)
        
        # 0.5秒ごとに timer_callback 関数を呼び出す
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = Int32()
        msg.data = self.count
        self.publisher_.publish(msg)  # データを送信！
        self.get_logger().info(f'送信しました: {msg.data}')
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)  # ノードを動き続けさせる
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()