#!/usr/bin/env python3

import cv2
import numpy as np
import sys
import sdl2
import sdl2.ext

W = np.floor_divide(1920, 1)
H = np.floor_divide(1080, 1)

sdl2.ext.init()

window = sdl2.ext.Window("Frame", size=(W, H))
window.show()


def get_frame(frame):
    
    # Resize
    img = cv2.resize(frame, (W, H), cv2.INTER_AREA)
    
    # Exit
    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            exit(0)
    
    # Draw
    windowArray = sdl2.ext.pixels3d(window.get_surface()) 
    windowArray[:,:,0:3] = img.swapaxes(0,1)    
    window.refresh()

    # cv2.imshow('frame', img)
    print(img)

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
