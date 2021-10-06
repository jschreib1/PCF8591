#   To check address: sudo i2cdetect -y 1

from joystickClass import joystick
from PCF import PCF8591
import smbus
from time import sleep

print('Working')
while True:
  print("Working in the While Loop")
  try:
    joystick(0x40, 127, 127)
    x = joystick.getx()
    y = joystick.gety()
    print('%d, %d'.format(x,y))
  
  except KeyboardInterrupt:
    print('shutting down joystick')