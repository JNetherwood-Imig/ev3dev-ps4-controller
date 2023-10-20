#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch

import struct

# Declare motors 
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
arm_motor = Motor(Port.C)
drive = 0
steer = 0
arm = 0

# A helper function for converting stick values (0 - 255)
# to more usable numbers (-100 - 100)
def scale(val, src, dst):
    '''
    Scale the given value from the scale of src to the scale of dst.
 
    val: float or int
    src: tuple
    dst: tuple
 
    example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
    '''
    return (float(val-src[0]) / (src[1]-src[0])) * (dst[1]-dst[0])+dst[0]


# Open the Gamepad event file:
infile_path = "/dev/input/event4"

# open file in binary mode
in_file = open(infile_path, "rb")

# Read from the file
FORMAT = 'llHHI'    
EVENT_SIZE = struct.calcsize(FORMAT)
event = in_file.read(EVENT_SIZE)

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
            # do something
        if code == 310 and value == 0: # L1 released
            # do something else
        # for a full list of input codes, check out https://github.com/codeadamca/ev3-python-ps4
        
    # Set motor voltages. 
    left_motor.dc(drive - steer)
    right_motor.dc(drive + steer)
    arm_motor.dc(arm)

    # Finally, read another event
    event = in_file.read(EVENT_SIZE)

in_file.close()