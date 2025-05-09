"""
reshape : 모양 변경(크기변경 불가)
resize : 크기 변경
-> 이미지 규격화 : 데이터 학습을 위한 전처리 작업
"""

import numpy as np 
import matplotlib.pyplot as plt 

from PIL import Image # PIL(Python Image Lib) 


## 1. image resize
path = r"C:\ITWILL\5_Python_ML\data\numpy" # 이미지 경로  

# 1) image read 
img = Image.open(path + "/test1.jpg") 
np.shape(img) # 원본이미지 모양 : (360, 540, 3) : (세로, 가로, 칼럼)
type(img)  # PIL.JpegImagePlugin.JpegImageFile

# 2) image resize 
img_re = img.resize( (150, 100) ) # (가로, 세로)
np.shape(img_re) # (100, 150, 3)
plt.imshow(img_re)
plt.show()



## 2. 폴더 전체 이미지 resize 
from glob import glob # 파일 검색 패턴 사용(문자열 경로, *, ? 사용) 


img_resize = [] # image 저장 

# glob() 함수 : 파일 검색 패턴 지정
for file in glob(path + '/*.jpg'): # 파일 패턴 대체 : jpg 파일 검색    
    print(file)
    
    
    img = Image.open(file) # image 읽기 
    
    img = img.resize((150, 100)) # 크기 변경(가로, 세로) 
    
    img_data = np.array(img) # 다차원배열 변경      
   
    img_resize.append(img_data)  # list append
    

len(img_resize)  # 3

img_resize_arr = np.array(img_resize)

img_resize_arr.shape  # 4d : (3, 100, 150, 3)  :  (size, h, w, c)


# 첫번째 이미지

img_resize_arr[0]

for i in range(len(img_resize)) :
    print(img_resize_arr[i].shape)
    plt.imshow(img_resize_arr[i])
    plt.show()


    
    
 


