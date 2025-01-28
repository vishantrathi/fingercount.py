import cv2
import time
import numpy as np

wCam, hCam =640, 480

cap=cv2.VideoCapture(1)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

while True :
    sucess, img=cap.read()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,f'FPS:{int(fps)}',(40,70,cv2.FONT_HERSHEY_COMPLEX,3(255,0,0)3))



