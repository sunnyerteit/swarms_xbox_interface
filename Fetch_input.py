"""
    - Generates userland PS4-controller
    - Listens for UDP-packets on port 8444, for all IP-adresses
    - Injects events in userland PS4-controller
"""
import socket
import json
import re
import evdev
from evdev import categorize
from evdev import UInput
from evdev import InputDevice
from evdev import ecodes as e

UDP_IP = '0.0.0.0'
UDP_PORT = 8444

DEVICES = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
PS4 = None
for dev in DEVICES:
    if dev.name == 'Sony Computer Entertainment Wireless Controller':
        PS4 = dev.fn

INPUT_DEVICE = InputDevice(PS4)

USER_INPUT = UInput.from_device(INPUT_DEVICE, name='xboxdrv_emu')
print(USER_INPUT.capabilities(verbose=True))

SOCK = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

SOCK.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = SOCK.recvfrom(10000000)
    LIST = [re.sub('[^A-Za-z0-9.-]+', "", x) for x in data.split(",")]
    CONTROLLER_1 = LIST[0:15]
    CONTROLLER_2 = LIST[15:30]

    # Lateral movement, min: 0, max: 255 [int]
    USER_INPUT.write(e.EV_ABS, e.ABS_X, int(
        255. * (float(CONTROLLER_1[0]) + 1.0) / 2.0))

    # Forward movement
    USER_INPUT.write(e.EV_ABS, e.ABS_Y, int(
        255. * (-float(CONTROLLER_1[1]) + 1.0) / 2.0))
    USER_INPUT.write(e.EV_ABS, e.ABS_RX, int(
        255. * (float(CONTROLLER_1[5]) + 1.0) / 2.0))
    USER_INPUT.write(e.EV_ABS, e.ABS_RY, int(
        255. * (float(CONTROLLER_2[5]) + 1.0) / 2.0))
        
    # Yaw manipulation
    USER_INPUT.write(e.EV_ABS, e.ABS_Z, int(
        255. * (float(CONTROLLER_2[5]) + 1.0) / 2.0))

    # Thrust (depth) movement
    USER_INPUT.write(e.EV_ABS, e.ABS_RZ, int(
        255. * (1. - (1. - float(CONTROLLER_2[10]) - (1. - float(CONTROLLER_2[9])))) / 2.0))
    USER_INPUT.syn()
