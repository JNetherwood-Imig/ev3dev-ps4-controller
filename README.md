# Drivebase instructions
When creating the drivebase object (robot = DriveBase(...)) there are 4 input fields. The first 2 specify the motors. They can be left as default because left_motor and right_motor are defined above. However, there are 2 more vaules: wheel_diameter and axle_track. The wheel diameter should be the same for all of the ev3 kits. The axle track, however, is unique to each robot. It is very important as it determines the robot's ability to turn a specified number of degrees. The axle track is the distance between the wheels. It should be measured in mm, as precisely as possible. Some experimentation may be required for getting optimal functionality. One way to test functionality is to make the robot turn 360 degrees and see how close it is to accurate.
For instructions on programming the drivebase, see the [pybricks documentation](https://docs.pybricks.com/en/stable/robotics.html#pybricks.robotics.DriveBase).
# Controller button codes
Coming soon. For now, check the sources section.
# Sources and more info
To see the original code, or a more detailed guide for connecting the controllers, see [antonsmindstorms.com](https://www.antonsmindstorms.com/2020/02/14/how-to-connect-a-ps4-dualshock-4-controller-to-your-mindstorms-ev3-brick-with-bluetooth/).

More information about controller button codes is abailable [here](https://github.com/codeadamca/ev3-python-ps4#lego-mindstorms-ev3-pthon-and-a-ps4-controller).

For more info about drivebases, see [this doc](https://docs.google.com/document/d/1rpNtUZS8Aor8wrZpCycvDiGADQ6NUlJ5iaD3Y8tqpQM/edit?usp=sharing).
