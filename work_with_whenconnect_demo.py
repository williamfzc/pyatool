""" working with whenconnect, a simple device management (remote mode) """
from whenconnect import when_connect, when_disconnect, start_detect
from pyatool import PYAToolkit
import time


device_dict = dict()


def add_device(device_id):
    if '.' in device_id:
        return
    # if you don't need remote connect, just remove argument `mode`
    new_device = PYAToolkit(device_id, mode='remote')
    device_dict[device_id] = new_device


def remove_device(device_id):
    if '.' in device_id:
        return
    if device_id in device_dict:
        device_dict[device_id].terminate()
        del device_dict[device_id]


when_connect(device='all', do=add_device)
when_disconnect(device='all', do=remove_device)
start_detect()

while True:
    time.sleep(2)
    if device_dict:
        for k, v in device_dict.items():
            print(k, v.device_id, v.device_ip)
