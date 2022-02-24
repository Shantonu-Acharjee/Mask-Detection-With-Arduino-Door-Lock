from pyfirmata import ArduinoMega
import time
import keyboard
port = 'COM3'
board = ArduinoMega(port)





def ArduinoState(valu):
    print(valu)
        
    if valu == 1:
        board.digital[13].write(1)
            
    else:
        board.digital[13].write(0)





def QggrState(valu):
    if valu == 1:
        board.digital[12].write(1)
        

    if valu != 1:
        board.digital[12].write(0)

        


