import pyfirmata
import time
board = pyfirmata.Arduino('COM5')
i=9
while True :
     if i>11 :
        i=9
     board.digital[i].write(1)
     time.sleep(1)
     board.digital[i].write(0)
     time.sleep(1)
     i=i+1