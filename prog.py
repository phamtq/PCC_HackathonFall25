# PCC Fall 2025 Hackathon Project
# Date: November 21, 2025
#
# Group members: Kieran, 
#
# Description: This project uses the DOFBOT-Pi to stack colored blocks in a
# particular order using computer vision.

#!/usr/bin/env python3
#coding=utf-8

import time
from Arm_Lib import Arm_Device

# Create the Arm object
Arm = Arm_Device()
time.sleep(.1)

# Define constants
SERVO1 = 1
SERVO2 = 2
SERVO3 = 3
SERVO4 = 4
SERVO5 = 5
SERVO6 = 6

# Initilize servos 1 - 6
Arm_serial_servo_write()
