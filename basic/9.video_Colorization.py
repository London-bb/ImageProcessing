# -*- coding: utf-8 -*-
"""
#웹캠을 활용한 영상처리 후(grayscale) 다양한 색깔을 입혀보자 
#gray2color(bgr,hsv etc)하는 방법에는 다양한 방법이 있습니다.
#이 예제에서는 1) cv2의 내장함수를 이용하는 방법, 2) Look Up Table을 이용하는 방법
#두가지를 확인하실 수 있습니다.
#LUT은 작성자가 직접 데이터값을 설정하여 화소 단위 처리가 가능하다는 장점이 있습니다.
#@author: square-Lee (LeeSeunghoon)
"""

import numpy as np
import cv2
import math
import time

user_vid = cv2.VideoCapture(0)
user_vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
user_vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def nothing(x):
    pass

def rescale(image,i, j):
    retval, rescale_image = cv2.threshold(image, i, j, cv2.THRESH_TOZERO_INV)
    #image의 픽셀값이 i 이상이면 0, 아니면 그대로
    reval2, rescale_image = cv2.threshold(rescale_image, j, i, cv2.THRESH_TOZERO)
    #rescale_image의 픽셀값이 j 이상이면 그대로 아니면 0
    
    return rescale_image
    #즉 return값은 i~j사이의 영역만 남는 영상이 됩니다.
 
def applyCustomColormap(image):
    
    lut = np.zeros((256, 1, 3), dtype=np.uint8)
    
    lut[:, 0, 2] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55,55,55,55,55,55,55,55,55,
       55,55,55,55,55,55,55,109,109,109,109,109,109,109,109,109,109,109,109,109,
       109,109,109,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,
       11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,65,65,65,65,65,65,65,65,
       65,65,65,65,65,65,65,65,119,119,119,119,119,119,119,119,119,119,119,119,
       119,119,119,119,173,173,173,173,173,173,173,173,173,173,173,173,173,173,
       173,173,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
       255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
       255,255,255,255,255,255,255,255,255,255,255,255,255,255,237,237,237,237,
       237,237,237,237,237,237,237,237,237,237,237,237,255,255,255,255,255,255,
       255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
       255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
       255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
       255,255,255,255,255]
    #R components
    lut[:, 0, 1] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,162,162,162,162,162,162,162,162,162,162,162,162,162,162,162,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,201,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,223,223,223,223,223,223,223,223,223,223,223,223,223,223,223,223,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #G components
    lut[:, 0, 0] = [237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,237,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,166,166,166,166,166,166,166,166,166,166,166,166,166,166,166,166,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #B components
    colorimage = cv2.LUT(image, lut)
    
    return colorimage

#영상의 재생시간을 구하기 위해 초기시간을 0으로 설정해줍니다.
prev_time=0

#영상의 평균을 구하기위한 mean filter 생성, 5x5사이즈 사용
mean_mask = np.array((
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]), dtype="int")/25

cv2.namedWindow('colorize_cv2', cv2.WINDOW_NORMAL)
cv2.createTrackbar('High', 'colorize_cv2',0, 255, nothing)
cv2.setTrackbarPos('High', 'colorize_cv2', 68)
cv2.createTrackbar('Low', 'colorize_cv2',0, 255, nothing)
cv2.setTrackbarPos('Low', 'colorize_cv2', 2)

cv2.namedWindow('colorize_LUT', cv2.WINDOW_NORMAL)
cv2.createTrackbar('High', 'colorize_LUT',0, 255, nothing)
cv2.setTrackbarPos('High', 'colorize_LUT', 68)
cv2.createTrackbar('Low', 'colorize_LUT',0, 255, nothing)
cv2.setTrackbarPos('Low', 'colorize_LUT', 2)
while True:
    
        ret, Frame = user_vid.read()
        
        if ret:
            raw = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
            
            i = cv2.getTrackbarPos('High', 'colorize_cv2')
            j = cv2.getTrackbarPos('Low','colorize_cv2')
            x = cv2.getTrackbarPos('High', 'colorize_LUT')
            y = cv2.getTrackbarPos('Low','colorize_LUT')
            
            img_for_zet = rescale(raw, i, j)
            img_for_LUT = rescale(raw, x, y)
            #cv2.applyColorMap 함수를 사용할 경우 grayscale 영상에 바로 적용합니다. 영상의 인자는 다양하며 Note 1)을 확인하시기 바랍니다.
            #If you use the cv2.applyColorMap function, apply it directly to the grayscale image. Please check factors in Note 1.
            #Note 1) https://docs.opencv.org/2.4/modules/contrib/doc/facerec/colormaps.html
            zet_img = cv2.applyColorMap(img_for_zet.astype('uint8'), cv2.COLORMAP_JET)

            #LUT을 사용할 경우 영상을 BGR(3D array)로 변환시켜줄 필요가 있습니다.
            #When using LUT, you need to convert the images to BGR.
            img = cv2.cvtColor(img_for_LUT.astype('uint8'), cv2.COLOR_GRAY2BGR)
            LUT_img = applyCustomColormap(img)
            
            #slider를 이용해 자유롭게 값을 옮겨가며 두 영상의 유사성과 차이를 확인해 보시기 바랍니다.
            #Use the slider to move the values freely to see the similarities and differences between the two images.
            cv2.imshow('raw',raw)
            cv2.imshow('colorize_cv2', zet_img)
            cv2.imshow('colorize_LUT', LUT_img)
            
        else:
                print('에러가 발생하였습니다.')

        if cv2.waitKey(1) == 27 :
            break
            
    
user_vid.release()
cv2.destroyAllWindows()
