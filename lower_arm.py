#this will be the program to move the arm from its starting position to 
#position A
def arm_clamp(enable):
    if enable == 0:
        Arm.Arm_serial_servo_write(6, 0, 1000)
    else:
        Arm.Arm_serial_servo_write(6, 143, 1000)
        time.sleep(.5)

def arm_move(p, s_time = 500):
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

p_mould = [90, 130, 0, 0, 90]
p_top = [90, 80, 50, 50, 270]

