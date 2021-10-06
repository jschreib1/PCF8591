#   To check address: sudo i2cdetect -y 1

from joystickClass import Joystick
from PCF import PCF8591
import smbus
from time import sleep

print('Working')
while True:
  print("Working in the While Loop")
  try:
    myJoystick = Joystick(0x48)
    x = myJoystick.getx()
    y = myJoystick.gety()
    print('{:d}, {:d}'.format(x,y))
    sleep(0.1)
  
  except KeyboardInterrupt:
    print('shutting down joystick')