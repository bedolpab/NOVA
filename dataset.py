import numpy as np
import os 
import sys
import cv2
import matplotlib.pyplot as plt

class FrameReader():
    def __init__(self, video):
        self.path = video
        self.frames = self.get_frames()

    def get_frames(self):
        video = cv2.VideoCapture(self.path)
        frames = []
        while(True):
            ret, frame = video.read()
            if ret:
                frames.append(frame)
            else:
                break
        return frames

class Dataset():
    def __init__(self, main_dir):
        self.main_dir = main_dir
        self.frame_reader = FrameReader(self.main_dir + "video.hevc")
        self.gps_times = np.load(main_dir + "global_pose/frame_gps_times")
        self.orientations = np.load(main_dir + "global_pose/frame_orientations")
        self.positions = np.load(main_dir + "global_pose/frame_positions")
        self.times = np.load(main_dir + "global_pose/frame_times")
        self.velocities = np.load(main_dir + "global_pose/frame_velocities")
    
    def frame_data(self, frame, idx):
        frame = {
            "image": np.array(frame),
            "gps_times": self.gps_times[idx],
            "orinetation": self.orientations[idx],
            "positions": self.positions[idx],
            "times": self.times[idx],
            "velocities": self.velocities[idx]
        }

        return frame

    def get_frame(self, idx):
        image = np.array(self.frame_reader.frames[idx])
        frame = {
            "image": image,
            "gps_times": self.gps_times[idx],
            "orinetation": self.orientations[idx],
            "positions": self.positions[idx],
            "times": self.times[idx],
            "velocities": self.velocities[idx]
        }
        print(frame)
        plt.imshow(self.frame_reader.frames[idx])
        plt.show()

    def play_video(self):
        for i in range(len(self.frame_reader.frames)):
            frame = self.frame_reader.frames[i]
            print(self.frame_data(frame, i))
            plt.imshow(frame)
            plt.pause(0.0001)


if __name__ == "__main__":
    test_path = "data/set-1/4/"
    data = Dataset(test_path)
    data.play_video()
    
