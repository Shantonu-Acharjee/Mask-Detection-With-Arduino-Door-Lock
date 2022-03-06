import pyfirmata
from tkinter import *
board = pyfirmata.Arduino('COM6')
import time


iter8 = pyfirmata.util.Iterator(board)
iter8.start()

pin9 = board.get_pin('d:9:s')

while True:
    pin9.write(75)
    time.sleep(0.5)
    pin9.write(0)
    time.sleep(0.5)
    
