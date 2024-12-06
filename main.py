#!/usr/bin/env pybricks-micropython

####################################################
# WARNING: This is an unstable development branch. #
# All new features are first implemented here,     #
# meaning that breaking changes are possible.      #
# Unless you need any of the unstable features,    #
# it is recommended that you use the main branch.  #
####################################################

import user_code as config
from definitions import (ButtonEvent, AxisCode, EventType)
from controller_callbacks import controller_callbacks

from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop, Direction, Button)
from pybricks.tools import wait
import usys

import struct
from sys import exit
import io

######################################################
# DO NOT MODIFY THIS FILE (main.py)                  #
# UNLESS YOU KNOW WHAT YOU ARE DOING                 #
#                                                    #
# Coding is intended to be done in the auto.py file, #
# where you will set up your robot and               #
# write your autonomous code                         #
######################################################

class Controller:
    left_x: float = 0
    left_y: float = 0
    right_x: float = 0
    right_y: float = 0

def update_controller(ev_type: int, ev_code: int, ev_value: int):
    if ev_type != EventType.AXIS:
        return

    value: float = scale(ev_value, (0, 255), (100, -100))
    value = 0 if abs(value) < config.controller_deadzone * 100 else value

    if ev_code == AxisCode.LEFT_STICK_X:
        Controller.left_x = value
    elif ev_code == AxisCode.LEFT_STICK_Y:
        Controller.left_y = value
    elif ev_code == AxisCode.RIGHT_STICK_X:
        Controller.right_x = value
    elif ev_code == AxisCode.RIGHT_STICK_Y:
        Controller.right_y = value

# Helper function to scale values from a source range to a destination range
def scale(val: float, source: tuple[int, int], target: tuple[int, int]) -> float:
    return (float(val - source[0]) / (source[1] - source[0])) * (target[1] - target[0]) + target[0]

# Implementation from
# https://xiaoxiae.github.io/Robotics-Simplified-Website/drivetrain-control/arcade-drive/
def arcade_drive():
    drive: float = Controller.left_y
    rotate: float = -Controller.right_x
    # variables to determine the quadrants
    maximum = max(abs(drive), abs(rotate))
    total, difference = drive + rotate, drive - rotate

    left_power: float = 0
    right_power: float = 0

    # set speed according to the quadrant that the values are in
    if drive >= 0:
        if rotate >= 0:  # I quadrant
            left_power = maximum
            right_power = difference
        else:            # II quadrant
            left_power = total
            right_power = maximum
    else:
        if rotate >= 0:  # IV quadrant
            left_power = total
            right_power = -maximum
        else:            # III quadrant
            left_power = -maximum
            right_power = difference

    if config.reverse_motor_direction:
        left_power *= -1
        right_power *= -1

    config.left_motor.dc(left_power)
    config.right_motor.dc(right_power)

# TODO: Fix tank drive
# Current logic doesn't quite work,
# I think right motor needs to be reversed,
# but I can't test it right now
# def tank_drive() -> None:
#     left_power = Controller.left_y
#     right_power = Controller.right_y
#     if config.reverse_motor_direction:
#         left_power *= -1
#         right_power += -1
#
#     config.left_motor.dc(left_power)
#     config.right_motor.dc(right_power)

def open_input_file(path: str) -> io.BufferedReader:
    try:
        in_file: io.BufferedReader = open(path, "rb")
        print("Controller connected!")
        return in_file
    except:
        print("Failed to open {} for reading.".format(path))
        print("Make sure your controller is turned on and connected.")
        exit(1)

# main function
def main() -> None:
    print("Implementation: " + str(usys.implementation))
    print("Version: " + str(usys.version))

     # Corresponds to 'sec: long, usec: long, type: ushort, code: ushort, value: uint'
    DATA_FORMAT: str = "llHHI"
    EVENT_SIZE: int = struct.calcsize(DATA_FORMAT)

    # Open controller input file
    in_file: io.BufferedReader = open_input_file("/dev/input/event" + str(config.controller_file))

    config.on_init()

    event: bytes = in_file.read(EVENT_SIZE)

    while event:
        (_, _, ev_type, ev_code, ev_value) = struct.unpack(DATA_FORMAT, event)
        if ev_type == EventType.BUTTON:
            if ev_code == config.stop_button and ev_value == ButtonEvent.PRESSED and not config.disable_stop_button:
                break
            if ev_code == config.auto_button and ev_value == ButtonEvent.PRESSED:
                config.auto()
            for cb in controller_callbacks:
                cb.try_run(ev_type, ev_code, ev_value)
        
        update_controller(ev_type, ev_code, ev_value)
        arcade_drive()

        if not config.disable_arm_motor:
            arm_sensitivity: float = 0.25
            arm_power: float = 0
            if ev_type == EventType.AXIS:
                if ev_code == AxisCode.LEFT_TRIGGER:
                    arm_power = ev_value * arm_sensitivity
                if ev_code == AxisCode.RIGHT_TRIGGER:
                    arm_power = -ev_value * arm_sensitivity
            config.arm_motor.dc(arm_power)

        event = in_file.read(EVENT_SIZE)

    in_file.close()

# program entry point
if __name__ == "__main__":
    main()

