# -*- coding: utf-8 -*-
"""
#영상에 threshold를 걸어 영상처리하기.
#@author: square-Lee (LeeSeunghoon)
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

vid = cv2.VideoCapture(0)

while True:
        ret, frame = vid.read()
        
        if ret:
            raw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            ret2, thresh1 = cv2.threshold(raw,127,255, cv2.THRESH_BINARY)
            ret2, thresh2 = cv2.threshold(raw,127,255, cv2.THRESH_BINARY_INV)
            ret2, thresh3 = cv2.threshold(raw,127,255, cv2.THRESH_TRUNC)
            ret2, thresh4 = cv2.threshold(raw,127,255, cv2.THRESH_TOZERO)
            ret2, thresh5 = cv2.threshold(raw,127,255, cv2.THRESH_TOZERO_INV)

            titles =['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
            images = [raw,thresh1,thresh2,thresh3,thresh4,thresh5]

            for i in range(6):
	            plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	            plt.title(titles[i])
	            plt.xticks([]),plt.yticks([])

            plt.show()