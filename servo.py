import pyfirmata
from pyfirmata import SERVO
import time
pin=9
board=pyfirmata.Arduino('COM11')
board.digital[pin].mode= SERVO
def rotateServo (pin,angle):
    board.digital[pin].write(angle)
    time.sleep(0.015)
while True:
    for i in range(0,180):
        rotateServo(pin,i)
    print("BACK")
    for i in range(180,1,-1):
        rotateServo(pin,i)