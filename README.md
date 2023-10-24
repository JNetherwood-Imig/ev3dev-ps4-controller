# Drivebase instructions
When creating the drivebase object (robot = DriveBase(...)) there are 4 input fields. The first 2 specify the motors. They can be left as default because left_motor and right_motor are defined above. However, there are 2 more vaules: wheel_diameter and axle_track. The wheel diameter should be the same for all of the ev3 kits. The axle track, however, is unique to each robot. It is very important as it determines the robot's ability to turn a specified number of degrees. The axle track is the distance between the wheels. It should be measured in mm, as precisely as possible. Some experimentation may be required for getting optimal functionality. One way to test functionality is to make the robot turn 360 degrees and see how close it is to accurate.
For instructions on programming the drivebase, see the [pybricks documentation](https://docs.pybricks.com/en/stable/robotics.html#pybricks.robotics.DriveBase).
# Controller button codes
| Event | ID | Code | Possible | Values | Description |
|-----------------------------------------------------|
| X Button	4	304	0 or 1	0 Released/1 Pressed |
| Circle Button	4	305	0 or 1	0 Released/1 Pressed |
| Triangle Burron	4	307	0 or 1	0 Released/1 Pressed |
| Square Button	4	308	0 or 1	0 Released/1 Pressed |
| Share Button	4	314	0 or 1	0 Released/1 Pressed |
| Options Button	4	315	0 or 1	0 Released/1 Pressed |
| PS Button	4	316	0 or 1	0 Released/1 Pressed |
| Left Stick Push	4	317	0 or 1	0 Released/1 Pressed |
| Right Stick Push	4	318	0 or 1	0 Released/1 Pressed |
| L1	4	310	0 or 1	0 Released/1 Pressed |
| R1	4	311	0 or 1	0 Released/1 Pressed |
| L2	4	312	0 or 1	0 Released/1 Pressed |
| R2	4	313	0 or 1	0 Released/1 Pressed |
| Left Stick Horizontal Axis	3	0	0 to 255	0 Left/127 Middle/255 Right |
| Left Stick Vertical Axis	3	1	0 to 255	0 Top/127 Middle/255 Bottom |
| L2 Axis	3	2	0 to 255	0 Released/255 Completely Pressed |
| Right Stick Horizontal Axis	3	3	0 to 255	0 Left/127 Middle/255 Right |
| Right Stick Vertical Axis	3	4	0 to 255	0 Top/127 Middle/255 Bottom |
| R2 Axis	3	4	0 to 255	0 Left/127 Middle/255 Right |
| Directional Pad Horizontal	3	16	-1, 0 or 1	-1 Right/0 Released, 1 Left |
| Directional Pad Vertical	3	17	-1, 0 or 1	-1 Right/0 Released, 1 Left |
# Sources and more info
To see the original code, or a more detailed guide for connecting the controllers, see [antonsmindstorms.com](https://www.antonsmindstorms.com/2020/02/14/how-to-connect-a-ps4-dualshock-4-controller-to-your-mindstorms-ev3-brick-with-bluetooth/).
More information about controller button codes is abailable [here](https://github.com/codeadamca/ev3-python-ps4#lego-mindstorms-ev3-pthon-and-a-ps4-controller).
For more info about drivebases, see [this doc](https://docs.google.com/document/d/1rpNtUZS8Aor8wrZpCycvDiGADQ6NUlJ5iaD3Y8tqpQM/edit?usp=sharing).
