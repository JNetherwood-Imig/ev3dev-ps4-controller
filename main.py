#!/usr/bin/env pybricks-micropython
from auto import (auto, auto_button, stop_button, disable_stop_button, left_motor, right_motor, arm_motor)
from definitions import (ButtonEvent, AxisCode, EventType)

from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop, Direction, Button)
from pybricks.tools import wait
import usys

import struct
from sys import exit
from io import BufferedReader

######################################################
# DO NOT MODIFY THIS FILE (main.py)                  #
# UNLESS YOU KNOW WHAT YOU ARE DOING                 #
#                                                    #
# Coding is intended to be done in the auto.py file, #
# where you will set up your robot and               #
# write your autonomous code                         #
######################################################

# Helper function to scale values from a source range to a destination range
def scale(val, source: tuple[int, int], target: tuple[int, int]):
    return (float(val - source[0]) / (source[1] - source[0])) * (target[1] - target[0]) + target[0]


def arcade_drive(ev_type: int, ev_code: int, ev_value: int):
    drive_speed = 0
    turn_rate = 0
    if ev_type == EventType.AXIS:
        if ev_code == AxisCode.LEFT_STICK_Y:
            drive_speed = scale(ev_value, (0,255), (100, -100))
        if ev_code == AxisCode.RIGHT_STICK_X:
            turn_rate = scale(ev_value, (0,255), (100, -100))

        left_motor.dc(drive_speed - turn_rate)
        right_motor.dc(drive_speed + turn_rate)

def tank_drive(ev_type: int, ev_code: int, ev_value: int):
    left_power = 0
    right_power = 0
    if ev_type == EventType.AXIS:
        if ev_code == AxisCode.LEFT_STICK_Y:
            left_power = scale(ev_value, (0, 255), (100, -100))
        if ev_code == AxisCode.RIGHT_STICK_Y:
            right_power = scale(ev_value, (0, 255), (100, -100))

    left_motor.dc(left_power)
    right_motor.dc(right_power)

def open_input_file(path: str) -> BufferedReader:
    try:
        in_file: BufferedReader = open(path, "rb")
        print("Controller connected!")
        return in_file
    except:
        print(f"Failed to open {path} for reading.")
        print("Make sure your controller is turned on and connected.")
        exit(1)

# main function
def main():
    print("Implementation: " + str(usys.implementation))
    print("Version: " + str(usys.version))

     # Corresponds to 'sec: long, usec: long, type: ushort, code: ushort, value: uint'
    DATA_FORMAT: str = "llHHI"
    EVENT_SIZE: int = struct.calcsize(DATA_FORMAT)

    # Open controller input file
    in_file: BufferedReader = open_input_file("/dev/input/event4")

    event: bytes = in_file.read(EVENT_SIZE)

    while event:
        (_, _, ev_type, ev_code, ev_value) = struct.unpack(DATA_FORMAT, event)
        if ev_type == EventType.BUTTON:
            if ev_code == stop_button and ev_value == ButtonEvent.PRESSED and not disable_stop_button:
                break
            if ev_code == auto_button and ev_value == ButtonEvent.PRESSED:
                auto()
        
        arcade_drive(ev_type, ev_code, ev_value)
        # tank_drive(ev_type, ev_code, ev_value)

        arm_power = 0
        arm_sensitivity = 0.3
        if ev_type == EventType.AXIS:
            if ev_code == AxisCode.LEFT_TRIGGER:
                arm_power = ev_value * arm_sensitivity
            if ev_code == AxisCode.RIGHT_TRIGGER:
                arm_power = -ev_value * arm_sensitivity
        arm_motor.dc(arm_power)

        event = in_file.read(EVENT_SIZE)

    in_file.close()

# program entry point
if __name__ == "__main__":
    main()

