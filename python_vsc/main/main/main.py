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
midium_motor = Motor(Port.B)
touch_sensor = TouchSensor(Port.S2)
color_sensor = ColorSensor(Port.S3)


# Write your program here.
ev3.speaker.beep()

# initialize midium_motor
midium_motor.run_until_stalled(120,duty_limit=50)
midium_motor.reset_angle(0)

while True:
    if Button.CENTER in ev3.buttons.pressed():
        break

wait(1000

while True:
    large_motor.run(-50)
    while Ture:
        if touch_sensor.pressed():
            large_motor.Stop()
            break
    color = color_sensor.color()
    if color == color.RED:
        ev3.speaker.say('red')
        ev3.screen.print('RED')
        large_motor.run_angle(50,0)
        midium_motor.run_target(50,-180,Stop.HOLD)
        #midium_motor.reset_angle(0)
        midium_motor.run_target(50,180,Stop.HOLD)
        ev3.screen.clear
        wait(500)
    else if color == color.YELLOW:
        ev3.speaker.say('yellow')
        ev3.screen.print('YELLOW')
        large_motor.run_angle(50,180)
        midium_motor.run_target(50,-180,Stop.Hold)
        midium_motor.run_target(50,180,Stop.Hold)
        ev3.screen.clear
        wait(500)
    else if color == color.GREEN:
        ev3.speaker.say('green')
        ev3.screen.print('GREEEN')
        large_motor.run_angle(50,380)
        midium_motor.run_target(50,-180,Stop.Hold)
        midium_motor.run_target(50,180,Stop.Hold)
        ev3.screen.clear
        wait(500)
    else
        ev3.speaker.say('blue')
        ev3.screen.print('BLUE')
        large_motor.run_angle(50,540)
        midium_motor.run_target(50,-180,Stop.Hold)
        midium_motor.run_target(50,180,Stop.Hold)
        ev3.screen.clear
        wait(500)

"""
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
largeMotor = Motor(Port.A)
midMotor = Motor(Port.B)
touchSensor = TouchSensor(Port.S2)
colorSensor = ColorSensor(Port.S3)
old = 1

# Write your program here.
ev3.speaker.beep()

midMotor.run_until_stalled(120, duty_limit=50)
midMotor.reset_angle(0)

while True:
    if Button.CENTER in ev3.buttons.pressed():
        break
    wait(1000)
    largeMotor.run(-360)

    if touchSensor.pressed():
        largeMotor.stop()
        break


while True:
    color = colorSensor.color()
    print(color, old)

    if color == Color.RED:
        ev3.speaker.say('red')
        ev3.screen.print('RED')
        largeMotor.run_angle(360, (4-old)*160)
        midMotor.run_angle(200, -180, Stop.HOLD)
        wait(500)
        midMotor.run_angle(200, 180, Stop.HOLD)
        old = 4
    elif color == Color.YELLOW:
        ev3.speaker.say('yellow')
        ev3.screen.print('YELLOW')
        largeMotor.run_angle(360, (3-old)*160)
        midMotor.run_angle(200, -180, Stop.HOLD)
        wait(500)
        midMotor.run_angle(200, 180, Stop.HOLD)
        old = 3 
    elif color == Color.GREEN:
        ev3.speaker.say('green')
        ev3.screen.print('GREEN')
        largeMotor.run_angle(360, (2-old)*160)
        midMotor.run_angle(200, -180, Stop.HOLD)
        wait(500)
        midMotor.run_angle(200, 180, Stop.HOLD)
        old = 2 
    elif color == Color.BLUE:
        ev3.speaker.say('blue')
        ev3.screen.print('BLUE')
        largeMotor.run_angle(360, (1-old)*160)
        midMotor.run_angle(200, -180, Stop.HOLD)
        wait(500)
        midMotor.run_angle(200, 180, Stop.HOLD)
        old = 1

    wait(1000)
    ev3.screen.clear()

"""
for i in range(4):
    angle = i*160
    largeMotor.run_angle(180, angle, Stop.HOLD)
    ev3.speaker.say('Good')
    wait(1000)
"""
"""