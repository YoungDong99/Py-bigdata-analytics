"""
reshape : 모양 변경 
 - 1차원 -> 2차원 
 - 2차원 -> 다른 형태의 2차원  
T : 전치행렬 
swapaxis : 축 변경 
transpose : 축 번호 순서로 구조 변경 
"""

import numpy as np

# 1. 모양변경
lst = list(range(1, 13)) # 1차원 배열
lst # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

arr2d = np.array(lst).reshape(3, 4) # 모양변경(길이 변경 불가)
print(arr2d)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''
arr2d.shape # (3, 4)

print(arr2d.reshape(2,2,3))
'''
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
'''

# 2. 전치행렬
print(arr2d.T)
'''
[[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]
'''

print(arr2d.T.shape) # (4, 3)

# 3. swapaxes : 축 변경 
print('swapaxes')
print(arr2d.swapaxes(0, 1))  # 2차원일경우 전치행렬과 결과동일

print(arr2d.reshape(2,2,3).swapaxes(1,0))
'''  3차원 축변경
[[[ 1  2  3]
  [ 7  8  9]]

 [[ 4  5  6]
  [10 11 12]]]
'''

# 4. 1차원 배열로 차원 변경 
arr1d = np.ravel(arr2d)
print(arr1d) # [ 1  2  3  4  5  6  7  8  9 10 11 12]
 

# 5. transpose
'''
3차원 : 축 순서를 이용하여 자료 구조 변경 
'''
arr3d = np.arange(1, 25).reshape(4, 2, 3)#(4면2행3열)
print(arr3d)
print(arr3d.shape) 

# default : (면,행,열) -> (열,행,면)
arr3d_def = arr3d.transpose()  # transpose 기본값 (2,1,0) 생략
print(arr3d_def.shape)  # (3, 2, 4)
print(arr3d_def)  
'''
[[[ 1  7 13 19]
  [ 4 10 16 22]]

 [[ 2  8 14 20]
  [ 5 11 17 23]]

 [[ 3  9 15 21]
  [ 6 12 18 24]]]
'''

# (면:0, 행:1, 열:2) -> (행:1, 열:2, 면:0)
arr3d_user = arr3d.transpose(1,2,0)
arr3d_user.shape # (2, 3, 4)
print(arr3d_user)
'''
[[[ 1  7 13 19]
  [ 2  8 14 20]
  [ 3  9 15 21]]

 [[ 4 10 16 22]
  [ 5 11 17 23]
  [ 6 12 18 24]]]
'''

