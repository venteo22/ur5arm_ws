"""
********************************************************************************
RoboticsUB-TCP_Endowrist_from_IMU.py - Control based on a IMU.
Copyright (C) 2020  Albert Álvarez-Carulla
Repository: https://github.com/Albert-Alvarez/roboticsub-imu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
********************************************************************************
"""

import serial
import time
import math

# RoboDK API: import the robolink library (bridge with RoboDK)
from robolink import *
# Robot toolbox: import the robodk library (robotics toolbox)
from robodk import *
# Import tkinter
from tkinter import *
import numpy as np
 


# Variables definition
# TCP end-effector respect the Flange
X=0
Y=-60
Z=320

i=0

# When rpy_or_quat == False, the quaternion function will be computed. when it is true, the RPY function will be computed
rpy_or_quat = False


# Lets bring some time to the system to stablish the connetction
time.sleep(2)

# Establish a link with the simulator
RDK = Robolink()

# ------------------------------------------------------------------------------
# Simulator setup
# ------------------------------------------------------------------------------

# Retrieve all items (object in the robodk tree)
# Define the "robot" variable with our robot (UR5e)
robot = RDK.Item ('UR5e')

# Define the "tcp" variable with the TCP of Endowrist needle
tcp_tool = RDK.Item('TCP_Endowrist')

# Performs a quick check to validate items defined
if robot.Valid():
    print('Robot selected: ' + robot.Name())
if tcp_tool.Valid():
    print('Tool selected: ' + tcp_tool.Name())

# Robot Flange with respect to UR5e base Frame
print ('Robot POSE is: ' + repr(robot.Pose()))
# Tool frame with respect to Robot Flange
print ('Robot POSE is: ' + repr(robot.PoseTool()))
# Tool frame with respect to Tool frame
print ('TCP pose is: ' + repr(tcp_tool.Pose()))

# ------------------------------------------------------------------------------
#  Establish the connection on a specific port (COM6)
arduino = serial.Serial("COM6", 115200, timeout=1)
# Create a new window
window = tkinter.Tk()
window.geometry("500x200")


# Close the window when calling this function
def onClose():
    window.destroy()
    quit(0)

# Changing the rpy_or_quat value to the contrary value (so that it computes the other function)
def change_to_rpy_or_quat():
    global rpy_or_quat
    if rpy_or_quat == True:
        rpy_or_quat = False        
    else:
        rpy_or_quat = True


        

# Set the window title 
window_title = 'RPY, Quaternion and torque values'
window.title(window_title)

# Delete the window when we close it
window.protocol("WM_DELETE_WINDOW", onClose)

# Define a button which will change rpy to quat / quat to rpy
button1 = Button(window, text='RPY or QUAT', command=lambda *args: change_to_rpy_or_quat())
button1.grid(row = 6, column = 1)

# Define the tiltle of the window
title = Label(window, text = " ")
title.grid(row = 0, column = 1)

# Define the different labels where the rpy and the quaternion values will be shown
a = Label(window, text = " ")
a.grid(row = 1, column = 0)
b = Label(window,text = " ")
b.grid(row = 1, column = 2)
c = Label(window, text = " ")
c.grid(row = 2, column = 0)
d = Label(window, text = " ")
d.grid(row = 2, column = 2)
e = Label(window, text = " ")
e.grid(row = 3, column = 0)
f = Label(window, text = " ")
f.grid(row = 3, column = 2)
g = Label(window, text = " ")
g.grid(row = 4, column = 0)
h = Label(window, text = " ")
h.grid(row = 4, column = 2)
i1 = Label(window, text = " ")
i1.grid(row = 5, column = 0)
j = Label(window, text=" ")
j.grid(row = 5, column = 2)


try:
    while True:
        # if the variable is true, it will obtain the rpy and torque values from arduino
        if rpy_or_quat == True:
            
            # Requesting data to Ardino (command A)
            arduino.write(b'A')

            # Storing received data
            roll_str = arduino.readline().strip()
            pitch_str = arduino.readline().strip()
            yaw_str = arduino.readline().strip()
            torque_str = arduino.readline().strip()

            # Convert variable values from string to float
            roll = float(roll_str)
            pitch = float(pitch_str)
            yaw = float(yaw_str)
            torque = float(torque_str)

            # Convert from degrees to radians R,P,Y angles
            R = math.radians(roll)
            P = math.radians(pitch)
            W = math.radians(yaw)
            
            # Calculate the POSE matrix (UR)
            pose_matrix = transl([X, W, Z])*rotx(pi)*rotx(-R)*roty(-P)*rotz(-W)
            tcp_tool_pose = tcp_tool.setPoseTool(pose_matrix)

            # Values will be shown in the tkinter window
            print([R,P,W],torque)
            a.config( text ="R = ")
            b.config( text = np.around(R, decimals = 3))
            c.config( text ="P = ")
            d.config( text = np.around(P, decimals = 3))
            e.config( text ="Y = ")
            f.config( text = np.around(W,decimals = 3))
            g.config( text ="torque = ")
            h.config( text = np.around(torque,decimals = 3))
            i1.config( text =" ")
            j.config( text =" ")
            button1.config( text ="View quaternions")
            title.config( text ="RPY and Torque")
            
            # updates on the window labels will be made every 2 values
            i = i + 1
            if (i % 2 == 0):
                window.update()        
        # If the variable is false, it will obtain the quaternion and torque values from arduino
        else:

            arduino.write(b'B')

            # Quaternion
            q1_str = arduino.readline().strip()
            q2_str = arduino.readline().strip()
            q3_str = arduino.readline().strip()
            q4_str = arduino.readline().strip()
            torque_str = arduino.readline().strip()

            # Convert variable values from string to float
            q1 = float(q1_str)
            q2 = float(q2_str)
            q3 = float(q3_str)
            q4 = float(q4_str)
            torque = float(torque_str)

            # Values will be shown in the tkiinter window
            print([q1,q2,q3,q4],torque)
            a.config( text ='q1 = ')
            b.config( text = np.around(q1, decimals = 3))
            c.config( text ="q2 = ")
            d.config( text = np.around(q2,decimals = 3))
            e.config( text ="q3 = ")
            f.config( text = np.around(q3,decimals = 3))
            g.config( text ="q4 = ")
            h.config( text = np.around(q4,decimals = 3))
            i1.config( text ="torque = ")
            j.config( text = np.around(torque,decimals = 3))
            button1.config( text ="View RPY")
            title.config( text ="Quaternions and Torque")
            
            # updates on the window labels will be made every 2 values
            i = i + 1
            if (i % 2 == 0):
                window.update()


except KeyboardInterrupt:
    print("Communication stopped.")
    pass

# ------------------------------------------------------------------------------
# Disconnect Arduino
# ------------------------------------------------------------------------------
print("Disconnecting Arduino...")
arduino.close()
