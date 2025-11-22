#this will be the program to move the arm from various locations
import time
from Arm_Lib import Arm_Device

Arm = Arm_Device()
time.sleep(.1)

MAX_GRIP = 143
RESET_GRIP = 0

def arm_move(p, s_time = 5000):
    for i in range(5):
        id = i + 1
        if id == 5:
            time.sleep(.1)
            Arm.Arm_serial_servo_write(id, p[i], int(s_time*1.5))
        elif id == 1:
            Arm.Arm_serial_servo_write(id, p[i], int(3*s_time/4))
        else:
            Arm.Arm_serial_servo_write(id, p[i], int(s_time))
        time.sleep(.01)
    time.sleep(s_time/1000)

def reset_all():
    Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, 5000)
    time.sleep(1)
    Arm.Arm_serial_servo_write(6, 0, 1000)
    time.sleep(1)

def switch_clamp(value):
    Arm.Arm_serial_servo_write(6, value, 1000) 
    time.sleep(1)
    


