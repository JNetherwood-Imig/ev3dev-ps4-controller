#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop, Direction, Button)
from pybricks.tools import wait

from drivebase import Drivebase
import struct
import io

# Declare motors 
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
arm_motor = Motor(Port.C)

# Defining variables that will store the dc values for the motors
drive_speed = 0
turn_rate = 0
arm_power = 0

robot_uses_intake = False

########
# Auto #
########

drivebase = Drivebase(
    left_motor,
    right_motor,
    arm_motor,
    55,
    121)

def auto(intake):
    if intake:
        drivebase.start_intake(100) # Runs the intake at a set speed from -100 to 100
    drivebase.move_distance(300, 500) # Drives for 300 mm at a speed of 500
    if not intake:
        drivebase.lower_arm()
    drivebase.move_distance(-300, 500)
    if intake:
        drivebase.stop_intake()
    else:
        drivebase.raise_arm()

#########
# Setup #
#########

# This function scales a range of values from source_range (typically 0-255) to target_range (for instance -100-100),
# where 0 is -100, 255 is 100, and all inbetween values are scaled porportionally
# example: scale(source(0,255), (-100-100))
def scale(source, source_range, target_range):
    return (float(source-source_range[0]) / (source_range[1]-source_range[0])) * (target_range[1]-target_range[0])+target_range[0]

# Open the Gamepad event file
DATA_FORMAT = 'llHHI'    
EVENT_SIZE = struct.calcsize(DATA_FORMAT)

# Function to test various files to detect the correct one for inputs
def try_infile(file_num):
    infile_path = "/dev/input/event" + str(file_num)

    global in_file
    try:
        in_file = open(infile_path, "rb")
        for i in range(100):
            (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(DATA_FORMAT, in_file.read(EVENT_SIZE))
            # Check if values are unreasonably large
            # This suggests that the open file is incorrect
            if ev_type == 3 and (value > 256 or value < -256):
                return False
        # Found correct file
        print("Controller connected!")
        print("Input file is ", infile_path)
        return True
    except:
        return False

# Test all files from /dev/input/event3 to event5
file_nums = [ 3, 4, 5 ]
success = False
for i in file_nums:
    # If the try infile function returns True
    # then the expression evaluates to true and the loop breaks at the current (correct) file
    if try_infile(i):
        success = True
        break

# If the whole process fails, print an error message and quit the program
if not success:
    print("Error accessing controller. Make sure your controller is turned on and connected.")
    quit()

#############
# Main loop #
#############

while True:
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(DATA_FORMAT, in_file.read(EVENT_SIZE))
    
    # Read analog stick values    
    if ev_type == 3: # Stick or trigger moved
        if code == 1: # Left stick y axis
            drive_speed = scale(value, (0,255), (100,-100)) # Scale input from 0-255 to -100-100 for the motor
        if code == 3: # Right stick x axis
            turn_rate = scale(value, (0,255), (100, -100)) # Scale input from 0-255 to -100-100 for the motor
        if code == 2: # Left trigger axis
            arm_power = value / 3
        if code == 5: # Left trigger axis
            arm_power = -value / 3
    if ev_type == 1: # Button pressed
        if code == 305 and value == 1:
            auto(robot_uses_intake)
            
    # Set motor voltages. 
    drivebase.drive(drive_speed, turn_rate, arm_power)

if controller_connected:
    in_file.close()
