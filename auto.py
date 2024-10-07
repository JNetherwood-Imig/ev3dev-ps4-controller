from definitions import ButtonCode
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop)

# Declare motors 
# These motors are used by other parts of the code so their names need to stay the same
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
arm_motor = Motor(Port.C)

# Declare which buttons to use to start auto code and stop the robot
auto_button = ButtonCode.CIRCLE
stop_button = ButtonCode.SQUARE

# Define drivebase
drivebase = DriveBase(
	left_motor,
	right_motor,
	wheel_diameter=55,
	axle_track=121) # distance betweed wheels. adjust if the robot is not turning the expected amount while in auto

# Auto function
# place all auto code in this function
def auto():
	drivebase.straight(500) # Drives for 300mm
	arm_motor.run_angle(500, 90, then=Stop.BRAKE)
	drivebase.straight(-500) # Drive backward 300mm
	arm_motor.run_angle(500, -90, then=Stop.BRAKE)
