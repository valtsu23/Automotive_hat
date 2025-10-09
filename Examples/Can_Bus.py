# This example code is dependent on python-can library.
# pip install python-can

import can
import os
import time

# Set the bitrate 500 kbs in this case
os.system('sudo ip link set can0 type can bitrate 500000')
# Turn the device on
os.system('sudo ifconfig can0 up')

can_bus = can.Bus(channel="can0", interface="socketcan")

# Read can bus message
message = can_bus.recv(timeout=5)
if message is None:
    print("No message received")
else:
    print("Message: ", message.data)
    print("Message ID: ", message.arbitration_id)
    print("Message data length: ", message.dlc)

# Construct message and send
msg = can.Message(arbitration_id=0x400, data=[0, 1, 2, 3, 4, 5, 6, 7])
can_bus.send(msg)
print("Message sent")

# Shut down
can_bus.shutdown()
os.system('sudo ifconfig can0 down')
