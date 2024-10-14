#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop, Direction, Button)
from pybricks.tools import wait

from auto import (auto, auto_button, stop_button, disable_stop_button, left_motor, right_motor, arm_motor)
from definitions import (ButtonEvent, AxisCode, EventType)
import struct
import usys
import sys

def main():
    print("Implementation: " + str(usys.implementation))
    print("Version: " + str(usys.version))

    def scale(source, source_range, target_range):
        return (float(source-source_range[0]) / (source_range[1]-source_range[0])) * (target_range[1]-target_range[0])+target_range[0]

    DATA_FORMAT = 'llHHI'    
    EVENT_SIZE = struct.calcsize(DATA_FORMAT)

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
            if code == AxisCode.RIGHT_STICK_X:
                turn_rate = scale(value, (0,255), (100, -100))
            if code == AxisCode.LEFT_TRIGGER:
                arm_power = value / 3
            if code == AxisCode.RIGHT_TRIGGER:
                arm_power = -value / 3
        if ev_type == EventType.BUTTON:
            if code == stop_button and value == ButtonEvent.PRESSED and not disable_stop_button:
                break
            if code == auto_button and value == ButtonEvent.PRESSED:
                auto()
                
        arm_motor.dc(arm_power)
        left_motor.dc(drive_speed - turn_rate)
        right_motor.dc(drive_speed + turn_rate)

        event = in_file.read(EVENT_SIZE)

    in_file.close()

if __name__ == "__main__":
    main()

