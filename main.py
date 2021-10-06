#   To check address: sudo i2cdetect -y 1

from joystickClass import Joystick
from PCF import PCF8591
import smbus
from time import sleep

while True:
  try:
    myJoystick = Joystick(0x48)
    x = myJoystick.getx()
    y = myJoystick.gety()
    print('{:s}, {:s}'.format(str(x).rjust(5),str(y).rjust(5)))
    sleep(0.1)
  
  except KeyboardInterrupt:
    print('shutting down joystick')