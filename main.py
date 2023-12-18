#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color)
from pybricks.tools import wait, StopWatch

import struct

ARM = 1
INTAKE = 2

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

########
# Auto #
########

# Specify ARM or INTAKE depending on which you are using
robot_type = ARM

def auto_arm():
    # Run both motors for 2 seconds
    left_motor.dc(100)
    right_motor.dc(100)
    wait(2000)
    # Stop both motors
    left_motor.brake()
    right_motor.brake()
    # Rotate arm motor 90 degrees
    arm_motor.dc(-50)
    wait(500)
    arm_motor.stop()
    # Drive backwards for 2 seconds
    left_motor.dc(-100)
    right_motor.dc(-100)
    wait(2000)
    # Stop both motors
    left_motor.brake()
    right_motor.brake()
    # Rotate arm motor 90 degrees
    arm_motor.dc(50)
    wait(500)
    arm_motor.stop()

def auto_intake():
    # Start intake
    arm_motor.dc(100)
    # Run both motors for 2.5 seconds
    left_motor.dc(100)
    right_motor.dc(100)
    wait(2500)
    # Stop both motors
    left_motor.brake()
    right_motor.brake()
    # Wait 0.5 seconds while the intake picks up balls
    wait(500)
    # Drive backwards for 2.5 seconds
    left_motor.dc(-100)
    left_motor.dc(-100)
    wait(2500)
    # Stop both motors
    left_motor.stop()
    right_motor.stop()
    # Stop intake
    arm_motor.stop()

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

try:
    in_file = open(infile_path, "rb")
    controller_connected = True
except:
    print("Error accessing controller. Make sure your controller is turned on and connected.")
    controller_connected = False


# Read from the file
FORMAT = 'llHHI'    
EVENT_SIZE = struct.calcsize(FORMAT)

#############
# Main loop #
#############

while controller_connected:
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
        if code == 305 and value == 1:
            if robot_type == ARM:
                auto_arm()
            elif robot_type == INTAKE:
                auto_intake()
            else:
                print("Invalid robot type. Please specify either ARM or INTAKE")
        
        # Use square button to stop code (useful when testing)
        # if code == 308 and value == 1:
        #     print("Stopping")
        #     break
            
    # Set motor voltages. 
    left_motor.dc(DRIVE_DIRECTION * drive - steer)
    right_motor.dc(DRIVE_DIRECTION * drive + steer)
    arm_motor.dc(ARM_DIRECTION * arm)

if controller_connected:
    in_file.close()
