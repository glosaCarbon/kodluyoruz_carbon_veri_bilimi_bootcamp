import cv2
import numpy as np

img = cv2.imread('1-open-cv\\images\\bookpage.jpg') # read image


#retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) # min 12, max 255
#
#cv2.imshow('original', img)
#cv2.imshow('threshold', threshold)


#grey_scale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#retval, grey_threshold = cv2.threshold(grey_scale, 12, 255, cv2.THRESH_BINARY) # min 12, max 255
#
#cv2.imshow('grey', grey_scale)
#cv2.imshow('grey_threshold', grey_threshold)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1) 

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('gaussian', th)


cv2.waitKey(0)
cv2.destroyAllWindows()
