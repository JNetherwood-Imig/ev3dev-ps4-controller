#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop, Direction, Button)
from pybricks.tools import wait

from auto import (auto, drivebase, auto_button)
import struct
import io
import usys
from sys import exit

print("Implementation: " + str(usys.implementation))
print("Version: " + str(usys.version))

def scale(source, source_range, target_range):
    return (float(source-source_range[0]) / (source_range[1]-source_range[0])) * (target_range[1]-target_range[0])+target_range[0]

DATA_FORMAT = 'llHHI'    
EVENT_SIZE = struct.calcsize(DATA_FORMAT)

def try_infile(file_num):
    infile_path = "/dev/input/event" + str(file_num)

    global in_file
    try:
        in_file = open(infile_path, "rb")
        for i in range(25):
            (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(DATA_FORMAT, in_file.read(EVENT_SIZE))
            # Check if values are unreasonably large
            # This suggests that the open file is incorrect
            if ev_type == 3 and code == 1 and (value > 256 or value < -256):
                return False
        print("Controller connected!")
        print("Input file is ", infile_path)
        return True
    except:
        return False

# Test all files from /dev/input/event3 to event5
file_nums = [ 3, 4, 5 ]
success = False
for file_num in file_nums:
    # If the try infile function returns True
    # then the expression evaluates to true and the loop breaks at the current (correct) file
    if try_infile(file_num):
        success = True
        break

if not success:
    print("Error accessing controller. Make sure your controller is turned on and connected.")
    exit()

drive_speed = 0
turn_rate = 0
arm_power = 0

while True:
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(DATA_FORMAT, in_file.read(EVENT_SIZE))
    
    # Read analog stick values    
    if ev_type == 3: # Analog stick or trigger
        if code == 1: # Left stick y axis
            drive_speed = scale(value, (0,255), (100,-100))
        if code == 3: # Right stick x axis
            turn_rate = scale(value, (0,255), (100, -100))
        if code == 2: # Left trigger axis
            arm_power = value / 3
        if code == 5: # Left trigger axis
            arm_power = -value / 3
    if ev_type == 1: # Button
        if code == auto_button and value == 1:
            auto()
            
    drivebase.drive(drive_speed, turn_rate, arm_power)
