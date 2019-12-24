# -*- coding: utf-8 -*-
"""
#cv2.Imwrite 함수 사용시 한국어가 경로에 있거나, 저장하는 이름이 한국어로 되어 있는 경우 저장이 되지 않는 경우나 에러메세지가 발생하는 경우가 있습니다.
#이것은 한글의 형식이 unicode이기 때문입니다.(python open cv는 unicode를 처리하지 못합니다.)
#이에 대한 좋은 해법을 아래와 같은 출처를 통해 구할 수 있었고, 많은 분들이 어려움을 겪고 계실 것으로 생각되어 출처와 함께 공유해드립니다.
# 출처 : https://jangjy.tistory.com/m/337 

#@author: square-Lee (LeeSeunghoon)
"""

import numpy as np
import cv2
import math
import time
import getpass
import os
import datetime

user_vid = cv2.VideoCapture(0)
user_vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
user_vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#영상이 저장될 폴더를 만드는 함수
#function that creates a folder in which images will be stored.
#실행될때마다 동일한 폴더가 생성되지 않도록 동일한 이름의 폴더 유무를 확인 후 없는 경우만 폴더 생성
#Create a folder only if it does not exist.

def make_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

def imwrite_kor(name, img, params=None):
    try:
        ext = os.path.splitext(name)[1]
        result, n = cv2.imencode(ext, img, params)
        #한글 경로를 인식할 수 있도록 imencode함수를 사용해 저장
        #imencode(buffer,flags)
        #buffer : 배열 또는 바이트 벡터 형태 입력
        #flags : 읽어들이는 이미지 이름

        if result:
            with open(name,mode='w+b') as f:
                n.tofile(f)
            return True
        
        else:
            return False
        
    except Exception as e:
        print(e)
        return False
    
#이미지가 저장되는 날짜 확인
#check system date
now = datetime.datetime.now().strftime("%Y-%m-%d")

#시스템 사용자의 컴퓨터 ID 확인
#check your user name
user_name = getpass.getuser()
        
#폴더 생성 주경로를 사용자의 배경화면으로 설정
#Set directory to the user's background screen

folder_root =  'C:/Users/' + user_name + '/Desktop/'
path = folder_root + now
        
#폴더 생성
#create folder
make_folder(path)

#영상의 재생시간을 구하기 위해 초기시간을 0으로 설정해줍니다.
#Set the initial time : 0
prev_time=0

#연속저장 시 번호를 메겨 저장할 수 있도록 카운트 변수를 만들어줍니다.
#Set the capture count : 0

capture_count = 0
while True:
    
        ret, Frame = user_vid.read()

        #keyboard 이벤트를 위해 초기 cv2.waitkey를 지정해줍니다.
        #set cv2.waitkey to use keyboard interrupt
        key = cv2.waitKey(3)

        if ret:
            current_time = time.time()
            sec = current_time - prev_time
            prev_time = current_time

            vid_fps = 1/(sec)
            fps_str = "FPS : %0.1f" % vid_fps
            
            cv2.putText(Frame, fps_str, (0,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
            
            cv2.imshow('fps', Frame)
            
        else:
                print('에러가 발생하였습니다.')

        if key == 27 :
            break
        
        #키보드의 C를 누르면 사진이 저장됩니다.
        #video capture(Snapshot) when press 'C' on your keyboard
        elif key == ord('c'):
            print('사진 저장')
            capture_count = capture_count+1
            
            imwrite_kor(os.path.join(path, '촬영'+ str(capture_count) + '.bmp'), Frame)
            
    
user_vid.release()
cv2.destroyAllWindows()
