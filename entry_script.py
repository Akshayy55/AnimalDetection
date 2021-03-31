import os
import cv2
import numpy as np
import time
import base64
from detector import model
from entry_camera import EntryCamera
class EntryCameraModule():
    def __init__(self):
        self.animal_detector = model()
        self.entry_camera_data = EntryCamera()
        self.video_capture = cv2.VideoCapture("Video/ezgif.com-video-cutter.mp4")
    def entry_camera(self,session):
        while True:
            # test with video
            ret, frame = self.video_capture.read()
            frame_h = frame.shape[0]
            frame_w = frame.shape[1]
            if frame is None:
                break
            start_time = time.time()
            animal_boxes, animal_name, scores = self.animal_detector.detect_animal(frame)
            print(scores, animal_name)
            class_list = [ "teddy bear", "giraffe", "zebra", "bear", "elephant", "cow", "sheep", "horse", "dog", "cat","bird" ]
            if scores > 0.8:
                if animal_name in class_list : 
                    total_time = (time.time() - start_time)
                    if len(animal_boxes) > 0:
                        for i in range(len(animal_boxes)):
                            box = animal_boxes[i]  
                            # print(box)
                            pt1 = (
                                    int(box[1] * frame_w),
                                    int(box[0] * frame_h),
                                )
                            pt2 = (
                                int(box[3] * frame_w),
                                int(box[2] * frame_h),
                                )
                            animal_img = frame[pt1[1]:pt2[1], pt1[0]:pt2[0]] 
                            crop_img =  cv2.resize(animal_img,(480, 360),interpolation=cv2.INTER_AREA)
                            self.entry_camera_data.insert_entry_cam_data(session, crop_img, animal_name, total_time)
                            label = "{}".format(animal_name) 
                                    # creating bounding box on faces
                            cv2.rectangle(frame, (pt1), (pt2),
                                            (255, 255, 255), 2)
                            cv2.putText(frame,label,(pt1[0],pt1[1]-20),
                                        cv2.FONT_HERSHEY_COMPLEX,1.5,(255,0,0),2)             

            cv2.imshow('Keras Faces', frame)
            if cv2.waitKey(5) == 27:  # ESC key press
                break

        cv2.destroyAllWindows()