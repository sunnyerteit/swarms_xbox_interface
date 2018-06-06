import socket
import time
import re

INDEX_TRANSLATION_X = 1     # axis is normal
INDEX_TRANSLATION_Y = 2     # axis is inverted (string)
INDEX_TILT_Y = 3            # axis is inverted (string)
INDEX_TILT_X = 4            # axis is inverted (string)
INDEX_ROTATION = 5          # axis is inverted (string)

INDEX_BUTTON_CIRCLE = 11    # default value "true" or "false" (string)
INDEX_BUTTON_TRIANGLE = 12  # default value "true" or "false" (string)
INDEX_BUTTON_SQUARE = 13    # default value "true" or "false" (string)

# Value is "0" where the KNOB is turned 
INDEX_KNOB_START = 6
INDEX_KNOB_STOP = 8

class SwarmsIID:
    def __init__(self):
        self.joy_input = {'lx': 0, 'ly': 0, 'rx': 0, 'ry': 0, 'btn_a': 0, 'btn_x': 0, 'btn_b': 0}
        self.joy_input_old = {'lx': 0, 'ly': 0, 'rx': 0, 'ry': 0, 'btn_a': 0, 'btn_x': 0, 'btn_b': 0}
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.setblocking(1)
            self.sock.bind(("0.0.0.0", 8444))
        except socket.error as e:
            print("SocketError: {}".format(e))
            raise e

    def get_joy_input(self):
        try:
            data, adress = self.sock.recvfrom(4096)
        except socket.error as e:
            raise e

        LIST = [re.sub('[^A-Za-z0-9.-]+', "", x) for x in data.split(",")]

        CONTROLLER_1 = LIST[0:15]
        CONTROLLER_2 = LIST[15:30]

        for i in range(11,14):
            if(CONTROLLER_1[i] == "true"):
                CONTROLLER_1[i] = 1
            else:
                CONTROLLER_1[i] = 0

        #print("CONTROLLER_1: {}".format(CONTROLLER_1))
        #print("CONTROLLER_2: {}".format(CONTROLLER_2))
        
        self.joy_input = {
                    'lx': float("%.3f" % float(CONTROLLER_1[INDEX_ROTATION])), 
                    'ly': float("%.3f" % (0.0 - float(CONTROLLER_1[INDEX_TILT_Y]))), 
                    'rx': float("%.3f" % (0.0 - float(CONTROLLER_2[INDEX_TILT_X]))), 
                    'ry': float("%.3f" % (0.0 - float(CONTROLLER_2[INDEX_TILT_Y]))), 
                    'btn_a': CONTROLLER_1[INDEX_BUTTON_CIRCLE], 
                    'btn_x': CONTROLLER_1[INDEX_BUTTON_TRIANGLE], 
                    'btn_b': CONTROLLER_1[INDEX_BUTTON_SQUARE]
                    }
                
        return self.joy_input