# Swarms Xbox interface
Generates an interface between Swarms input device and an userland Xpad device.

## Getting Started
The input device outputs an UDP-packet with a JSON-object. Therefore, some steps are required to mask the input device as a gamepad.
### Prerequisites
To employ the Swarms input device with Qgroundcontrol, the Swarms input device has to be masked as recognized gamepad controller, like the Xbox 360-controller.

- [xboxdrv](https://pingus.seul.org/~grumbel/xboxdrv/)
  - The shell script employed in this repo assumes that xboxdrv is installed in /usr/bin/xboxdrv
  - For xboxdrv to work, the uinput module needs to be writeable: ```sudo chmod 0666 /dev/uinput```
- python 2.7 with [python-evdev](http://python-evdev.readthedocs.io/en/latest/install.html)

Although not required, it's beneficial to install [jstest-gtk](https://github.com/Grumbel/jstest-gtk).
```
sudo apt-get install jstest-gtk
```
This allows the user to test gamepads and joysticks.

### Connection with the Swarms input device
The Swarms input device employ an ethernet interface. The input device consists of two Raspberry Pi machines; the main machine has the local IP-address ```172.16.0.12```. As of May 2018 the username and password for the machine is the Raspberry Pi default. To ssh into the input device the wired connection needs to be properly set-up:

![Image of IPv4-settings on Ubuntu](IPv4.png)

In the terminal window the input device can be accessed by ssh-connection.
```sh
ssh pi@172.16.0.12
```

The machine doesn't send out signals by default. In the home directory there's a shell script that accesess the RPi.GPIO Python library:
```sh
./start_local.sh
```

This script sends a JSON-list through UDP-packets.

### Installation
```sh
git clone https://github.com/sunnyerteit/swarms_xbox_interface
```

## Running the program
After prerequisites are fulfilled and connection is established with the input device, the program is started through a shell-script:
```sh
# The first step allows everyone to execute the script.
sudo chmod +x Controller_event.sh

sudo ./Controller_event.sh
```
### Physical input
As of May 2018, there are only four physical joysticks that generates output to the userland Xpad device.