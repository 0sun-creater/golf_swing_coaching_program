import cv2
import numpy as np
import threading
import make_original_graph as make_graph

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


pin_x=[]
pin_y=[]
spin_x=[]
spin_y=[]

color=(0,0,255)
radius=10
thickness=2

def marker(point, mov_x, mov_y, side_x, side_y, mark, smark):
    address=point[0]
    takeaway=point[1]
    backswing=point[2]
    top=point[3]
    impact=point[4]
    finish=point[5]
    print("marker" + str(impact))

    def marking(windowname, VideoName, mark):
        
        cap=cv2.VideoCapture('./examples/media/'+str(VideoName))
        num_frame=0
        
        fps=30
        width=int(cap.get(3))
        height=int(cap.get(4))

        fcc= cv2.VideoWriter_fourcc(*'XVID')
        frame_array=[]
        out = cv2.VideoWriter('Camera1_original_out.avi',fcc,fps,(width,height))

        while cap.isOpened():
            ret,frame = cap.read()
            if ret:         
                if num_frame < address: # Address 구간
                    frame = make_frame(0, num_frame, frame) 
                                        
                if num_frame < takeaway and num_frame > address: # Address~TakeAway 구간
                    frame = make_frame(1, num_frame, frame) 

                if num_frame < takeaway+10 and num_frame > takeaway-10: # TakeAway 구간
                    frame = make_frame(2, num_frame, frame) 

                if num_frame < top and num_frame > takeaway: # BackSwing 구간
                    frame = make_frame(3, num_frame, frame) 

                if num_frame < top+10 and num_frame > top-10: # TopSwing 구간
                    frame = make_frame(4, num_frame, frame) 

                if num_frame < impact and num_frame > top: # TopSwing~Impact 구간
                    frame = make_frame(5, num_frame, frame) 

                if num_frame < impact+10 and num_frame > impact-10: # Impact 구간
                    frame = make_frame(6, num_frame, frame) 

                try:
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
        
    def marking_side(swindowname, sVideoName, smark):
        cap=cv2.VideoCapture('./examples/media/'+str(sVideoName))
        num_frame=0

        fps=30
        width=int(cap.get(3))
        height=int(cap.get(4))
        
        fcc= cv2.VideoWriter_fourcc(*'XVID')
        frame_array=[]
        out = cv2.VideoWriter('Camera2_original_out.avi',fcc,fps,(width,height))
        
        while cap.isOpened():
            ret,frame = cap.read()
            if ret:
                if num_frame < address: # Address 구간
                    frame = smake_frame(0, num_frame, frame) 
                                        
                if num_frame < takeaway and num_frame > address: # Address~TakeAway 구간
                    frame = smake_frame(1, num_frame, frame) 

                if num_frame < takeaway+10 and num_frame > takeaway-10: # TakeAway 구간
                    frame = smake_frame(2, num_frame, frame) 

                if num_frame < top and num_frame > takeaway: # BackSwing 구간
                    frame = smake_frame(3, num_frame, frame) 

                if num_frame < top+10 and num_frame >top-10: # TopSwing 구간
                    frame = smake_frame(4, num_frame, frame) 

                if num_frame < impact and num_frame > top: # TopSwing~Impact 구간
                    frame = smake_frame(5, num_frame, frame) 

                if num_frame < impact+10 and num_frame > impact-10: # Impact 구간
                    frame = smake_frame(6, num_frame, frame) 

                        
                try:
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



    def make_frame(num_part, num_frame, frame):
        if mark[num_part][0] == 1: #머리
            center = (int(pin0_x[num_frame]), int(pin0_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][1] == 1: # 어깨
            start = (int(pin2_x[num_frame]), int(pin2_y[num_frame]))
            end = (int(pin5_x[num_frame]), int(pin5_y[num_frame]))
            frame = cv2.line(frame, start, end, color, thickness)                    
        if mark[num_part][2] == 1: # 왼팔
            center = (int(pin6_x[num_frame]), int(pin6_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][3] == 1: # 오른팔
            center = (int(pin3_x[num_frame]), int(pin3_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][4] == 1: # 왼손목
            center = (int(pin7_x[num_frame]), int(pin7_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][5] == 1: # 오른손목
            center = (int(pin4_x[num_frame]), int(pin4_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][6] == 1: # 공
            center = (ball_x, ball_y)
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][7] == 1: # 척추
            start = (int(pin1_x[num_frame]), int(pin1_y[num_frame]))
            end = (int(pin8_x[num_frame]), int(pin8_y[num_frame]))
            frame = cv2.line(frame, start, end, color, thickness)
        if mark[num_part][8] == 1: # 골반
            start = (int(pin9_x[num_frame]), int(pin9_y[num_frame]))
            end = (int(pin12_x[num_frame]), int(pin12_y[num_frame]))
            frame = cv2.line(frame, start, end, color, thickness)
        if mark[num_part][9] == 1: # 왼무릎
            center = (int(pin13_x[num_frame]), int(pin13_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][10] == 1: # 오른무릎
            center = (int(pin10_x[num_frame]), int(pin10_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][11] == 1: # 왼발
            center = (int(pin14_x[num_frame]), int(pin14_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][12] == 1: # 오른발
            center = (int(pin11_x[num_frame]), int(pin11_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness)

        return frame


    def smake_frame(num_part, num_frame, frame):
        if mark[num_part][0] == 1: #머리
            center = (int(spin0_x[num_frame]), int(spin0_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][1] == 1: # 어깨
            start = (int(spin2_x[num_frame]), int(pin2_y[num_frame]))
            end = (int(spin5_x[num_frame]), int(spin5_y[num_frame]))
            frame = cv2.line(frame, start, end, color, thickness)                    
        if mark[num_part][2] == 1: # 왼팔
            center = (int(spin6_x[num_frame]), int(spin6_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][3] == 1: # 오른팔
            center = (int(spin3_x[num_frame]), int(spin3_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][4] == 1: # 왼손목
            center = (int(spin7_x[num_frame]), int(spin7_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][5] == 1: # 오른손목
            center = (int(spin4_x[num_frame]), int(spin4_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][6] == 1: # 공
            center = (sball_x, sball_y)
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][7] == 1: # 척추
            start = (int(spin1_x[num_frame]), int(spin1_y[num_frame]))
            end = (int(spin8_x[num_frame]), int(spin8_y[num_frame]))
            frame = cv2.line(frame, start, end, color, thickness)
        if mark[num_part][8] == 1: # 골반
            start = (int(spin9_x[num_frame]), int(spin9_y[num_frame]))
            end = (int(spin12_x[num_frame]), int(spin12_y[num_frame]))
            frame = cv2.line(frame, start, end, color, thickness)
        if mark[num_part][9] == 1: # 왼무릎
            center = (int(spin13_x[num_frame]), int(spin13_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][10] == 1: # 오른무릎
            center = (int(spin10_x[num_frame]), int(spin10_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][11] == 1: # 왼발
            center = (int(spin14_x[num_frame]), int(spin14_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness) 
        if mark[num_part][12] == 1: # 오른발
            center = (int(spin11_x[num_frame]), int(spin11_y[num_frame]))
            frame = cv2.circle(frame, center, radius, color, thickness)

        return frame


    # 부위별 original graph만들기
    ball_x=630
    ball_y=679
    #정면
    pin0_x, pin0_y = make_graph.make(mov_x, mov_y,0) #머리
    pin5_x, pin5_y = make_graph.make(mov_x, mov_y,5) #왼어깨
    pin2_x, pin2_y = make_graph.make(mov_x, mov_y,2) #오른어깨 
    pin6_x, pin6_y = make_graph.make(mov_x, mov_y,6) #왼팔
    pin3_x, pin3_y = make_graph.make(mov_x, mov_y,3) #오른팔
    pin7_x, pin7_y = make_graph.make(mov_x, mov_y,7) #왼쪽 손목
    pin4_x, pin4_y = make_graph.make(mov_x, mov_y,4) #오른쪽 손목
    pin1_x, pin1_y = make_graph.make(mov_x, mov_y,1) #척추 1
    pin8_x, pin8_y = make_graph.make(mov_x, mov_y,8) #척추 8
    pin12_x, pin12_y = make_graph.make(mov_x, mov_y,12) #왼골반
    pin9_x, pin9_y = make_graph.make(mov_x, mov_y,9) #오른골반
    pin13_x, pin13_y = make_graph.make(mov_x, mov_y,13) #왼무릎
    pin10_x, pin10_y = make_graph.make(mov_x, mov_y,10) #오른무릎
    pin14_x, pin14_y = make_graph.make(mov_x, mov_y,14) #왼발
    pin11_x, pin11_y = make_graph.make(mov_x, mov_y,11) #오른발
    #측면
    sball_x=0
    sball_y=0
    spin0_x, spin0_y = make_graph.make(side_x, side_y,0) #머리
    spin5_x, spin5_y = make_graph.make(side_x, side_y,5) #왼어깨
    spin2_x, spin2_y = make_graph.make(side_x, side_y,2) #오른어깨 
    spin6_x, spin6_y = make_graph.make(side_x, side_y,6) #왼팔
    spin3_x, spin3_y = make_graph.make(side_x, side_y,3) #오른팔
    spin7_x, spin7_y = make_graph.make(side_x, side_y,7) #왼쪽 손목
    spin4_x, spin4_y = make_graph.make(side_x, side_y,4) #오른쪽 손목
    spin1_x, spin1_y = make_graph.make(side_x, side_y,1) #척추 1
    spin8_x, spin8_y = make_graph.make(side_x, side_y,8) #척추 8
    spin12_x, spin12_y = make_graph.make(side_x, side_y,12) #왼골반
    spin9_x, spin9_y = make_graph.make(side_x, side_y,9) #오른골반
    spin13_x, spin13_y = make_graph.make(side_x, side_y,13) #왼무릎
    spin10_x, spin10_y = make_graph.make(side_x, side_y,10) #오른무릎
    spin14_x, spin14_y = make_graph.make(side_x, side_y,14) #왼발
    spin11_x, spin11_y = make_graph.make(side_x, side_y,11) #오른발



    thread1 = threading.Thread(target = marking, args = ('Camara1','Camera1.avi',mark,))                      
    thread2 = threading.Thread(target = marking_side, args = ('Camara2','Camera2.avi',smark,))
                        
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    
    ffmpeg_extract_subclip("Camera1_original_out.avi", address/10,finish/10, targetname="Camera1_out.avi")
    ffmpeg_extract_subclip("Camera2_original_out.avi", address/10,finish/10, targetname="Camera2_out.avi")
    
    ffmpeg_extract_subclip("Camera1_original_out.avi", address/10,takeaway/10, targetname="testing1.avi")
    ffmpeg_extract_subclip("Camera1_original_out.avi", takeaway/10, top/10, targetname="testing2.avi")
    ffmpeg_extract_subclip("Camera1_original_out.avi", top/10, impact/10, targetname="testing3.avi")
    ffmpeg_extract_subclip("Camera1_original_out.avi", impact/10,finish/10, targetname="testing4.avi")
    
