from math import ceil
import cv2
import numpy as np
from matplotlib import pyplot as plt

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


st = "".join(list(reversed('Ñ@#W$9876543210?!abc;:+=-,._  ')))

cap = cv2.VideoCapture(0) # 0 -> first webcam


while(True):
    ret, img = cap.read() # ret -> return: True or False
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    small = cv2.resize(gray, dsize=(64, 64), interpolation=cv2.INTER_CUBIC)
    
    cv2.imshow('gray image', gray)
    
    clearConsole()

    for i in small: 
        for j in i: 
            # j -> (0, 255) / 255
            # j -> 0, 1 arasında oluyor 
            # 'Ñ@#W$9876543210?!abc;:+=-,._  '
            
            c = ceil(j/200 * len(st))
            character = st[min(c, len(st)-1)]
            print(character, end='')
        print()
    
    if cv2.waitKey(30) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


