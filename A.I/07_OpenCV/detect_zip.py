#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import matplotlib.pyplot as plt

def detect_zipno(fname):
    
    # 이미지를 읽어옵니다.
    img = cv2.imread(fname)
    
    # 이미지의 높이와 너비를 구합니다.
    h, w = img.shape[:2]
    
    # ???
    img = img[0:h//2, w//3:]
    
    # 이미지를 그레이 스케일로 바꿔줍니다.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 가우시안 블러로 노이즈를 줄여줍니다.
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    
    # 노이즈를 줄인 이미지를 이진화 처리해줍니다.
    im2 = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)[1]
    
    # 단순윤곽을 검출합니다.
    cnts = cv2.findContours(im2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
    
    # result 리스트를 만들어줍니다.
    result = []
    
    # contour들의 정보를 구합니다.
    for cnt in cnts:
        
        # boundingRect함수를 통해서 x, y, w, h를 구합니다.
        x, y, w, h = cv2.boundingRect(cnt)
        
        # 너비가 50 아래거나 70을 넘는 contour만 구합니다.
        if not(50 < w < 70): continue
            
        # 리스트에 x, y, w, h 추가해줍니다.
        result.append([x, y, w, h])
    
    # result를 정렬해줍니다.
    result = sorted(result, key=lambda x: x[0])
    
    # result2라는 리스트를 만들어 줍니다.
    result2 = []
    
    # ???
    lastx = -100
    
    # ???
    for x, y, w, h in result:
        if (x - lastx) < 10: continue
        result2.append([x, y, w, h])
        lastx = x
    
    # result2에 있는 좌표들로 사각형을 그려줍니다.
    for x, y, w, h in result2: 
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
    # result2와 img를 반환해줍니다.
    return result2, img

# 
if __name__ == '__main__': # ???
    cnts, img = detect_zipno('hagaki1.png')
    
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.savefig('detect-zip.png', dip=200)
    plt.show()

