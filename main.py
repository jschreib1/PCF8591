#   To check address: sudo i2cdetect -y 1

from joystickClass import joystick
from PCF import PCF8591
import smbus
from time import sleep

while True:
  try:
    joystick(0x40)
    x = joystick.getx()
    y = joystick.gety()
    print('%s, %s'.format(x,y))
  
  except KeyboardInterrupt:
    print('shutting down joystick')