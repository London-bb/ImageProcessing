# -*- coding: utf-8 -*-
"""
#웹캠을 입력받아 화면에 출력하는 코드
#@author: square-Lee (LeeSeunghoon)
"""

import numpy as np
import cv2
import math
from matplotlib import pyplot as plt


user_vid = cv2.VideoCapture(0)
user_vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
user_vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    
        ret, Frame = user_vid.read()
        
        if ret:
            raw = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
            blur=cv2.blur(raw,(5,5))
            cv2.imshow('gray',raw)
            cv2.imshow('original',Frame)
            cv2.imshow('buffer_vid',blur)

        else:
                print('에러가 발생하였습니다.')

        if cv2.waitKey(1) == 27 :
            break
            
    
user_vid.release()
cv2.destroyAllWidows()
    
#카메라에서 영상을 받아와 흑백 및 원본(color)영상을 재생하고, 
#동시에 재생되는 컬러영상을 저장
#ESC누르면 종료, ESC 누르지 않을경우 계속 화면 재생


    
    


    