import cv2
import numpy as np
import threading
import make_original_graph as make_graph
import part_seperate as graph
import make_SET_graph as t
import s3 as s3

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from matplotlib import pyplot as plt

pin_x=[]
pin_y=[]
spin_x=[]
spin_y=[]


color1=(255,0,0)
color2=(0,255,0)
color3=(0,0,255)

radius=10
radius2=2
thickness=2


def marker(point, mov_x, mov_y, side_x, side_y, id_text):
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
        fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
        fps=30
       
        out = cv2.VideoWriter('Camera1_original_master_out.avi',fourcc, fps, (640,480))
        num_frame=0

        while cap.isOpened():
            ret,frame = cap.read()
            if ret:
                try:
                    '''
                    #머리
                    center3 = (int(t0_x[1]+140), int(t0_y[num_frame]))
                    start3 = (int(t0_x[1]+100), int(t0_y[num_frame]))
                    end3 = (int(t0_x[1]+180), int(t0_y[num_frame]))
                    flo3 = (int(t0_x[1]+140), height)
                    frame = cv2.line(frame, start3, end3, color1, thickness)
                    frame = cv2.line(frame, flo3, center3, color1, thickness)


                    c = (int(t0_x[0]+140), int(t0_y[0]))
                    s = (int(t0_x[0]+100), int(t0_y[0]))
                    e = (int(t0_x[0]+180), int(t0_y[0]))
                    f = (int(t0_x[0]+140), int(t0_y[0]))



                    end3 = (int(t0_x[1]+180), int(t0_y[num_frame]))
                    flo3 = (int(t0_x[1]+140), height)
                    frame = cv2.line(frame, start3, end3, color1, thickness)
                    frame = cv2.line(frame, flo3, center3, color1, thickness)
                    #frame = cv2.line(frame, center3, 0, color1, thickness)
                    '''


                    #angle
                    start = (int(t2_x[num_frame]), int(t2_y[num_frame]))
                    end = (int(t3_x[num_frame]), int(t3_y[num_frame]))
                    ang = (int(t_x[num_frame]), int(t_y[num_frame]))
                    frame = cv2.line(frame, start, end, color2, thickness)
                    frame = cv2.line(frame, ang, end, color2, thickness)
                    frame = cv2.line(frame, start, ang, color2, thickness)

                    #손목
                    center = (int(t_x[num_frame]), int(t_y[num_frame]))
                    frame = cv2.circle(frame, center, radius, color2, thickness)


                    #knee
                    center = (int(t10_x[num_frame]), int(t10_y[num_frame]))
                    frame = cv2.circle(frame, center, radius, color3, thickness)
                    center = (int(t13_x[num_frame]), int(t13_y[num_frame]))
                    frame = cv2.circle(frame, center, radius, color3, thickness)


                    
                    for i in range(0, num_frame):
                        
                        #머리
                        center3 = (int(t0_x[i]), int(t0_y[i]))
                        frame = cv2.circle(frame, center3, radius2, color1, thickness)
                        '''
                        frame = cv2.line(frame, s, e, color1, thickness)
                        frame = cv2.line(frame, f, c, color1, thickness)
                        '''

                        #손목
                        center2 = (int(t_x[i]), int(t_y[i]))
                        frame = cv2.circle(frame, center2, radius2, color2, thickness)

                        #knee
                        center2 = (int(t10_x[i]), int(t10_y[i]))
                        frame = cv2.circle(frame, center2, radius2, color3, thickness)
                        center2 = (int(t13_x[i]), int(t13_y[i]))
                        frame = cv2.circle(frame, center2, radius2, color3, thickness)


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
   
   

    #head
    t0_x, t0_y = make_graph.make(mov_x, mov_y,0)

    
    #손목
    t_x, t_y = t.make(mov_x, mov_y)


    #어깨
    t2_x, t2_y= make_graph.make(mov_x, mov_y,2)
    t3_x, t3_y = make_graph.make(mov_x, mov_y, 5)
    

    #knee
    t10_x, t10_y = make_graph.make(mov_x, mov_y,10)
    t13_x, t13_y = make_graph.make(mov_x, mov_y,13)


    marking('Camara1','Camera1.avi')

    ffmpeg_extract_subclip("Camera1_original_master_out.avi", address/10, finish/10, targetname="Camera1_master_out.avi")
    
    s3.upload(id_text)

