import cv2
import numpy as np
import threading
import make_original_graph as make_graph
import part_seperate as graph
import make_SET_graph as t


from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from matplotlib import pyplot as plt

pin_x=[]
pin_y=[]
spin_x=[]
spin_y=[]


color1=(0,0,255)
color2=(255,255,0)
radius=10
radius2=2
thickness=2


def marker(point, mov_x, mov_y, side_x, side_y):
    address=point[0]
    takeaway=point[1]
    backswing=point[2]
    top=point[3]
    impact=point[4]
    finish=point[5]

    def marking(windowname, VideoName):
        cap=cv2.VideoCapture('./examples/media/'+str(VideoName))
        cap.set(3,640)
        cap.set(4,480)

        fps=30
       
        out = cv2.VideoWriter('Camera1_original_pelvis_out.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (640,480))

        num_frame=0

        while cap.isOpened():
            ret,frame = cap.read()
            if ret:
                try:
                    '''
                    for i in range(0, num_frame):
                        #pelvis
                        center1 = (int(t9_x[i]), int(t9_y[i]))
                        center2 = (int(t12_x[i]), int(t12_y[i]))
                        frame = cv2.line(frame, center1, center2, color1, thickness)
                        
                        #spine
                        center1 = (int(t1_x[i]), int(t1_y[i]))
                        center2 = (int(t8_x[i]), int(t8_y[i]))
                        frame = cv2.line(frame, center1, center2, color, thickness)
                        
                     '''
                    #pelvis
                    center1 = (int(t9_x[num_frame]), int(t9_y[num_frame]))
                    center2 = (int(t12_x[num_frame]), int(t12_y[num_frame]))
                    frame = cv2.line(frame, center1, center2, color1, thickness)

                    #spine
                    center1 = (int(t1_x[num_frame]), int(t1_y[num_frame]))
                    center2 = (int(t8_x[num_frame]), int(t8_y[num_frame]))
                    frame = cv2.line(frame, center1, center2, color2, thickness)

                    c1 = (int(t1_x[0]), int(t1_y[0]))
                    c2 = (int(t8_x[0]), int(t8_y[0]))
                    frame = cv2.line(frame, c1, c2, color2, thickness)
                        

                    out.write(frame)
                    out.write(frame)
                    out.write(frame)
                    num_frame = num_frame+1

                except:
                    pass

            else:
                break  
                         
        cap.release()
        out.release()
        cv2.destroyAllWindows()

        
    # 부위별 original graph만들기
    ball_x=674
    ball_y=679
   
   

    #pelvis
    t9_x, t9_y = make_graph.make(side_x, side_y,9)
    t12_x, t12_y = make_graph.make(side_x, side_y,12)


    #spine
    t8_x, t8_y = make_graph.make(side_x, side_y,8)
    t1_x, t1_y = make_graph.make(side_x, side_y,1)


    


    marking('Camara2','Camera2.avi')

    ffmpeg_extract_subclip("Camera1_original_pelvis_out.avi", address/10, finish/10, targetname="Camera1_pelvis_out.avi")
