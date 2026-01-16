import rclpy
from rclpy.node import Node
from mavros_msgs.srv import CommandBool, SetMode, CommandTOL
from mavros_msgs.msg import State

class SitlTakeoffNode(Node):
    def __init__(self):
        super().__init__('sitl_takeoff_node')
        
        # Clients
        self.arm_client = self.create_client(CommandBool, '/mavros/cmd/arming')
        self.mode_client = self.create_client(SetMode, '/mavros/set_mode')
        self.takeoff_client = self.create_client(CommandTOL, '/mavros/cmd/takeoff')
        
        # State Subscriber
        self.state_sub = self.create_subscription(State, '/mavros/state', self.state_callback, 10)
        self.current_state = State()

        # Wait for services to be available
        while not self.arm_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for MAVROS services...')

    def state_callback(self, msg):
        self.current_state = msg

    def start_mission(self):
        # 1. Set Mode to GUIDED
        mode_req = SetMode.Request()
        mode_req.custom_mode = 'GUIDED'
        self.mode_client.call_async(mode_req)
        self.get_logger().info("Setting mode to GUIDED...")

        # 2. Arm the drone
        arm_req = CommandBool.Request()
        arm_req.value = True
        self.arm_client.call_async(arm_req)
        self.get_logger().info("Arming motors...")

        # 3. Takeoff to 10m
        takeoff_req = CommandTOL.Request()
        takeoff_req.altitude = 10.0
        self.takeoff_client.call_async(takeoff_req)
        self.get_logger().info("Takeoff initiated!")

def main(args=None):
    rclpy.init(args=args)
    node = SitlTakeoffNode()
    
    # Simple delay to ensure state is received before commanding
    import time
    time.sleep(2) 
    
    node.start_mission()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()