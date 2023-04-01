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


def read_frame(frame):
    img = cv2.resize(frame, (W//2, H//4), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    ax1.set_title("Frame")

    ax2.hist(gray.ravel(), bins=256, range=(0, 256))
    ax2.set_title("Frame hist")
    print(img.shape)
    plt.pause(1)

def show_mp4(file):
    cap = cv2.VideoCapture(file)
    if(cap.isOpened() == False):
        print("file error")

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret == True:
            read_frame(frame)
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':

    # Model Architecture
    # --------------------
    # INPUT
    # Get input from video
    file = 'video.hevc'
    
    show_mp4(file)    
    # Previous Frame (3, 128, 256)

    # Current Frame (3, 128, 256)
    
    # Concat BOTH images --> (6, 128, 256)

    # APPLY EFFICIENTNET-B2

