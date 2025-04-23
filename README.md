# Basic functionality
Most of the code will be done using the default pybricks v3.5 api
Documentation is available online, though make sure to select the documentation for pybricks 3.5, not 2.0

# Extending the code
If the basic setup does not suit your use case, the main file can be altered to work exactly as you want.
The main loop which reads events from the controller file and responds to them is located at line 76 and can be reasonably reverse-engineered.
Two basic changes are switching from arcade drive to tank drive and changing the functionality of the joysticks.
To switch to tank drive, simply go to line 84 in main, comment out the call to arcade drive, and uncomment the call to tank drive.
To change the functionality of the joysticks and triggers, find their respective places in the file and experiment with changing them.
Arcade drive joystick functions are at line 32, tank drive at line 44, and arm movement is at line 90.
