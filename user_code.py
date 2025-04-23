import controller_callbacks as cb
import utils

from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop)

# Configure motor ports
left_motor_port: Port = Port.A
right_motor_port: Port = Port.B
arm_motor_port: Port = Port.C

# If one of your motors is faster than the other, you can slow it down a bit here
left_motor_sensitivity: float = 1.0
right_motor_sensitivity: float = 1.0
arm_motor_sensitivity: float = 0.25

# Declare which buttons to use to start auto code and stop the robot
# A full list of button codes can be found in definitions.py
auto_button: int = utils.ButtonCode.CIRCLE
stop_button: int = utils.ButtonCode.SQUARE
disable_stop_button: bool = False

# Misc options
reverse_motor_direction: bool = False
disable_arm_motor: bool = False
use_tank_drive: bool = False
controller_deadzone: float = 0.0

# Example controller callback
# This makes a function called example that prints 'Hello, world!'
# and will be run every time the triangle button is pressed
def example():
    print("Hello, world!")

cb.register_on_press_callback(utils.ButtonCode.TRIANGLE, example)

# Declare important variables
left_motor: Motor = None
right_motor: Motor = None
arm_motor: Motor = None
drivebase: DriveBase = None

# This function will be run once when the program starts up
def on_init() -> None:
    utils.init_motors()

    global drivebase
    drivebase = DriveBase(
        left_motor,
        right_motor,
        wheel_diameter=55,
        axle_track=121) # distance betweed wheels, make sure it is accurate

# This function will be run when you press the auto button as defined above
def auto() -> None:
	drivebase.straight(500) # Drives for 300mm
	arm_motor.run_angle(500, -90, then=Stop.BRAKE) # Turn the arm motor 90 degrees ccw
	drivebase.straight(-500) # Drive backward 300mm
	arm_motor.run_angle(500, 90, then=Stop.BRAKE) # Turn the arm motor 90 degrees cw
