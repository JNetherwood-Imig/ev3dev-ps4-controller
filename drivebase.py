from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop, Direction)
from pybricks.tools import wait

from math import pi

# Stall check functions are used to allow the program to continue running
# if a motor were to stall
# rather than just blocking the program from running

# Function to run a motor a specific number of degrees
# unless it stalls, in which case it will simply move on in the program
def run_angle_until_stalled(motor, speed, angle):
    motor.run_angle(speed, angle, wait=False)
    while not motor.done():
        # Motor stalled
        if motor.stalled():
            motor.stop()
            break

# Check if the drivebase has stalled
# and break when either the instruction is complete
# or if a stall is detected       
def check_drivebase_for_stall(left_motor, right_motor):
    while not left_motor.done() and not right_motor.done():
        if left_motor.stalled() or right_motor.stalled():
            left_motor.stop()
            right_motor.stop()
            break

# Creating the drivebase class
class Drivebase:
    
    # Specifying input values when creating the drivebase
    def __init__(self, left_motor, right_motor, arm_motor, wheel_diameter, axle_track):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.arm_motor = arm_motor
        self.wheel_diamater = wheel_diameter
        self.wheel_circumference = wheel_diameter * pi
        self.axle_track = axle_track
        
    # Function to simply make the drivebase drive forwards at a given speed
    # until the stop() function is called
    def move(self, speed):
        self.left_motor.run(speed)
        self.right_motor.run(speed)
        
    # Makes the drivebase spin in a circle at a given speed until stop() is called
    def turn(self, speed):
        self.left_motor.run(speed)
        self.right_motor.run(-speed)
        
    # Drive the drivebase a specific distance forward at a specific speed
    def move_distance(self, distance, speed):
        degrees = distance / self.wheel_circumference * 360
        self.left_motor.run_angle(speed, degrees, wait=False)
        self.right_motor.run_angle(speed, degrees, wait=False)
        check_drivebase_for_stall(self.left_motor, self.right_motor)
    
    # Turn the drivebase a specific number of degrees at a designated speed
    def turn_degrees(self, speed, degrees):
        motor_degrees = (self.axle_track * pi / (360 / degrees)) / self.wheel_circumference * 360
        self.left_motor.run_angle(speed, motor_degrees, wait=False)
        self.right_motor.run_angle(speed, -motor_degrees, wait=False)
        check_drivebase_for_stall(self.left_motor, self.right_motor)
  
    # Stop the drivebase
    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        
    # Start the intake for an intake based robot
    def start_intake(self, reversed):
        self.arm_motor.dc(100 if reversed == False else -100)
     
    # Stop the intake   
    def stop_intake(self):
        self.arm_motor.stop()
    
    # Raise arm (might need to be tweaked to use correct rotation angle)
    def raise_arm(self, reversed):
        self.arm_motor.run_until_stalled(200 if reversed == False else -200,
                                         then=Stop.COAST,
                                         duty_limit=None)
    
    # Lower arm (same value might need to be changed)
    def lower_arm(self, reversed):
        self.arm_motor.run_until_stalled(-200 if reversed == False else 200,
                                         then=Stop.COAST,
                                         duty_limit=None)
    
    # Drive the drivebase using controller inputs
    def drive(self, drive_speed, turn_speed, arm_power):
        self.left_motor.dc(drive_speed - turn_speed)
        self.right_motor.dc(drive_speed + turn_speed)
        self.arm_motor.dc(arm_power)
