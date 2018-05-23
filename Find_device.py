"""Finds PS4 controller in /dev/input"""
import evdev

DEVICE_NAME = 'xboxdrv_emu'

DEVICES = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for dev in DEVICES:
    if dev.name == DEVICE_NAME:
        print dev.fn.replace("/", "\/")
