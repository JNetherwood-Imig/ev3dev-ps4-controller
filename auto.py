from definitions import ButtonCode
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop)

# Declare motors 
# DO NOT CHANGE THE VARIABLE NAMES, only the ports, such that they match your robot configuration
left_motor  = Motor(Port.A)
right_motor = Motor(Port.B)
arm_motor   = Motor(Port.C)

# Declare which buttons to use to start auto code and stop the robot
# A full list of button codes can be found in definitions.py
auto_button = ButtonCode.CIRCLE
stop_button = ButtonCode.SQUARE
disable_stop_button = False # For competition, you may want to disable the stop button to prevent accidentally terminating your code

controller_deadzone = 0.1

# Define drivebase
drivebase = DriveBase(
	left_motor,
	right_motor,
	wheel_diameter=55,
	axle_track=121) # distance betweed wheels. adjust if the robot is not turning the expected amount while in auto

print("Default drivebase settings are:", str(drivebase.settings()))
# The default settings which print out at the beginning of the program are about 40% of the maximum values
# To make your drivebase faster, use 'drivebase.settings(xx, xx, xx, xx)', where the arguments are
# straight speed, straight acceleration, turn rate, turn acceleration
# To avoid pybricks crashing, keep the parameters within a reasonable range

# This function will be run when you press the auto button as defined above
# There is little limitation on what this function can do, so if you want, you could make it use a distance sensor
# You are not limited to driving instructions
def auto():
	drivebase.straight(500) # Drives for 300mm
	arm_motor.run_angle(500, 90, then=Stop.BRAKE) # Turn the arm motor 90 degrees cw
	drivebase.straight(-500) # Drive backward 300mm
	arm_motor.run_angle(500, -90, then=Stop.BRAKE) # Turn the arm motor 90 degrees ccw

