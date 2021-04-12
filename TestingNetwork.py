import sys
import time
import MainNode
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
id = socket.gethostname()
s.close()

node = MainNode.MainNode(ip, 10001, id)
# node2 = MainNode.MainNode("127.0.0.1", 10002, id)
time.sleep(1)

# Do not forget to start your node!
node.start()
# node2.start()
time.sleep(1)

# Connect with another node, otherwise you do not create any network!
# node.connect_with_node('127.0.0.1', 10002)
time.sleep(2)

# Example of sending a message to the nodes (dict).
node.send_to_nodes({"message": "Hi there!"})

time.sleep(5) # Create here your main loop of the application

node.stop()
# node2.stop()