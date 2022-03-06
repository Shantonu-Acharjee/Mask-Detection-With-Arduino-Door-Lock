import pyfirmata
from pyfirmata import Arduino, SERVO
import time
port = 'COM6'
board = Arduino(port)

try:
    
    Motor = board.get_pin('d:9:s')
    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()
    def ServoMotor(val = 0):
        if val == 1:
            Motor.write(0)
        
        if val != 1:
            Motor.write(75)
      
        
except:
    print('Arduino File Error')



Motor.write(0)

