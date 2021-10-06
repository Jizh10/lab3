import PCF8591

class Joystick():

  def __init__(self, address1, address2):
    self.xVal = PCF8591(address1)
    self.yVal = PCF8591(address2)

  def getX(self):
    return self.xVal.read()

  def getY(self):
    return self.yVal.read()
  
  
    
      