#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
large_motor = Motor(Port.A)
touch_sensor = TouchSensor(Port.S2)


# Write your program here.
ev3.speaker.beep()

for i in range(4):
    large_motor.run(-50)
    while Ture:
        if touch_sensor.pressed():
            large_motor.Stop()
    angle = i*160
    large_motor.run_angle(50,angle,Stop.HOLD)
    ev3.speak.say('Good')
    wait(1000)
