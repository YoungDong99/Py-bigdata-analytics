"""
indexing/slicing 
 - 1차원 indexing 
 - 2,3차원 indexing 
 - 조건(boolean) indexing  
"""

import numpy as np

## 1. 색인(indexing) 

# 1) list 배열 색인
ldata = [0,1,2,3,4,5]
print(ldata[:]) # 전체 원소 
print(ldata[3]) # 특정 원소 1개 
print(ldata[:3]) # 범위 선택 (0~n-1)
print(ldata[-1]) # 오른쪽 기준(-)

# 2) numpy 다차원 배열 색인 : list 동일 
arr = np.arange(10) # 0~9
print(arr[:])
print(arr[3])
print(arr[:3])
print(arr[-1])


## 2. slicing : 특정 부분을 잘라서 new object
arr = np.arange(10) # 0~9

# 주소 복사 
arr_obj = arr[1:4]  # slicing
print(arr_obj) # [1 2 3]

arr_obj[:] = 100 # 전체 수정
print(arr_obj) # [100 100 100]

print(arr) # 원본 수정 

# 내용 복사 
arr_obj = arr[1:4].copy() # slicing
arr_obj[:] = [1,2,3] # 내용 수정 

arr # 원본 영향 없음 


## 3. 고차원 색인(indexing)

# 1) 2차원 indexing : 행,열
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 중첩list
print(arr2d)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

# 행 index(기본)
print(arr2d[0, :]) # 1행 전체 
print(arr2d[0])  # 1행 전체
print(arr2d[1:,1:])
print(arr2d[::2]) # 홀수행 선택 : [start:stop:step] 

# 비연속 행렬
print(arr2d[[0,2]])  # 1행, 3행 선택 


# 2) 3차원 indexing : 면,행,열
arr3d = np.array([[[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]]) # 3중list 
print(arr3d)
'''
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
'''
print(arr3d.shape)  # (2, 2, 3)

# 면 index(기본)
print(arr3d[0]) # 1면 전체 
print(arr3d[0, 1])  # 1면의 1행 전체 
print(arr3d[0, 1, 1:])  # 1면 1행 2~3열 


## 4. 조건식 색인(boolean index)
dataset = np.random.randn(3, 4) # 12개 
print(dataset)


# 0.7 이상 경우 
print(dataset[dataset >= 0.7])

# 0.1 ~ 1.5 범위 
result = dataset[(dataset >= 0.1) & (dataset <= 1.5)]
print(result) 

'''
논리연산자 기호 : &(and), |(or), ~(not) 
'''


## 5. 팬시 인덱싱(Fancy Indexing) 
'''
배열 인덱스에 다른 배열의 값을 적용하여 원하는 요소를 선택하는 방법
'''
fidx = dataset >= 0.7 # True or False

result = dataset[fidx] # True인 값의 원소만 출력
print(result) 







