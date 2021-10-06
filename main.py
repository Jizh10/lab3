from Joystick import Joystick
import time

xChn = 0
yChn = 1
address = 0x48

joystick = Joystick(address, xChn, yChn)

while True:
  print("%4s, %4s" % (joystick.getX(), joystick.getY()))
  time.sleep(0.1)
