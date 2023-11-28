# Drivebase instructions
When creating the drivebase object (robot = DriveBase(...)) there are 4 input fields. The first 2 specify the motors. They can be left as default because left_motor and right_motor are defined above.
However, there are 2 more vaules: wheel_diameter and axle_track. The wheel diameter should be the same for all of the ev3 kits.
The axle track, however, is unique to each robot. It is very important as it determines the robot's ability to turn a specified number of degrees. The axle track is the distance between the wheels. It should be measured in mm, as precisely as possible. Some experimentation may be required for getting optimal functionality. One way to test functionality is to make the robot turn 360 degrees and see how close it is to accurate.
For instructions on programming the drivebase, see the [drivebase page](https://docs.pybricks.com/en/stable/robotics.html#pybricks.robotics.DriveBase) of the pybricks documentation.
For information about moving individual motors, see the [motors page](https://docs.pybricks.com/en/stable/pupdevices/motor.html#pybricks.pupdevices.Motor).
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
# Sources and more info
To see the original code, or a more detailed guide for connecting the controllers, see [antonsmindstorms.com](https://www.antonsmindstorms.com/2020/02/14/how-to-connect-a-ps4-dualshock-4-controller-to-your-mindstorms-ev3-brick-with-bluetooth/).

More information about controller button codes is abailable [here](https://github.com/codeadamca/ev3-python-ps4#lego-mindstorms-ev3-pthon-and-a-ps4-controller).
