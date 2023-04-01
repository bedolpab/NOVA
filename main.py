#!/usr/bin/env python3

import cv2
import numpy as np
import sys
from PIL import ImageTk, Image
import matplotlib.pyplot as plt

# (874, 1164, 3)
W = 874
H = 1164
C = 3

if __name__ == '__main__':

    file = 'video.hevc'
    cap = cv2.VideoCapture(file)
    if(cap.isOpened() == False):
        print("file error")
    
    fig, ax = plt.subplots(1, 2)
    while(cap.isOpened()):
        # Read frame
        ret, frame = cap.read()

        if ret == True:
             # Resize frame
            img = cv2.resize(frame, (W//2, H//4), interpolation=cv2.INTER_AREA)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            ax[0].imshow(img)
            ax[1].imshow(img)
            plt.pause(0.01)
            # Quit key
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


