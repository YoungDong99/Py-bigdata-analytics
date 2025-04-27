"""
Numpy 패키지 
  - 수치 과학용 데이터 처리 목적으로 사용 
  - 다차원 배열, 고속 연산  
  - 수학/통계 함수 제공 
  - 배열 vs 배열 연산 : broadcast연산 
"""

import numpy as np # 별칭 
import statistics as st # mean

# 1. list 배열 vs 다차원 배열 

# 1) list 배열
lst = [1, 2, 3, 3.5] # 정수와 실수 자료형
print(lst) # 다양한 자료형
sum(lst) # 9.5 : 외부 함수 
st.mean(lst)

# list 색인
lst[0] # 1


# 2) 다차원 배열 
arr = np.array(lst) # array([list])  
dir(arr)
'''

'''

print(arr) # 단일 자료형 (원소에 실수가 하나라도 있으면 전부 실수형으로 단일화)
arr.sum() # 9.5 : 자체 제공 
arr.mean() # 2.375 : 자체 제고ㅓㅇ
arr[0]

print(type(arr))



# 2. array() : 다차원 배열 생성 

# 1) 단일 list  
lst1 = [3, 5.2, 4, 7]
print(lst1) # 단일 리스트 배열 

# list -> 다차원배열
arr1d = np.array(lst1) 
print(arr1d.shape) # 자료구조 확인 : (4,) -> 1차원(4개원소)

# 2) 중첩list -> 2차원 배열 
lst2 = [[1,2,3,4], [5,6,7,8]]
print(lst2)

# list -> 다차원배열
arr2d = np.array(lst2) 
print(arr2d.shape) # 자료구조 확인 : (2, 4) -> 2차원(행, 열)
print(arr2d)
'''
[[1 2 3 4]
 [5 6 7 8]]
'''

# 3. broadcast 연산 : 배열 간 사칙연산  
#print(0.5 * lst1)  # TypeError : 배열에 산술 연산 불가

print(0.5 * arr1d)
'''
[1.5 2.6 2.  3.5]
'''

print(0.5 * arr2d)
'''
[[0.5 1.  1.5 2. ]
 [2.5 3.  3.5 4. ]]
'''
print(arr1d * arr2d) 
'''

'''


'''
예) 표본 분산 = sum((X-산술평균)**2) / n-1
'''
X = [1,2,3,4,5] # list
x = np.array(X)
type(x)

x_bar = x.mean()  # x의 평균
n = len(x)

std = sum((x-x_bar)**2) / (n-1)
print('표본 표준편차 =', std)  # 2.5


# 4. zeros or ones : 초기값 지정 행열 만들기
zerr = np.zeros( (3, 10) ) # 3행10열 (내부속성:튜플)
print(zerr) # 희소행렬 : doc(3) vs word(10) 빈도수 
'''
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
'''

onearr = np.ones( (3, 10) ) # 3행10열 
print(onearr)
'''
[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
'''



## 추가) object 배열
listo = [[1,2,3,4], [5,6,7]]
arro = np.array(listo)  # ValueError : 내부 리스트 길이가 달라 생성 불가

# 내부 리스트가 객체로 들어간 배열 생성
arro = np.array(listo, dtype=object)
print(arro)  # [list([1, 2, 3, 4]) list([5, 6, 7])]
print(arro.shape)  # (2,) -> 내부 리스트들을 각각 하나의 객체로 간주해서 1차원 배열


