from time import sleep
from PCF import PCF8591

class Joystick:
  def __init__(self, address):
    self.PCF8591 = PCF8591(address)
    #PCF8591(0x40)
    def getx():
      #print(PCF8591.read(1))
      return PCF8591.read(1)

    def gety():
      #print(PCF8591.read(2))
      return PCF8591.read(2)

    print('%s, %s'.format(self.x, self.y))
    sleep(100)