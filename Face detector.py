from platform import system
import string
import cv2
import pyfirmata
import time
import random
from pyfirmata import SERVO

j=random.randint(1,100)

board = pyfirmata.Arduino('COM11')
board.digital[9].mode= SERVO
trained_face_data = cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)
def screenshot():
    global cam
    #cv2.imshow("screenshot", cam.read()[1]) # shows the screenshot directly
    cv2.imwrite('screenshot.png',cam.read()[1]) # or saves it to disk

while True:
    successful_frame_read, frame= webcam.read() #vid = cv2.resize(vid, (320, 220))
    #frame=(cv2.resize(frame, (320, 220)))
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y),
                      (x+w, y+h), (0, 255, 0), 2)
        board.analog[9].write(1)
        cv2.imwrite(str(j)+'.png' ,webcam.read()[1])
        time.sleep(0.1)
        print(face_coordinates)
    board.digital[9].write(0)
    cv2.imshow('GrebecGod Face detector', frame)
    key = cv2.waitKey(1)
    if key == 81 or key == 113: #q
            break
"""""
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
print(face_coordinates)
cv2.imshow('GrebecGod Face detector', img)
cv2.waitKey()
"""
print("Code completed")