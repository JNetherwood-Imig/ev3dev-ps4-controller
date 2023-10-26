#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import struct

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
robot = DriveBase(left_motor, right_motor, 55.5, 121.5)

# Drivebase settings
# Arguments: straight speed: mm/s, straight acceleration: mm/s^2, turn rate: deg/s, turn acceleration: deg/s^2
robot.settings(500, 1000, 100, 100)


########
# Auto #
########

# Example
robot.straight(2000) # drive 2000mm foreward
robot.stop()

#########
# Setup #
#########

# A helper function for converting stick values (0 - 255)
# to more usable numbers (-100 - 100)
def scale(source, source_range, target_range):
    # the function scales a range of values from source_range (typically 0-255) to target_range (for instance -100-100),
    # where 0 is -100, 255 is 100, and all inbetween values are scaled porportionally
    # example: scale(source(0,255), (-100-100))
    return (float(source-source_range[0]) / (source_range[1]-source_range[0])) * (target_range[1]-target_range[0])+target_range[0]


# Open the Gamepad event file:
infile_path = "/dev/input/event4"

# open file in binary mode
in_file = open(infile_path, "rb")

# Read from the file
FORMAT = 'llHHI'    
EVENT_SIZE = struct.calcsize(FORMAT)
event = in_file.read(EVENT_SIZE)

#############
# Main loop #
#############

while event:
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, event)
    
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
        if code == 310 and value == 1: # L1 pressed
            print("L1 Pressed!")
            # do something
        if code == 310 and value == 0: # L1 released
            # do something else
            print("L1 Released")
        
    # Set motor voltages. 
    left_motor.dc(drive - steer)
    right_motor.dc(drive + steer)
    arm_motor.dc(arm * arm_speed)

    # Finally, read another event
    event = in_file.read(EVENT_SIZE)

in_file.close()