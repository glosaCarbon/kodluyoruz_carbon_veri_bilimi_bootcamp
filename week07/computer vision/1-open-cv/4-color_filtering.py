import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# HSV -> hue = color, value = how much of that color, saturation = intensity of that color
# https://giggster.com/guide/static/fed42130c194b0c240a4ec10408adf97/8282f/hsl-cover-2.png

while(1):
    _, frame = cap.read() 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([100,150,0],np.uint8)  # it is hard to find these values
    upper_blue = np.array([140,255,255],np.uint8)
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()