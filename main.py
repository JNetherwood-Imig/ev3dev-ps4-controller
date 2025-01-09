#!/usr/bin/env pybricks-micropython

####################################################
# WARNING: This is an unstable development branch. #
# All new features are first implemented here,     #
# meaning that breaking changes are possible.      #
# Unless you need any of the unstable features,    #
# it is recommended that you use the main branch.  #
####################################################

import user_code as config
from utils import (ButtonEvent, AxisCode, EventType, print_ports)
from controller_callbacks import cb_list

from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font
import usys

import struct
from sys import exit
import io
import re
from time import sleep

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

    config.left_motor.dc(left_power * config.left_motor_sensitivity)
    config.right_motor.dc(right_power * config.right_motor_sensitivity)

def tank_drive() -> None:
    left_power = Controller.left_y
    right_power = Controller.right_y
    if config.reverse_motor_direction:
        left_power *= -1
        right_power += -1

    config.left_motor.dc(left_power)
    config.right_motor.dc(right_power)

def get_input_file_path() -> str:
    ev3: EV3Brick = EV3Brick()
    try:
        event_list: io.TextIOWrapper = open("/proc/bus/input/devices", "r")
        content: str = event_list.read()
        devices = content.strip().split("\n\n")
        for device in devices:
            if "Name=\"Wireless Controller\"" in device:
                match = re.search(r"Handlers=(\S+)", device)
                if match:
                    return "/dev/input/" + match.group(1)
                else:
                    ev3.screen.clear()
                    ev3.screen.set_font(Font(size=14))
                    ev3.screen.print("Failed to find event handler for controller.")
                    sleep(15)
                    exit(1)
        ev3.screen.clear()
        ev3.screen.set_font(Font(size=14))
        ev3.screen.print("Failed to find\n\"Wireless Controller\"\nin /proc/bus/input/devices.")
        ev3.screen.print("Make sure your controller\nis turned on and connected.")
        sleep(15)
        exit(1)
        
    except:
        print("Failed to get event file list")
        exit(1)

def open_input_file(path: str) -> io.BufferedReader:
    ev3: EV3Brick = EV3Brick()
    ev3.screen.clear()
    ev3.screen.set_font(Font(size=14))
    try:
        in_file: io.BufferedReader = open(path, "rb")
        ev3.screen.print("Controller connected!")
        ev3.screen.print("Using\n" + path)
        return in_file
    except:
        ev3.screen.print("Failed to open " + path + " for reading.")
        ev3.screen.print("Make sure your controller is turned on and connected.")
        sleep(15)
        exit(1)

def main() -> None:
    print("Implementation: " + str(usys.implementation))
    print("Version: " + str(usys.version))
    print_ports()

    # Corresponds to 'sec: long, usec: long, type: ushort, code: ushort, value: uint'
    DATA_FORMAT: str = "llHHI"
    EVENT_SIZE: int = struct.calcsize(DATA_FORMAT)

    in_file: io.BufferedReader = open_input_file(get_input_file_path())

    config.on_init()

    event: bytes = in_file.read(EVENT_SIZE)

    arm_power: float = 0
    while event:
        (_, _, ev_type, ev_code, ev_value) = struct.unpack(DATA_FORMAT, event)
        if ev_type == EventType.BUTTON:
            if ev_code == config.stop_button and ev_value == ButtonEvent.PRESSED and not config.disable_stop_button:
                break
            if ev_code == config.auto_button and ev_value == ButtonEvent.PRESSED:
                config.auto()
            for cb in cb_list:
                cb.try_run(ev_type, ev_code, ev_value)
        
        update_controller(ev_type, ev_code, ev_value)
        if config.use_tank_drive:
            tank_drive()
        else:
            arcade_drive()

        if not config.disable_arm_motor:
            if ev_type == EventType.AXIS:
                if ev_code == AxisCode.LEFT_TRIGGER:
                    arm_power = ev_value * config.arm_motor_sensitivity
                if ev_code == AxisCode.RIGHT_TRIGGER:
                    arm_power = -ev_value * config.arm_motor_sensitivity
            config.arm_motor.dc(arm_power)

        event = in_file.read(EVENT_SIZE)

    in_file.close()

if __name__ == "__main__":
    main()
