from drivebase import Drivebase
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

########
# Auto #
########

# Declare motors 
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
arm_motor = Motor(Port.C)

# Declare which button to use to start auto code
# a full list of button codes is available in the github README
auto_button = 305 # Circle button

# Define drivebase
drivebase = Drivebase(
	left_motor,	 # left motor
	right_motor, # right motor
	arm_motor,   # arm motor
	55,          # wheel diameter (mm)
	121)         # axle track (mm)

# Auto function
# place all auto code in this function
def auto():
	drivebase.move_distance(300, 500) # Drives for 300mm at a speed of 500
	drivebase.lower_arm(reversed=False)
	drivebase.move_distance(-300, 500) # Drive backward 300mm at a speed of 500
	drivebase.raise_arm(reversed=False)