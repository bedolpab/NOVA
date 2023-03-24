#!/usr/bin/env python3

import cv2
import numpy as np
import sys
import sdl2
import sdl2.ext

W = np.floor_divide(1920, 2)
H = np.floor_divide(1080, 2)


sdl2.ext.init()

window = sdl2.ext.Window("Frame", size=(W, H))
window.show()

# INIT ORB
orb = cv2.ORB_create()


def get_frame(frame):
    
    # Resize
    img = cv2.resize(frame, (W, H), cv2.INTER_AREA)
    
    # Orb features
    kp = orb.detect(img, None)
    kp, des = orb.compute(img, kp)
    for p in kp:
        print(f'keypoint: {p.pt}')

    # Draw
    img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
    
    # Exit
    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            exit(0)
    
    # Draw
    windowArray = sdl2.ext.pixels3d(window.get_surface()) 
    windowArray[:,:,0:3] = img_kp.swapaxes(0,1)    
    window.refresh()

    # cv2.imshow('frame', img)
    print(img)
    print(f'size: {img.shape}')
    input('frame cot: ()')

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
