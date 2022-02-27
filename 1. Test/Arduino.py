from ast import While
from pyfirmata import Arduino, SERVO
import time
import keyboard
port = 'COM7'
board = Arduino(port)



Motor = board.get_pin('d:9:s')
Motor.write(0)

def ServoMotor(val):
    if val == 1:
        Motor.write(90)
       
    else:
        Motor.write(0)
      
        

