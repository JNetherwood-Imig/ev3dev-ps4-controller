#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import *

import struct

DRIVE_DIRECTION = 1
ARM_DIRECTION = 1

# Declare motors 
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
arm_motor = Motor(Port.C)

# Defining variables that will store the dc values for the motors
drive = 0
steer = 0
arm = 0

# Arm speed is a value from 0-1 that is multiplied by the input value for the arm movement.
# 1 is default, but you can lower it for better control
arm_speed = 1

#############
# Drivebase #
#############

# A drivebase allows for precise and easy control of the robot while acting autonomously
# Read drivebase documentation linked in the README on github to correctly set the last value
drivebase = DriveBase(left_motor, right_motor, 55.5, 121.5)
# If the drivebase declaration line fails with "INVALID ARGUMENT" then it is a hardware issue
# Most likely a bad motor or wire

# Drivebase settings
# Arguments: straight speed: mm/s, straight acceleration: mm/s^2
# turn rate: deg/s, turn acceleration: deg/s^2

drivebase.settings(500, 1000, 100, 100)

########
# Auto #
########

# Example

drivebase.straight(500) # drive 500mm foreward
# drivebase.straight(-100) # drive 100mm backward
# drivebase.turn(degrees) # Turn the robot by a specified number of degrees.

# To make the program pause:
# wait(milliseconds)

# To raise and lower the arm, you can do something like this
# arm_motor.run_angle(speed, degrees, then=stop.HOLD, wait=True) # Runs the arm motor for a specified number of degrees

# Ex:
# Arm up
# arm_motor.run_angle(100, 90, then=stop.HOLD, wait=True)
# Arm down
# arm_motor.run_angle(100, -90, then=stop.HOLD, wait=True)

# For an intake based design, you can just constantly run a motor like this:
# arm_motor.run(speed)
# Use a negative speed to run it backwards
# When you're ready to stop it:
# arm_motor.stop()

# For further info, read the pybricks documentation linked on the github page.

# Do not remove these calls to stop()
# This is essential to allow the program to continue to the manual control section
arm_motor.stop()
drivebase.stop()

#########
# Setup #
#########

# This function scales a range of values from source_range (typically 0-255) to target_range (for instance -100-100),
# where 0 is -100, 255 is 100, and all inbetween values are scaled porportionally
# example: scale(source(0,255), (-100-100))
def scale(source, source_range, target_range):
    return (float(source-source_range[0]) / (source_range[1]-source_range[0])) * (target_range[1]-target_range[0])+target_range[0]

# Open the Gamepad event file:
infile_path = "/dev/input/event4"
in_file = open(infile_path, "rb")

# If you recieve an OS Error 2 (OSError: [Errno 2] ENOENT), then the input event file "event4" does not exist
# Make sure that the controller is connected, because the file does not exist when the controller is not connected
# If it is still broken, ssh into the robot and run:
# ls /dev/input/
# to see available input files.

# Read from the file
FORMAT = 'llHHI'    
EVENT_SIZE = struct.calcsize(FORMAT)

#############
# Main loop #
#############

while True:
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, in_file.read(EVENT_SIZE))
    
    # Read analog stick values    
    if ev_type == 3: # Stick or trigger moved
        if code == 1: # Left stick y axis
            drive = scale(value, (0,255), (100,-100)) # Scale input from 0-255 to -100-100 for the motor
        if code == 3: # Right stick x axis
            steer = scale(value, (0,255), (100, -100)) # Scale input from 0-255 to -100-100 for the motor
        if code == 2: # Left trigger axis
            arm = value / 2
        if code == 5: # Left trigger axis
            arm = -value / 2
    if ev_type == 1: # Button pressed
        if code == 310 and value == 1:
            print("L1 Pressed!")
        if code == 310 and value == 0:
            print("L1 Released")
        
    # Set motor voltages. 
    left_motor.dc(DRIVE_DIRECTION * drive - steer)
    right_motor.dc(DRIVE_DIRECTION * drive + steer)
    arm_motor.dc(ARM_DIRECTION * arm * arm_speed)

in_file.close()
