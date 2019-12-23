# -*- coding: utf-8 -*-
"""
#slider를 이용해 다양한 상황에서 영상을 실시간으로 바꿔보자
#@author: square-Lee (LeeSeunghoon)
"""

import numpy as np
import cv2

def nothing(x):
    pass

def rescale(image,i, j):
    retval, rescale_image = cv2.threshold(image, i, j, cv2.THRESH_TOZERO_INV)
    #image의 픽셀값이 i 이상이면 0, 아니면 그대로
    reval2, rescale_image = cv2.threshold(rescale_image, j, i, cv2.THRESH_TOZERO)
    #rescale_image의 픽셀값이 j 이상이면 그대로 아니면 0
    
    return rescale_image
    #즉 return값은 i~j사이의 영역만 남는 영상이 됩니다.

cv2.namedWindow('control', cv2.WINDOW_NORMAL)
cv2.createTrackbar('High', 'control',0, 255, nothing)
cv2.setTrackbarPos('High', 'control', 68)
cv2.createTrackbar('Low', 'control',0, 255, nothing)
cv2.setTrackbarPos('Low', 'control', 2)

vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
        ret, frame = vid.read()
        key = cv2.waitKey(3)
        
        if ret:
            raw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            i = cv2.getTrackbarPos('High', 'control')
            j = cv2.getTrackbarPos('Low','control')

            threshold_img = rescale1(raw, i, j)
            cv2.imshow('control', threshold_img)

        else:
            print('에러가 발생하였습니다.')
            break
            #영상 입력이 잘못된경우 에러메세지 출력 및 종료
            
        if key == 27:
            break
            #ESC를 누르면 while문을 탈출한다.(실행종료)
    
     
vid.release()
cv2.destroyAllWindows()