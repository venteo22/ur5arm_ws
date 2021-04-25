/******************************************************************************
roboticsub-imu.ino - MPU Arduino library example
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
******************************************************************************/

#include "src/RoboticsUB.h"
#include <Servo.h>

IMU imu;
Servo servo1;

int PIN_IMU_VCC = 4;
int PIN_IMU_INT = 5;
float *rpw;           // Pointer to read RPW
float *q;             // Pointer to quaternion
char instruction = 0; // For incoming serial data
int Pin_R1 = A0;      // Analogic pin used by R1 (Servo1)
float R1 = 1.6;       // Resistance value
float torque = 0;     // Indicated as current (ampere)
float torque_int = 0;
const unsigned long period_milis = 200; //Time for torque output
unsigned long current_milis = 0;
unsigned long previous_milis = 0;
float motor_angle = 0;  // Motor angle

void setup()
{

  Serial.begin(115200);

  // Power the IMU from pin to reset
  pinMode(PIN_IMU_VCC, OUTPUT);
  digitalWrite(PIN_IMU_VCC, LOW);
  delay(100);
  digitalWrite(PIN_IMU_VCC, HIGH);
  delay(100);
  imu.Install();
  servo1.attach(9);
  
}

void loop()
{
  current_milis = millis();
  if (digitalRead(PIN_IMU_INT) == HIGH) {
    imu.ReadSensor();
    rpw = imu.GetRPW();
    q = imu.GetQuaternion();
  }

  // Angle range from 0 to 180 degrees
  if (rpw[2] <= 180 && rpw[2] >= 0)
  {
    motor_angle = rpw[2];
  }

  servo1.write(motor_angle);
  if (current_milis-previous_milis>=period_milis){
    torque=torque_int;
    torque_int=0;
    previous_milis=current_milis;
  }
  else{
  torque_int += analogRead(Pin_R1) * (3.3 / 1023.0) / R1;
  }
  if (Serial.available() > 0)
  {

    instruction = Serial.read();

    switch (instruction)
    {
    case 'A':

      Serial.println(String(rpw[0], 4));
      Serial.println(String(rpw[1], 4));
      Serial.println(String(rpw[2], 4));
      Serial.println(String(torque, 4));

      break;

    case 'B':
    
      Serial.println(String(q[0], 4));
      Serial.println(String(q[1], 4));
      Serial.println(String(q[2], 4));
      Serial.println(String(q[3], 4));
      Serial.println(String(torque, 4));
      
      break;
      
    default:
      break;
    }

    instruction = NULL;
    
  }
//Serial.println(torque); //only for test in arduino. Comment it to go to roboDK!
}
