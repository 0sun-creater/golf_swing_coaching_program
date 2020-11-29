import boto3
import sys
import os
import pymysql
import base64
import requests

from os import path
import cv2

from datetime import datetime




def connect_RDS(host,port,username,password,database):
    try:
        conn = pymysql.connect(host,user=username,passwd = password,db=database,
                              port=port,use_unicode=True,charset ='utf8')
        
        #cursor는 db와 sql문장을 주고받는 역할
        cursor = conn.cursor()
    
    except:
        logging.error("RDS에 연결되지 않았습니다.")
        sys.exit(1)
    
    return conn,cursor



def upload(id_text):
    #RDS info
    host = "" #rds endpoint
    port = 3306
    username = "" #rds만들 때 입력한 이름
    database = "" #RDS DB 내에서 연결하고 싶은 DB 이름
    password = ""# mysql pwd



    #call RDS
    conn, cursor = connect_RDS(host,port,username,password,database)



    video_name = "video" + datetime.now().strftime("%H%M%S") + ".mp4"
    image_name = video_name + "_i"
    video_date = datetime.now().strftime("%Y%m%d%H%M%S")

    video_query="""INSERT INTO AppService.VIDEO (user_id,video_name,image_name,video_date,video_location)
                VALUES('{0}','{1}', '{2}', '{3}','{4}');
                """.format(
                        id_text,video_name,image_name,video_date,'인천 연수구')



    #S3 클라이언트 생성
    s3 = boto3.client('s3')



    #업로드할 S3 버킷
    bucket_name = ''#버킷 이름



    #(로컬에서 올릴 파일이름, S3버킷이름, 버킷에 저장될 파일 이름)
    s3.upload_file('Camera1_master_out.avi',bucket_name,video_name)




    cursor.execute(video_query)    
    conn.commit()



