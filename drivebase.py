from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Stop, Direction)
from pybricks.tools import wait

from math import pi

def run_angle_until_stalled(motor, speed, angle):
    motor.run_angle(speed, angle, wait=False)
    while True:
        if motor.stalled():
            print("motor stalled")
            motor.stop()
            break
        elif motor.done():
            break
        
def check_stalled(motor):
    while True:
        if motor.stalled():
            print("motor stalled")
            motor.stop()
            break
        elif motor.done():
            break

class Drivebase:
    
    def __init__(self, left_motor, right_motor, arm_motor, wheel_diameter, axle_track):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.arm_motor = arm_motor
        self.wheel_diamater = wheel_diameter
        self.wheel_circumference = wheel_diameter * pi
        self.axle_track = axle_track
        
    def move(self, speed):
        self.left_motor.run(speed)
        self.right_motor.run(speed)
        
    def turn(self, speed):
        self.left_motor.run(speed)
        self.right_motor.run(-speed)
        
    def move_distance(self, distance, speed):
        degrees = distance / self.wheel_circumference * 360
        self.left_motor.run_angle(speed, degrees, wait=False)
        self.right_motor.run_angle(speed, degrees, wait=False)
        check_stalled(self.left_motor)
        
    def turn_angle(self, speed, angle):
		degrees = (self.axle_track * pi / (360 / angle)) / self.wheel_circumference * 360
		self.left_motor.run_angle(speed, degrees, wait=False)
		self.right_motor.run_angle(speed, -degrees, wait=False)
		check_stalled(self.left_motor)
        
    def start_intake(self, speed):
        self.arm_motor.dc(speed)
        
    def stop_intake(self, speed):
        self.arm_motor.stop()
        
    def raise_arm(self):
        run_angle_until_stalled(self.arm_motor, 200, 180)
        
    def lower_arm(self):
        run_angle_until_stalled(self.arm_motor, 200, -180)
        
    def drive(self, drive_speed, turn_speed, arm_power):
        self.left_motor.dc(drive_speed - turn_speed)
        self.right_motor.dc(drive_speed + turn_speed)
        self.arm_motor.dc(arm_power)
