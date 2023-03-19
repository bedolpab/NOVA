#!/usr/bin/env python3

import cv2
import numpy as np
import pygame
import sys

W = np.floor_divide(1920, 2)
H = np.floor_divide(1080, 2)

pygame.init()
screen = pygame.display.set_mode((W, H))

def get_frame(frame):
    img = cv2.resize(frame, (W, H), cv2.INTER_AREA)
    surf = pygame.surfarray.make_surface(img.swapaxes(0,1))
    screen.blit(surf, (0, 0))
    pygame.display.update()
    print(img.shape)

def show_mp4(file):
    cap = cv2.VideoCapture(file)
    if(cap.isOpened() == False):
        print("file error")

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            get_frame(frame)

            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    show_mp4('drive.mp4')
