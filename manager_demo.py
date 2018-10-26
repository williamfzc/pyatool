from pyat import PYAToolkit
from whenconnect import when_connect, start_detect
import time


# register
PYAToolkit.bind_cmd(func_name='test_a', command='shell pm list package')


# when connect
def add_device(device_id):
    d = PYAToolkit(device_id)
    result = d.test_a()
    print(result)


# detector
when_connect(device='all', do=add_device)
start_detect()

# keep running
while True:
    time.sleep(1)
