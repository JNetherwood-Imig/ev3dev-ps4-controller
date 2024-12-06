#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop, Direction, Button)
from pybricks.tools import wait

from auto import (auto, auto_button, stop_button, disable_stop_button, left_motor, right_motor, arm_motor, controller_deadzone)
from definitions import (ButtonEvent, AxisCode, EventType, ButtonCode)
import struct
import usys
from sys import exit

######################################################
# DO NOT MODIFY THIS FILE (main.py)                  #
# UNLESS YOU KNOW WHAT YOU ARE DOING                 #
#                                                    #
# Coding is intended to be done in the auto.py file, #
# where you will set up your robot and               #
# write your autonomous code                         #
# To switch to the unstable dev branch,              #
# use 'git switch dev' in the terminal               #
######################################################

# Helper function to scale values from a source range to a destination range
def scale(val, source, target):
    return (float(val - source[0]) / (source[1] - source[0])) * (target[1] - target[0]) + target[0]


# main function
def main():
    print("Implementation: " + str(usys.implementation))
    print("Version: " + str(usys.version))


    DATA_FORMAT = 'llHHI'    
    EVENT_SIZE = struct.calcsize(DATA_FORMAT)

    # Open controller input file
    in_file = None
    try:
        in_file = open("/dev/input/event4", "rb")
        print("Controller connected!")
    except:
        print("Failed to open /dev/input/event4 for reading.")
        print("Make sure your controller is turned on and connected.")
        exit(1)

    # Declare variables to store movement speeds as set by the controller
    drive_speed = 0
    turn_rate = 0
    arm_power = 0

    event = in_file.read(EVENT_SIZE)

    while event:
        (_, _, ev_type, code, value) = struct.unpack(DATA_FORMAT, event)
        
        # Read analog stick values    
        if ev_type == EventType.AXIS:
            if code == AxisCode.LEFT_STICK_Y:
                drive_speed = scale(value, (0,255), (100,-100))
                if abs(drive_speed) < controller_deadzone * 100:
                    drive_speed = 0
            if code == AxisCode.RIGHT_STICK_X:
                turn_rate = scale(value, (0,255), (100, -100))
                if abs(turn_rate) < controller_deadzone * 100:
                    turn_rate = 0
            if code == AxisCode.LEFT_TRIGGER:
                arm_power = value / 3
            if code == AxisCode.RIGHT_TRIGGER:
                arm_power = -value / 3
        if ev_type == EventType.BUTTON:
            if code == stop_button and value == ButtonEvent.PRESSED and not disable_stop_button:
                break
            if code == auto_button and value == ButtonEvent.PRESSED:
                auto()
            # Example: X button
            if code == ButtonCode.X:
                # Do someting with x button
                pass
                
        arm_motor.dc(arm_power)
        left_motor.dc(drive_speed - turn_rate)
        right_motor.dc(drive_speed + turn_rate)

        event = in_file.read(EVENT_SIZE)

    in_file.close()

# program entry point
if __name__ == "__main__":
    main()

