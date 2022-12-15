import pyfirmata
import time

pinA = 2
pinB = 3
pinC = 4
pinD = 5
pinE = 6
pinF = 7
pinG = 8
D1 = 9
D2 = 10
D3 = 11
D4 = 12
i=1

board = pyfirmata.Arduino('COM5')

def position(x):
    if x ==1 :
        board.digital[D1].write(1)
        board.digital[D2].write(0)
        board.digital[D3].write(0)
        board.digital[D4].write(0)
    if x ==2:
        board.digital[D1].write(0)
        board.digital[D2].write(1)
        board.digital[D3].write(0)
        board.digital[D4].write(0)
    if x ==3:
        board.digital[D1].write(0)
        board.digital[D2].write(0)
        board.digital[D3].write(1)
        board.digital[D4].write(0)
    if x == 4:

        board.digital[D1].write(0)
        board.digital[D2].write(0)
        board.digital[D3].write(0)
        board.digital[D4].write(1)
def digit(y):
    if y==1:
        board.digital[pinA].write(1)
        board.digital[pinB].write(0)
        board.digital[pinC].write(0)
        board.digital[pinD].write(1)
        board.digital[pinE].write(1)
        board.digital[pinF].write(1)
        board.digital[pinG].write(1)
    if y==2:

        board.digital[pinA].write(0)
        board.digital[pinB].write(0)
        board.digital[pinC].write(1)
        board.digital[pinD].write(0)
        board.digital[pinE].write(0)
        board.digital[pinF].write(1)
        board.digital[pinG].write(0)
    if y==3: 

        board.digital[pinA].write(0)
        board.digital[pinB].write(0)
        board.digital[pinC].write(0)
        board.digital[pinD].write(0)
        board.digital[pinE].write(1)
        board.digital[pinF].write(1)
        board.digital[pinG].write(0)
    if y ==4: 
        board.digital[pinA].write(1)
        board.digital[pinB].write(0)
        board.digital[pinC].write(0)
        board.digital[pinD].write(1)
        board.digital[pinE].write(1)
        board.digital[pinF].write(0)
        board.digital[pinG].write(0)
    if y==5: 
        board.digital[pinA].write(0)
        board.digital[pinB].write(1)
        board.digital[pinC].write(0)
        board.digital[pinD].write(0)
        board.digital[pinE].write(1)
        board.digital[pinF].write(0)
        board.digital[pinG].write(0)
    if y==6:
        board.digital[pinA].write(0)
        board.digital[pinB].write(1)
        board.digital[pinC].write(0)
        board.digital[pinD].write(0)
        board.digital[pinE].write(0)
        board.digital[pinF].write(0)
        board.digital[pinG].write(0)
    if y==7:
        board.digital[pinA].write(0)
        board.digital[pinB].write(0)
        board.digital[pinC].write(0)
        board.digital[pinD].write(1)
        board.digital[pinE].write(1)
        board.digital[pinF].write(0)
        board.digital[pinG].write(1)
    if y==8:
        board.digital[pinA].write(0)
        board.digital[pinB].write(0)
        board.digital[pinC].write(0)
        board.digital[pinD].write(0)
        board.digital[pinE].write(0)
        board.digital[pinF].write(0)
        board.digital[pinG].write(0)
    if y==9: 
        board.digital[pinA].write(0)
        board.digital[pinB].write(0)
        board.digital[pinC].write(0)
        board.digital[pinD].write(0)
        board.digital[pinE].write(1)
        board.digital[pinF].write(0)
        board.digital[pinG].write(0)
    if y==0:
        board.digital[pinA].write(0)
        board.digital[pinB].write(0)
        board.digital[pinC].write(0)
        board.digital[pinD].write(0)
        board.digital[pinE].write(0)
        board.digital[pinF].write(0)
        board.digital[pinG].write(1)

x=1
y=0
while True:
    if x>4 :
        x=1
    if y>9:
        y=0
    position(x)
    digit(y)
    x=x+1
    y=y+1
    time.sleep(1)