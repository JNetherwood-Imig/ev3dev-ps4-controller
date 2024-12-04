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

# Declare motors 
# DO NOT CHANGE THE VARIABLE NAMES, only the ports, such that they match your robot configuration
left_motor: Motor  = Motor(Port.A)
right_motor: Motor = Motor(Port.B)
arm_motor: Motor   = Motor(Port.C)

# Declare which buttons to use to start auto code and stop the robot
# A full list of button codes can be found in definitions.py
auto_button: int = ButtonCode.CIRCLE
stop_button: int = ButtonCode.SQUARE
disable_stop_button: bool = False # For competition, you probably want to disable the stop button to prevent accidentally terminating your code
reverse_motor_direction: bool = False
disable_arm_motor: bool = False

# If you are experiencing controller drift, increase this to 0.1 or 0.2
controller_deadzone: float = 0.0

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


############################
# EXAMPLE BUTTON CALLBACKS #
############################
'''
Declaring your own button callbacks will work as follows
# Note: all callback functions need to take an integer value as a parameter.
# If you don't need to know the event value, just name the parameter _

def on_triangle_press(_: int):
    print("Triangle button pressed.")

def on_triangle_release(_: int):
    print("Triangle button released.")

# This will be run ONCE when the triangle button is pressed
register_on_press_callback(ButtonCode.TRIANGLE, on_triangle_press)

# This will be run ONCE when the triangle button is released
register_on_release_callback(ButtonCode.TRIANGLE, on_triangle_release)
'''

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

