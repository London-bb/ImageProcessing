# -*- coding: utf-8 -*-
"""
#웹캠의 영상 일부분을 마우스로 잘라내기(크롭)하여 활용해보자
#@author: square-Lee (LeeSeunghoon)
"""

import numpy as np
import cv2

user_vid = cv2.VideoCapture(0)
user_vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
user_vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

mouse_is_pressing = False
clicked_x, clicked_y = 1, 1

def mouse_callback(event, x, y, flags, param):
    global clicked_x, clicked_y,mouse_is_pressing

    if event == cv2.EVENT_LBUTTONDOWN:

        mouse_is_pressing = True
        clicked_x, clicked_y = x, y
        #마우스를 클릭했을때부터 좌표가 찍히도록 설정합니다.
        #set x,y when u click somewhere image

    elif event == cv2.EVENT_LBUTTONUP:

        mouse_is_pressing = False 
        roi = raw[ clicked_y:y, clicked_x:x ]
        #마우스로 선택한 raw의 특정 영역만을 가져옵니다. 
        #crop image where u drag

        #이 공간에 크롭된 영상을 처리하는 다양한 함수와 방식을 입력하면됩니다.
        #Enter various functions and methods for processing cropped images in this space.
        
        cv2.imshow('crop',roi) 

while True:
    
        ret, Frame = user_vid.read()
        key = cv2.waitKey(3)
        if ret:
            raw = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('raw',raw)
            cv2.setMouseCallback('raw', mouse_callback)

        if key == 27:
                break
        
user_vid.release()
cv2.destroyAllWindows()    