# PCC Fall 2025 Hackathon Project
# Date: November 21, 2025
#
# Group members: Kieran, Tim, Conner
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

MAX_GRIP = 143
RESET_GRIP_POS = 0
RESET_SERVO_POS = 90

# Function definitions
def reset_all():
    Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write(6, 0, 100)
    time.sleep(1)

# Initialize/reset servos to upright position
reset_all()
