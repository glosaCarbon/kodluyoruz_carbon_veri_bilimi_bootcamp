import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1-open-cv\images\watch.jpg') # read image

if img is None:
    print("Image path is incorrect")

cv2.imshow('image', img) # show image -> gives error if img is None

cv2.waitKey(0) # wait for key press, or wait for given ms
cv2.destroyAllWindows()
