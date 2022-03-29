import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# HSV -> hue = color, value = how much of that color, saturation = intensity of that color
# https://giggster.com/guide/static/fed42130c194b0c240a4ec10408adf97/8282f/hsl-cover-2.png

while(1):
    _, frame = cap.read() 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([100,150,0],np.uint8)  # it is hard to find these values
    upper_red = np.array([140,255,255],np.uint8)
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask= mask)

    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel) # simple averaging

    blur = cv2.GaussianBlur(res, (15,15), 0)

    median = cv2.medianBlur(res, 15)

    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    #cv2.imshow('frame',frame)
    #
    cv2.imshow('mask', mask)
    #cv2.imshow('res', res)
    #cv2.imshow('smoothed', smoothed)
    #cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)


    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()