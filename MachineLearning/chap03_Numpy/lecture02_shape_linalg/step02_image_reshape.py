"""
이미지 reshape
"""

import matplotlib.pyplot as plt  # image show
from sklearn.datasets import load_digits  # dataset load



## 1. image shape & reshape

# 1) dataset load 
digits = load_digits() # 10진수 숫자 필기체 이미지(머신러닝 모델에서 사용되는 데이터셋) 

'''
X변수(입력) : 10진수 숫자(0~9)에 대한 필기체 이미지 픽셀(digit)  
y변수(정답) : 10진 정수
'''
X = digits.data # 입력변수(X) 추출 
y = digits.target # 출력변수(y) 추출 
print(X.shape)


# 2) image reshape 
first_img = X[0].reshape(8,8) # 모양변경 
first_img.shape # (8, 8)


# 3) image show 
plt.imshow(X=first_img, cmap='gray')
plt.show()

y[0]  # 정답 : 0


# 마지막 이미지
last_img = X[-1].reshape(8,8)

plt.imshow(X=last_img, cmap='gray')
plt.show()

y[-1]  # 정답 : 8



## 2. image file read & show
import matplotlib.image as img # 이미지 읽기 

# image file path 
path = r"C:\ITWILL\5_Python_ML\data\numpy" # 이미지 경로 


# 1) image 읽기 
img_arr = img.imread(path + "/test1.jpg")
print(img_arr)
type(img_arr)

img_arr.shape # (360, 540, 3)

img_red = img_arr[:,:,0]
img_green = img_arr[:,:,1]
img_blue = img_arr[:,:,2]

print(img_red)
print(img_green)
print(img_blue)


# 2) image 출력 
plt.imshow(img_arr)
plt.show()







