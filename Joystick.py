import PCF8591

class Joystick():

  def __init__(self, address, chn1, chn2):
    self.xVal = PCF8591(address)
    self.yVal = PCF8591(address)
    self.xChn = chn1
    self.yChn = chn2

  def getX(self):
    return self.xVal.read(self.xChn)

  def getY(self):
    return self.yVal.read(self.yChn)
  
  
    
      