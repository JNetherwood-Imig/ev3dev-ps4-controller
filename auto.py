from drivebase import Drivebase
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

########
# Auto #
########

# Declare motors 
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
arm_motor = Motor(Port.A)

# Define drivebase
drivebase = Drivebase(
    left_motor,         # left motor
    right_motor,        # right motor
    arm_motor,          # arm motor
    55,                 # wheel diameter (mm)
    121)                # axle track (mm)

def auto():
    drivebase.move_distance(300, 500) # Drives for 300mm at a speed of 500
    drivebase.lower_arm(reversed=False)
    drivebase.move_distance(-300, 500) # Drive backward 300mm at a speed of 500
    drivebase.raise_arm(reversed=False)