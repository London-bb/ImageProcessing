# -*- coding: utf-8 -*-
"""
#웹캠을 회전하고 크기를 변경
#@author: square-Lee (LeeSeunghoon)
"""

# version info
# python 3.6
# open cv 3.4.2
# numpy 1.16.2

import numpy as np
import cv2

user_vid = cv2.VideoCapture(0)
user_vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
user_vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#영상의 초기 해상도를 640*480으로 설정해줍니다.

while True:
    
        ret, Frame = user_vid.read()
        
        if ret:
            raw = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
            rotate_raw = cv2.rotate(raw,rotateCode = cv2.ROTATE_90_CLOCKWISE)
            resize_raw= cv2.resize(raw, None, fx= 0.5, fy= 0.5, interpolation=cv2.INTER_AREA)

            cv2.imshow('gray',raw)
            cv2.imshow('gray_rotate',rotate_raw)
            cv2.imshow('resize', resize_raw)

        else:
                print('에러가 발생하였습니다.')
                

        if cv2.waitKey(1) == 27 :
            #ESC누르면 while문 탈출
            break
            
    
user_vid.release()
cv2.destroyAllWidows()