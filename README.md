# Drivebase instructions
In the auto.py file is a drivebase object which is created near the top. This should be created with parameters that match your robot.
The wheel diameter should not need to be changed unless the wheels are modified, but the axle track is important. It represents the distance between the two weels. To get an accurate value, measure from the middle of one wheel to the middle of the other.

## Drivebase commands
   >[!NOTE]
   >The speed values are arbitrary and do not have defined units\
   >All functions are called in the form of: `drivebase_name.function_name()`

### move(speed)
Drives at a given speed until stop is called
### move_distance(distance, speed)
Drives for a given amount of millimeters at a given speed
### turn(speed)
Spins around at a given speed until stop is called
### turn_angle(angle, speed)
Turns at a given speed and stops after a given number of degrees
### stop()
Stops the robot
### start_intake()
### stop_intake()
### raise_arm()
### lower_arm()
### drive()
This function is only used the main file as it just drives the robot using the controller input

# Controller button codes
| Event                      | Code | Possible Values | Description                 |
| -------------------------- | ---- | --------------- | --------------------------- |
| X Button                   | 304 | 0 or 1           | 0 Released/1 Pressed        |
| Circle Button	             | 305 | 0 or 1	          | 0 Released/1 Pressed        |
| Triangle Button	         | 307 | 0 or 1           | 0 Released/1 Pressed        |
| Square Button	             | 308 | 0 or 1           | 0 Released/1 Pressed        |
| Share Button               | 314 | 0 or 1           | 0 Released/1 Pressed        |
| Options Button             | 315 | 0 or 1           | 0 Released/1 Pressed        |
| PS Button	                 | 316 | 0 or 1           | 0 Released/1 Pressed        |
| Left Stick Push	         | 317 | 0 or 1   	      | 0 Released/1 Pressed        |
| Right Stick Push           | 318 | 0 or 1           | 0 Released/1 Pressed        |
| L1                         | 310 | 0 or 1   	      | 0 Released/1 Pressed        |
| R1                         | 311 | 0 or 1           | 0 Released/1 Pressed        |
| L2 Binary	                 | 312 | 0 or 1           | 0 Released/1 Pressed        |
| R2 Binary                  | 313 | 0 or 1           | 0 Released/1 Pressed        |
| L2 Axis                    | 2   | 0 to 255         | 0 Released/255 Pressed      |
| R2 Axis                    | 5   | 0 to 255         | 0 Released/255 Pressed      |
| Left Stick X Axis          | 0   | 0 to 255         | 0 Left/127 Middle/255 Right |
| Left Stick Y Axis          | 1   | 0 to 255 	      | 0 Top/127 Middle/255 Bottom |
| Right Stick X Axis         | 3   | 0 to 255	      | 0 Left/127 Middle/255 Right |
| Right Stick Y Axis         | 4   | 0 to 255         | 0 Top/127 Middle/255 Bottom |
| Directional Pad Horizontal | 16  | -1, 0 or 1	      | -1 Right/0 Released, 1 Left |
| Directional Pad Vertical   | 17  | -1, 0 or 1       | -1 Right/0 Released, 1 Left |

More information about controller button codes is abailable [here](https://github.com/codeadamca/ev3-python-ps4#lego-mindstorms-ev3-pthon-and-a-ps4-controller).
