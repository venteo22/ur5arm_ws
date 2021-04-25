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
from tkinter import *


# RoboDK API: import the robolink library (bridge with RoboDK)
from robolink import *
# Robot toolbox: import the robodk library (robotics toolbox)
from robodk import *

# Variables definition
# TCP end-effector respect the Flange
X=0
Y=-60
Z=320
PORT="COM9"


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
# UI TKinter
# Generate the main window
root = Tk()
root.title("Program settings")
#imagen = PhotoImage(file="UR5e.gif")
#Label(root, image=imagen, bd=30).pack()

# Define a label and entry text for the different parameters
entry_port = StringVar()
entry_port.set(PORT)
Label(root, text="COM port: ").pack()
Entry(root, textvariable=entry_port).pack()

Label(root, text="").pack()  # Separador

PORT=entry_port.get()

arduino = serial.Serial(PORT, 115200, timeout=1)

#Function to be able to generate the button to change to rpw angles
def rpw():
    global rpw_quaternion
    print("You have choosen rpw")
    rpw_quaternion = "rpw"
    
def quaternion():
    global rpw_quaternion
    print("You have choosen quaternions")
    rpw_quaternion = "q"

#Button's definition. 
rpw_button = Button(root, text="RPW", command = rpw, relief='raised')
rpw_button.pack()
quaternion_button = Button(root, text="QUATERNIONS", command = quaternion, relief='raised')
quaternion_button.pack()

# Label where values will be printed. The text will be defined lately.
rpw_values=Label(root, text="RPY values: ")
rpw_values.pack()

quaternion_values=Label(root, text="Quaternion values: ")
quaternion_values.pack()

# Visualitzar en grid
#window.title("RPY angles")
#tk.Label(window,text="R: ").grid(row = 0,column=0)
#tk.Label(window,text="P: ").grid(row = 1,column=0)
#tk.Label(window,text="Y: ").grid(row = 2,column=0)
#tk.Label(window,text="Torque: ").grid(row = 3,column=0)
#tk.Label(window,text=str(R)).grid(row = 0,column=1)
#tk.Label(window,text=str(P)).grid(row = 1,column=1)
#tk.Label(window,text=str(W)).grid(row = 2,column=1)
#tk.Label(window,text=str(torque)).grid(row = 3,column=1) 

def Execute():
    # Run the main program once all the global variables have been set
    # Establish the connection on a specific port (COM3)
    global rpw_quaternion
    while True:
        if rpw_quaternion=="rpw":
            # Requesting data to Ardino (command A)
            missatge="A"
            arduino.write(b'A')

            # Storing received data
            roll_str = arduino.readline().strip()
            pitch_str = arduino.readline().strip()
            yaw_str = arduino.readline().strip()
            torque_str = arduino.readline().strip()

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
            
            #Firstly I have defined the text of the label with their respective values. 
            rpw_print=('ROLL = ', roll, 'PITCH = ', pitch, 'YAW = ', yaw, 'Torque = ', torque)
            rpw_values.config(text=rpw_print) #.config() is used to extract values to the function.
            root.update() #.update() to rewrite over the previous line.

        elif rpw_quaternion=="q": 
            # Requesting data to Ardino (command B)
            missatge="B"
            arduino.write(b'B')

            q1_str = arduino.readline().strip()
            q2_str = arduino.readline().strip()
            q3_str = arduino.readline().strip()
            q4_str = arduino.readline().strip()
            torque_str = arduino.readline().strip()

            print(q1_str, q2_str, q3_str, q4_str, torque_str)

            # Convert variable values from string to float
            q1 = float(q1_str)
            q2 = float(q2_str)
            q3 = float(q3_str)
            q4 = float(q4_str)
            torque = float(torque_str)

            # Calculate the POSE matrix (UR)
            pose_matrix = transl(X,Y,Z)*rotx(pi)*quaternion_2_pose([q1, q2, q3, q4])

            #Firstly I have defined the text of the label with their respective values. 
            quaternion_print=('Q1 = ', q1, 'Q2 = ', q2, 'Q3 = ', q3, 'Q4', q4, 'Torque = ', torque)
            quaternion_values.config(text=quaternion_print)
            root.update()

        else:
            pass
        
    tcp_tool_pose = tcp_tool.setPoseTool(pose_matrix)
        
def StopProg():
    print("Communication stopped.")
    # ------------------------------------------------------------------------------
    # Disconnect Arduino
    # ------------------------------------------------------------------------------
    print("Disconnecting Arduino...")
    arduino.close()

Label(root, text="").pack()  # Separador
Button(root, text='Simulate', command=Execute).pack()
Label(root, text="").pack()  # Separador
Button(root, text='Stop Arduino', command=StopProg).pack()
Label(root, text="").pack()  # Separador
Button(root, text='Stop UI', command=root.destroy).pack()
Label(root, text="").pack()  # Separador

# Important to display the graphical user interface
root.mainloop()