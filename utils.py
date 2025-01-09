from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font

from time import sleep

import user_code as uc

class EventType:
    BUTTON = 1
    AXIS = 3

class ButtonEvent:
    PRESSED = 1
    RELEASED = 0

class ButtonCode:
    X = 304
    CIRCLE = 305
    TRIANGLE = 307
    SQUARE = 308
    LEFT_BUMPER = 310
    RIGHT_BUMPER = 311
    LEFT_TRIGGER = 312
    RIGHT_TRIGGER = 313
    SHARE = 314
    OPTIONS = 315
    PLAYSTATION = 316
    LEFT_STICK_PUSH = 317
    RIGHT_STICK_PUSH = 318

class AxisCode:
    LEFT_STICK_X = 0
    LEFT_STICK_Y = 1
    LEFT_TRIGGER = 2
    RIGHT_STICK_X = 3
    RIGHT_STICK_Y = 4
    RIGHT_TRIGGER = 5

def get_port_string(port: Port) -> str:
    if port == Port.A:
        return "A"
    if port == Port.B:
        return "B"
    if port == Port.C:
        return "C"
    if port == Port.D:
        return "D"

    return "Unknown"

def print_ports() -> None:
    ev3: EV3Brick = EV3Brick()
    ev3.screen.clear()
    ev3.screen.set_font(Font(size=14))
    ev3.screen.print("Failed to initialize motors")
    ev3.screen.print("Expected port configuration:")
    ev3.screen.print("Left motor:", get_port_string(uc.left_motor_port))
    ev3.screen.print("Right motor:", get_port_string(uc.right_motor_port))
    ev3.screen.print("Arm motor:", get_port_string(uc.arm_motor_port))

def init_motors() -> None:
    try:
        uc.left_motor = Motor(uc.left_motor_port)
        uc.right_motor = Motor(uc.right_motor_port)
        uc.arm_motor = Motor(uc.arm_motor_port)
    except:
        print_ports()
        sleep(15)
        exit(1)
