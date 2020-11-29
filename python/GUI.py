import sys
import datetime
import socket, time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5 import QtWidgets

from PyQt5.QtCore import Qt, QByteArray, QSettings, QTimer, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QSizePolicy, QVBoxLayout, QAction, QPushButton, QLineEdit
from PyQt5.QtGui import QMovie

from time import sleep


import main as m
import Python_to_Linux as PtoL

import cv2
import threading
import serial
import numpy as np
import math

import statistics
import os

import sys
import pymysql
import base64
import requests

cam0 = cv2.VideoCapture(2)
cam1 = cv2.VideoCapture(0)

arduino = serial.Serial('/dev/ttyACM0', 115200)
print("camera on")
ar_flag = 0
Impact_frame=0
cnt=0
id_text =""
light_stop=False
######################################## light thread
class lightThread(threading.Thread):
    def __init__(self, end, stop):
        threading.Thread.__init__(self)
        self.end = end
        self.stop = stop


    def __del__(self):
        print("del")
        
    def run(self):
        ligth(self.end, self.stop)
        
def ligth(end, stop):
    youngsun =1
    while youngsun:
        
        if stop():
            print("stop hihi")
            break
        f=arduino.readline()
        f=f.decode()
        if f == 'Impact\r\n':
            end.light_signal.emit()
            break


####################################### cam 녹화 스레드
class camThread(threading.Thread):
    success = 0
    def __init__(self, previewName, camID, cam):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
        self.cam = cam

        
    def run(self):
        self.success = camPreview(self.previewName, self.camID, self.cam)


def camPreview(previewName, camID, cam):
    global cnt

    cam.set(3,640)
    cam.set(4,480)

    ##
    #frame_width=int(cam.get(3))
    #frame_height=int(cam.get(4))
    ##

    fps = 30
    out = cv2.VideoWriter('./examples/media/'+ str(previewName)+'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (640,480))

    if camID==0:
        cnt = 0
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(seconds=8)

    while(True):
        if camID==0:
            cnt+=1
        ret, frame = cam.read()
        
        if ret:
            out.write(frame)
           
            if end_time < datetime.datetime.now():
                out.release()
                
                print("recoding success "+str(previewName))
                return 1
        else:
            print("error "+str(previewName))
            return 5
    
def impact_fram(cnt):
    global Impact_frame
    print(cnt)
    Impact_frame=cnt
    
####################################### interrupt 만들기
class Communicate(QObject):
    end_signal = pyqtSignal()
    cam_signal = pyqtSignal()
    main_signal = pyqtSignal()
    light_signal = pyqtSignal()
    
    take_signal = pyqtSignal()
    top_signal = pyqtSignal()
    impact_signal = pyqtSignal()

    youngseon = pyqtSignal()



####################################### 영상 재생 스레드         
class Video(threading.Thread):        
    def __init__(self, ui, previewName, labelName, width, height, re, stop, end):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.labelName = labelName
        self.ui = ui
        self.width = width
        self.height = height
        self.re = re
        self.stop = stop
        self.end = end

    def run(self):
        VideoPlayer(self.ui, self.previewName, self.labelName, self.width, self.height, self.re, self.stop, self.end)

def VideoPlayer(ui, previewName, label, width, height, re, stop, end):
    marker_cnt=0
    global ar_flag

    
    while True:
        cap = cv2.VideoCapture(previewName)
        if stop():
            break
        if re ==3 :
            while ar_flag == 0 :
                a=arduino.readline()
                a=a.decode()
                if a == 'Start\r\n':
                    ar_flag = 1
                    end.cam_signal.emit()
        
        while True:
            if re == 0:
                if ar_flag == 1:
                    break
                else:
                    pass
            elif re == 9:
                marker_cnt +=1

                
            label.ret, label.frame = cap.read()
            if label.ret:
                label.rgbImage = cv2.cvtColor(label.frame, cv2.COLOR_BGR2RGB)
                label.convertToQtFormat = QImage(label.rgbImage.data, label.rgbImage.shape[1],
                                                          label.rgbImage.shape[0], QImage.Format_RGB888)
                       
                label.pixmap = QPixmap(label.convertToQtFormat)
                label.p = label.pixmap.scaled(width, height, QtCore.Qt.IgnoreAspectRatio)

                label.setPixmap(label.p)
                label.update()
                if re == 9:
                    if marker_cnt == math.floor(m.point[1]*3):      #takeaway지점
                        end.take_signal.emit()
                    elif marker_cnt == math.floor(m.point[3]*3):    #top지점
                        end.top_signal.emit()
                    elif marker_cnt == math.floor(m.point[4]*3):    #impact지점
                        end.impact_signal.emit()
                loop = QtCore.QEventLoop()
                QtCore.QTimer.singleShot(25, loop.quit)
                loop.exec_()
            else:
                break
            
            if stop():
                break
            
        cap.release()
        
        if re == 0 or re == 3:
            break
        else:
            pass
        
    if re == 3:
        end.end_signal.emit()
        
def camera(end):
    global light_stop
    light_stop=False
    cam_t1 = camThread("Camera1", 0, cam0)
    cam_t2 = camThread("Camera2", 1, cam1)

    light = lightThread(end, lambda: light_stop)
    
    loop = QtCore.QEventLoop()
    QtCore.QTimer.singleShot(3000, loop.quit)
    loop.exec_()
    
    
    cam_t1.start()
    cam_t2.start()
    light.start()

    return light

    


def young(light):
    light.quit()
    

########################################## 피드백 스레드
class MainThread(threading.Thread):
    success = 0
    def __init__(self,end):
        threading.Thread.__init__(self)
        self.end = end
        
    def run(self):
        main_run(self.end)

def main_run(end):
    global id_text
    global Impact_frame
    PtoL.JSONmaker()
    m.main(Impact_frame, id_text)
    end.main_signal.emit()

########################################### main GUI
gifFile = "loading.gif"
class MyWindow_step(QMainWindow):
    def __init__(self, gifFile):
        super().__init__()
        self.gifFile = gifFile
        self.GUI_login()
        
        #self.GUI_all()

    def GUI_login(self):
        self.ui = uic.loadUi('Designer_login.ui')
        self.ui.show()

        self.ui.LoginButton.clicked.connect(lambda : self.LoginDB(self.ui))

    def LoginDB(self,a):

        global id_text
        id_text = a.UserID.text()
        
        try:
            #send db -> response 200
            conn = pymysql.connect("db-ladybug.cmghyay3tpvl.ap-northeast-2.rds.amazonaws.com",user="ladybug",passwd = "ladybug456123",db="AppService", port=3306,use_unicode=True,charset ='utf8')
            cursor = conn.cursor()
            query = """SELECT * FROM AppService.MEMBER WHERE user_id = '{0}';""".format(id_text)
            cursor.execute(query)
            result = cursor.fetchall()
            conn.commit()
            asdf=()

 
            if result == asdf:
                a.UserID.setText("Please Sign up in application")   
            else:    
                self.GUI_all()
    
        except:
            #respose 404
            print("server not connect")
        

    
    intro_stop = False
    swing_stop = False
    
    def GUI_all(self):
        self.ui = uic.loadUi('Designer_all.ui')
        #print("all"+str(threading.active_count()))
        self.ui.loadinglabel_2.hide()
        global ar_flag
        global intro_stop
        global swing_stop
        global cnt
        global light_stop
        
        light_stop=False
        
        ar_flag = 0
        self.end = Communicate()
        
        intro_stop = False
        swing_stop = False
        intro_thread = Video(self.ui,"golf_animation_intro.avi", self.ui.video_label, 1920, 1080, 0, lambda: intro_stop, self.end)
        swing_thread = Video(self.ui,"golf_animation_swing.avi", self.ui.video_label, 1920, 1080, 3, lambda: swing_stop, self.end)
        
        intro_thread.daemon = True
        swing_thread.daemon = True

        intro_thread.start()
        swing_thread.start()
        
        self.ui.show()

        light = self.end.cam_signal.connect(lambda: camera(self.end))
        self.end.light_signal.connect(lambda: impact_fram(cnt))
        self.end.end_signal.connect(self.GUI_loading)
        self.end.youngseon.connect(lambda: young(light))

    def GUI_loading(self):       
        self.ui.loadinglabel_2.show()
        print("loding" + str(threading.active_count()))

        self.end = Communicate()
        
        self.movie = QMovie(self.gifFile, QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.ui.loadinglabel.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()
        
        global Impact_frame
        if Impact_frame==0:
            self.GUI_fakeswing(self.end)
            return
        
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(3000, loop.quit)
        loop.exec_()
        
        main_Thread = MainThread(self.end)
        main_Thread.daemon = True
        main_Thread.start()
        
        self.end.main_signal.connect(self.GUI_feedback)
        

    def GUI_fakeswing(self,end):
        end.youngseon.emit()
        print(threading.active_count())
        global intro_stop
        global swing_stop
        global light_stop
        light_stop=True
        print(threading.active_count())
        intro_stop=True
        print(threading.active_count())
        swing_stop=True
        print(threading.active_count())
        
        self.ui = uic.loadUi('Designer_fakeswing.ui')
        self.ui.show()
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(3000, loop.quit)
        loop.exec_()
        self.GUI_all()
        
    
    marker_stop=False
    def GUI_feedback(self):
        self.ui = uic.loadUi('Designer_feedback.ui')
        self.end = Communicate()
        



        self.ui.show()

        
        self.ui.home.clicked.connect(lambda: self.feedback_clicked(1))
        self.ui.replay.clicked.connect(lambda: self.feedback_clicked(2))
        self.ui.feedback1.clicked.connect(lambda: self.feedback_clicked(3))
        self.ui.feedback2.clicked.connect(lambda: self.feedback_clicked(4))
        self.ui.feedback3.clicked.connect(lambda: self.feedback_clicked(5))

    
    def GUI_feedback1(self):
        self.ui = uic.loadUi('Designer_feedback1.ui')
        self.end = Communicate()
        
        global marker_stop
        global intro_stop
        global swing_stop

        intro_stop = True
        swing_stop = True
        marker_stop=False
        
        front_thread = Video(self.ui,"Camera1_out.avi", self.ui.front_label, 830, 700, 9, lambda: marker_stop, self.end)
        side_thread = Video(self.ui,"Camera2_out.avi", self.ui.side_label, 830, 700, 1, lambda: marker_stop, self.end)
        
        front_thread.daemon=True
        side_thread.daemon=True

        front_thread.start()
        side_thread.start()

        self.ui.show()
        
        self.textbox(self.ui.textBrowser,1)
        self.end.take_signal.connect(lambda: self.textbox(self.ui.textBrowser,2))
        self.end.top_signal.connect(lambda: self.textbox(self.ui.textBrowser,3))
        self.end.impact_signal.connect(lambda: self.textbox(self.ui.textBrowser,4))
        self.end.impact_signal.connect(lambda: self.textbox(self.ui.textBrowser,0))
        
        self.ui.skip_button.clicked.connect(self.feedback_clicked1)




    feedback_stop = False           
    def GUI_feedback2(self):
        self.ui = uic.loadUi('Designer_feedback2.ui')
        self.end = Communicate()
        
        global feedback_stop
        feedback_stop = False
    
        address_thread = Video(self.ui,"testing1.avi", self.ui.video1, 425, 530, 1, lambda: feedback_stop, self.end)
        backswing_thread = Video(self.ui,"testing2.avi", self.ui.video2, 425, 530, 1, lambda: feedback_stop, self.end)
        swing_thread = Video(self.ui,"testing3.avi", self.ui.video3, 425, 530, 1, lambda: feedback_stop, self.end)
        finish_thread = Video(self.ui,"testing4.avi", self.ui.video4, 425, 530, 1, lambda: feedback_stop, self.end)

        address_thread.daemon=True
        backswing_thread.daemon=True
        swing_thread.daemon=True
        finish_thread.daemon=True
        
        address_thread.start()
        backswing_thread.start()
        swing_thread.start()
        finish_thread.start()

        self.ui.show()


        self.textbox(self.ui.text1,1)
        self.textbox(self.ui.text2,2)
        self.textbox(self.ui.text3,3)
        self.textbox(self.ui.text4,4)

        self.ui.backButton.clicked.connect(self.feedback_clicked2)
    
    
    
    

    def GUI_feedback3(self):
        self.ui = uic.loadUi('Designer_feedback3.ui')
        self.end = Communicate()
        
        global feedback_stop
        feedback_stop = False
    
        address_thread = Video(self.ui,"master_out.avi", self.ui.video1, 911, 471, 1, lambda: feedback_stop, self.end)
        backswing_thread = Video(self.ui,"pelvis_out.avi", self.ui.video2, 911, 471, 1, lambda: feedback_stop, self.end)
        swing_thread = Video(self.ui,"Camera1_master_out.avi", self.ui.video3, 911, 471, 1, lambda: feedback_stop, self.end)
        finish_thread = Video(self.ui,"Camera1_pelvis_out.avi", self.ui.video4, 911, 471, 1, lambda: feedback_stop, self.end)


        address_thread.daemon=True
        backswing_thread.daemon=True
        swing_thread.daemon=True

        finish_thread.daemon=True
        
        address_thread.start()
        backswing_thread.start()
        swing_thread.start()
        finish_thread.start()

        self.ui.show()

        self.ui.backButton.clicked.connect(self.feedback_clicked3)

            
    def textbox(self, textBox, text):
        if text ==0:
            for i, val in enumerate(m.stands):
                textBox.append(val)
                textBox.show()
        elif text ==1:
            for i, val in enumerate(m.address_feedback):
                textBox.append(val)
                textBox.show()
        elif text ==2:
            for i, val in enumerate(m.backswing_feedback):
                textBox.append(val)
                textBox.show()
        elif text ==3:
            for i, val in enumerate(m.swing_feedback):
                textBox.append(val)
                textBox.show()
        elif text ==4:
            for i, val in enumerate(m.finish_feedback):
                textBox.append(val)
                textBox.show()

    


    def feedback_clicked(self,button):
        global feedback_stop
        feedback_stop = True
        self.ui.close()
        if button ==1:
            self.GUI_login()
        elif button ==2:
            self.GUI_all()
        elif button ==3:
            self.GUI_feedback1()
        elif button ==4:
            self.GUI_feedback2()
        elif button ==5:
            self.GUI_feedback3()



    def feedback_clicked1(self):
        global marker_stop
        marker_stop=True
        self.ui.close()
        self.GUI_feedback()

    def feedback_clicked2(self):
        global marker_stop
        marker_stop=True
        self.ui.close()
        self.GUI_feedback()

    def feedback_clicked3(self):
        global marker_stop
        marker_stop=True
        self.ui.close()
        self.GUI_feedback()
                    


if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myApp_step = MyWindow_step(gifFile)
    app.exec_()




   
