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
import tkinter as tk


# RoboDK API: import the robolink library (bridge with RoboDK)
from robolink import *
# Robot toolbox: import the robodk library (robotics toolbox)
from robodk import *

# Variables definition
# TCP end-effector respect the Flange
X=0
Y=-60
Z=320


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
#  Establish the connection on a specific port (COM5)
arduino = serial.Serial("COM6", 115200, timeout=1)

window = tk.Tk()
window.geometry('200x200')
etiqueta = tk.Label(window, text = "")
etiqueta.pack()

def roll_pitch_yaw():
    global etiqueta
    try:
        while True:
        
            # Requesting data to Arduino (command A)
            arduino.write(b'A')

            # Storing received data
            roll_str = arduino.readline().strip()
            # roll_str = str(90)
            pitch_str = arduino.readline().strip()
            # pitch_str = str(180)
            yaw_str = arduino.readline().strip()
            # yaw_str = str(0)
            torque_str = arduino.readline().strip()
            # torque_str = str(90)

            print(roll_str, pitch_str, yaw_str,torque_str)

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
            pose_matrix = transl([X, Y, Z])*rotx(pi)*rotx(-R)*roty(-P)*rotz(-W)
            print ('The POSE matrix with RPY is: ' + repr(pose_matrix))
            tcp_tool_pose = tcp_tool.setPoseTool(pose_matrix)
            
            var_1 = ('r = ',R, '\n', 'p = ',P,'\n','y = ',W,'\n','Torque = ',torque)
            etiqueta.config(text = var_1)
            window.update()
            

    except KeyboardInterrupt:
        print("Communication stopped.")
        pass


def quaternion():
    global etiqueta
    try:
        while True:
            # Requesting data to Arduino (command B)
            arduino.write(b'B')

            # Storing data recieved
            quat1 = arduino.readline().strip()
            # quat1 = str(0) 
            quat2 = arduino.readline().strip()
            # quat2 = str(0.5)
            quat3 = arduino.readline().strip()
            # quat3 = str(0.707)
            quat4 = arduino.readline().strip()
            # quat4 = str(0)
            torque_str = arduino.readline().strip()
            # torque_str = str(90)

            print(quat1, quat2, quat3, quat4, torque_str)

            # Convert variable values from string to float
            q1 = float(quat1)
            q2 = float(quat2)
            q3 = float(quat3)
            q4 = float(quat4)
            torque = float(torque_str)
            

            # Calculate the POSE matrix (UR)
            pose_matrix = transl(X,Y,Z)*rotx(pi)*quaternion_2_pose([q1, q2, q3, q4]) # Ara caldrà calibrar!
            print ('The POSE matrix with quaternions is: ' + repr(pose_matrix))

            # Define the Endowrist TCP POSE in the first suture point (1st point)
            # by first point matrix POSE:
            tcp_tool_pose = tcp_tool.setPoseTool(pose_matrix)
            print ('Tool TCP pose with quaternions is: ' + repr([q1,q2,q3,q4]) + '\n')

            var_2 = ("q1 = ",q1,'\n',"q2 = ",q2,'\n',"q3 = ",q3,'\n','q4 = ',q4,'\n','Torque = ',torque)
            etiqueta.config(text = var_2)
            window.update()

    except KeyboardInterrupt:
        print("Communication stopped.")
        pass


choice_1 = tk.Button(window, text = 'RPY', command=roll_pitch_yaw)
choice_2 = tk.Button(window, text = 'Quaternions', command=quaternion)

choice_1.pack()
choice_2.pack()
roll_pitch_yaw()




# ------------------------------------------------------------------------------
# Disconnect Arduino
# ------------------------------------------------------------------------------
print("Disconnecting Arduino...")
arduino.close()

