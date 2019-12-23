# -*- coding: utf-8 -*-
"""
@author: Square-Lee(LeeSeunghoon)

cv2를 사용하지 않고 회전시키는 방법을 문의하신 분이 있어 numpy로 회전시키는 법을 공유합니다.
변화를 명확히 확인하실수 있도록 cw/ccw로 함수를 나누어 작성하였지만, 
실제로 응용하실 때는 rot90함수만 단독으로 사용하여 4 ~ -4까지 값을 두번째 변수인자에 입력하시면 됩니다.
 
version info
1. Python 3.6(Anaconda 1.8.7)
2. numpy 1.16.2
3. re
"""

import numpy as np
import re


def cw_word_rotation(img, degree):
    
    if degree % 4 == 1:
        result = np.rot90(img,-1)
        #정방향으로 90도 회전
    elif degree % 4 == 2:
        result = np.rot90(img, -2)
        #정방향으로 180도 회전
    elif degree % 4 == 3:
        result = np.rot90(img, -3)
        #정방향으로 270도 회전     
    else:
        result = np.rot90(img, -4)
        #360도 회전

    return result    

def ccw_word_rotation(img, degree):
   
    if degree % 4 == 1:
        result = np.rot90(img, 1)
        #역방향으로 90도 회전(-90도)
    elif degree % 4 == 2:
        result = np.rot90(img, 2)
        #역방향으로 180도 회전
    elif degree % 4 == 3:
        result = np.rot90(img, 3)
        #역방향으로 270도 회전(-270도)        
    else:
        result = np.rot90(img, 4)
        #360도 회전 
    return result 

def Rotate(img,X):
    angle = int(re.findall("\d+", X)[0])/90
    #사용자가 입력한 값중 숫자만 검출하여 90으로 나눈 뒤 int형식으로 저장
        
    direction = " ".join(re.findall("[a-zA-Z]+", X))
    # 사용자가 입력한 값중 문자만 검출하여 변수로 저장
    if float(angle) - int(angle) == 0:
        
        if direction == 'cw':
            result = cw_word_rotation(img, angle)
        #저장된 문자 변수가 CW면 정방향 회전 실행
        
        elif direction == 'ccw':
            result = ccw_word_rotation(img, angle)
        #저장된 문자 변수가 CCW면 역방향 회전 실행
        
    else:
        result = '회전하실 각도와 방향을 [cw/ccw + 각도] 형식으로 정확히 입력해주십시오. ex.)cw90'
        #입력이 잘못된 경우 에러메세지 출력
        
    return result

def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y' :
        k = input("새로운 방향과 각도를 입력해주세요")
        ans = Rotate(img,k)
        print('입력한 각도와 방향 : ', k)
        print('결과 : ')
        print(ans)
        return 0
    elif reply[0] == 'n' :
        return 1
    else:
        return yes_or_no("다른 회전을 시도하시겠습니까? (y/n) ")

    
img = [['이','것','은','','그','림'], 
        ['입','니','다','모','든','글'],
        ['자','는','그','림','의','픽'],
        ['셀','값','입','니','다','~']]

print('초기상태 : ')
print(Rotate(img,'cw360'))
#초기상태 출력

X = input("회전하시겠습니까? cw/ccw + 각도형식으로 입력해주십시오")
Ans = Rotate(img,X)
print('입력한 각도와 방향 : ',X)
print('결과 : ')
print(Ans)
while True:
    
    if(yes_or_no('다른회전을 시도하시겠습니까?')):
        break
    #yes/no를 반복해 no를 답변할 때까지 반복
print("고생하셨습니다.")

    
    
            