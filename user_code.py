####################################################
# WARNING: This is an unstable development branch. #
# All new features are first implemented here,     #
# meaning that breaking changes are possible.      #
# Unless you need any of the unstable features,    #
# it is recommended that you use the main branch.  #
####################################################

from controller_callbacks import *
from definitions import ButtonCode

from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop)
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font

from time import sleep

# Utilities, do not touch
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

def init_motors():
    global left_motor, right_motor, arm_motor
    try:
        left_motor = Motor(left_motor_port)
        right_motor = Motor(right_motor_port)
        arm_motor = Motor(arm_motor_port)
    except:
        print("Error: bad port configuration")
        ev3: EV3Brick = EV3Brick()
        ev3.screen.clear()
        ev3.screen.set_font(Font(size=14))
        ev3.screen.print("Failed to initialize motors")
        ev3.screen.print("Expected port configuration:")
        ev3.screen.print("Left motor:", get_port_string(left_motor_port))
        ev3.screen.print("Right motor:", get_port_string(right_motor_port))
        ev3.screen.print("Arm motor:", get_port_string(arm_motor_port))
        sleep(15)
        exit(1)

# Declare motors 
# DO NOT CHANGE THE VARIABLE NAMES, only the ports, such that they match your robot configuration
left_motor_port = Port.A
right_motor_port = Port.B
arm_motor_port = Port.C

left_motor: Motor = None
right_motor: Motor = None
arm_motor: Motor = None
init_motors()

# Declare which buttons to use to start auto code and stop the robot
# A full list of button codes can be found in definitions.py
auto_button: int = ButtonCode.CIRCLE
stop_button: int = ButtonCode.SQUARE
disable_stop_button: bool = False # For competition, you probably want to disable the stop button to prevent accidentally terminating your code
reverse_motor_direction: bool = False
disable_arm_motor: bool = False

# If you are experiencing controller drift, increase this to 0.1 or 0.2
controller_deadzone: float = 0.0

# If one of your motors is faster than the other, you can slow it down a bit here
left_motor_sensitivity: float = 1.0
right_motor_sensitivity: float = 1.0
arm_motor_sensitivity: float = 0.25

# Define drivebase
drivebase: DriveBase = DriveBase(
	left_motor,
	right_motor,
	wheel_diameter=55,
	axle_track=121) # distance betweed wheels. adjust if the robot is not turning the expected amount while in auto

# The default settings which print out at the beginning of the program are about 40% of the maximum values
# To make your drivebase faster, use 'drivebase.settings(xx, xx, xx, xx)', where the arguments are
# straight speed, straight acceleration, turn rate, turn acceleration
# To avoid pybricks crashing, keep the parameters within a reasonable range
print("Default drivebase settings are:", str(drivebase.settings()))

# This function will be run once when the program starts up
def on_init() -> None:
    pass

# This function will be run when you press the auto button as defined above
# There is little limitation on what this function can do, so if you want, you could make it use a distance sensor
# You are not limited to driving instructions
def auto() -> None:
	drivebase.straight(500) # Drives for 300mm
	arm_motor.run_angle(500, -90, then=Stop.BRAKE) # Turn the arm motor 90 degrees ccw
	drivebase.straight(-500) # Drive backward 300mm
	arm_motor.run_angle(500, 90, then=Stop.BRAKE) # Turn the arm motor 90 degrees cw

