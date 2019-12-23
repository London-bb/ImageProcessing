# -*- coding: utf-8 -*-
"""
#웹캠의 fps를 계산하고 영상과 함께 출력하는 방법
#@author: square-Lee (LeeSeunghoon)
"""

import numpy as np
import cv2
import math
import time

user_vid = cv2.VideoCapture(0)
user_vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
user_vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

prev_time=0
#영상의 재생시간을 구하기 위해 초기시간을 0으로 설정해줍니다.

while True:
    
        ret, Frame = user_vid.read()
        
        if ret:
            current_time = time.time()
            #time 라이브러리를 이용해 현재시간을 입력
            sec = current_time - prev_time
            #경과시간을 sec으로 저장
            prev_time = current_time

            vid_fps = 1/(sec)
            fps_str = "FPS : %0.1f" % vid_fps
            #영상의 프레임 계산
           
            cv2.putText(Frame, fps_str, (0,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
            #계산된 fps를 영상에 위치시킴

            cv2.imshow('fps', Frame)
            
        else:
                print('에러가 발생하였습니다.')

        if cv2.waitKey(1) == 27 :
            break
            
    
user_vid.release()
cv2.destroyAllWindows()
