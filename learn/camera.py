import numpy as np
import cv2

def camera():
    cap=cv2.VideoCapture(0)

    while True:
        ret,frame=cap.read(0)
        cv2.imshow('frame',frame)
       # if cv2.waitKey(1)==ord("x"):
          #  break

def off_camera():
    cap.release()
    cv2.destroyAllWindow()
    
