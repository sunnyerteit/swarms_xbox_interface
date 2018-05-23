# Swarms Xbox interface
Generates an interface between Swarms input device and an userland Xpad device.

## Getting Started

### Prerequisites
To employ

### Connection with the Swarms input device
The Swarms input device employ an ethernet interface. The input device consists of two Raspberry Pi machines; the main machine has the local IP-address ```172.16.0.12```. As of May 2018 the username and password for the machine is the Raspberry Pi default. To ssh into the input device the wired connection needs to be properly set-up:

![Image of IPv4-settings on Ubuntu](IPv4.png)

In the terminal window the input device can be accessed by ssh-connection.
```[bash]
ssh pi@172.16.0.12
```