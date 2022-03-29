import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 0 -> first webcam

while(True):
    ret, frame = cap.read() # ret -> return: True or False
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    small = cv2.resize(gray, dsize=(64, 64), interpolation=cv2.INTER_CUBIC)
    
    cv2.imshow('small', small)  
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
