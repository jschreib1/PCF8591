#   To check address: sudo i2cdetect -y 1

import smbus
from time import sleep

class PCF8591:

  def __init__(self,address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val):
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))

class Joystick:
  def __init__(self, address, x, y):
    self.PCF8591 = PCF8591(address, x, y)
    PCF8591(address)
    self.x = self.getx()
    self.y = self.gety()
    def getx():
      #print(PCF8591.read(1))
      return PCF8591.read(1)

    def gety():
      #print(PCF8591.read(2))
      return PCF8591.read(2)
      sleep(100)

  print('%s, %s'.format(self.x, self.y))
