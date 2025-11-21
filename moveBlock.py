#Test script to test movement from block locations
import time
from moveArm import arm_move
import definedLocations

moveArm.arm_move(definedLocations.p_null, 500)
time.sleep(.2)
moveArm.arm_move(definedLocations.p_top, 500)
time.sleep(.2)
moveArm.arm_move(definedLocations.p_yellow, 500)
time.sleep(.2)
