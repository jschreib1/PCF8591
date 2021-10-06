from time import sleep
from PCF import PCF8591

class Joystick:
  def __init__(self, address):
    self.PCF8591 = PCF8591(address)
    #PCF8591(0x40)
  def getx(self):
    #print(PCF8591.read(1))
    return self.PCF8591.read(1)

  def gety(self):
    #print(PCF8591.read(2))
    return self.PCF8591.read(2)