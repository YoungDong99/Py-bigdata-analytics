"""
Numpy 패키지 
  - 수치 과학용 데이터 처리 목적으로 사용 
  - 선형대수(벡터, 행렬) 연산 관련 함수 제공 
  - N차원 배열, 선형대수 연산, 고속 연산  
  - 수학/통계 함수 제공 
  - indexing/slicing   
  - broadcast 연산
"""

import numpy as np # 별칭 


## 1. list 배열 vs Numpy 다차원 배열 

# 1) list 배열
lst = [1, 2, 3, 3.5] # 정수와 실수 자료형
print(lst) # 다양한 자료형
print(lst * 3 ) # 3번 반복
sum(lst) # 외부 함수 

# 2) Numpy 다차원 배열 
arr = np.array(lst) # array([list])  
type(arr)

print(arr) # 단일 자료형
print(arr * 0.5) # broadcast 연산 
arr.sum() # 자체 제공 



## 2. array() : list이용 다차원 배열 생성 
'''
형식) np.array(list [, dtype])
    dtype : int, float, bool, 생략 시 값으로 결정   
'''
lst1 = [3, 5.2, 4, 7]
print(lst1) # 단일 리스트 배열 

arr1d = np.array(lst1) # array(단일list)
print(arr1d.shape) # 자료구조 확인 : (4,)

print('평균 =', arr1d.mean()) 
print('분산=', arr1d.var())
print('표준편차=', arr1d.std()) 



## 3. broadcast 연산 
# - 작은 차원이 큰 차원으로 늘어난 후 연산 

# 상수(scala) vs 1차원(vector)
print(0.5 * arr1d)


'''
broadcast 연산 예 
표본 분산 = sum((x - x_bar)**2) / n-1

(x - x_bar) : x배열 - x산술평균
'''

# 학생 5명 점수 표준편차 
x = np.array([65, 82, 55, 76, 78]) # 5명 점수 : 변수 x  
x_bar = x.mean() # 평균 = 71.2  
var = sum((x - x_bar)**2) / (len(x)-1) # 분산 
std = np.sqrt(var) # 표준편차 
print('표준편차 =', round(std, 3))


## 4. 순차적인 값으로 다차원 배열 생성 
'''
형식) numpy.arange([start=0, ] stop [, step=1, dtype = float64]) : 순차적인 값으로 생성

range(start=0, stop, step=1) : 10진수 정수 수열 
'''
range(0, 10) # 0 ~ 9
#range(-1.0, 10)

arr = np.arange(-1.2, 5.5) # 실수 사용 가능  
print(arr) # [-1.2 -0.2  0.8  1.8  2.8  3.8  4.8]

# ex) x의 수열에 대한 2차 방정식 
x = np.arange(-1.0, 2, 0.1) # (start, stop, step)
x.min() # -1.0
x.max() # 1.8999
len(x) # 30


# fx함수 : x -> y 
def fx(x) :
    #y = 2*x + 3 # 1차방정식(직선) 
    #y = x**2 + 2*x + 3 # 2차방정식(U곡선) 
    y = x**3 + x**2 + 3*x + 4 # 3차방정식(S곡선)
    return y
    

 # f(x) 함수 
y = [fx(i) for i in x] 
print(y)

import matplotlib.pyplot as plt 

plt.plot(x, y)
plt.show()


## 5. 다차원 배열의 기본 속성
'''
ndim : 차원(축)의 수
shape : 각 차원의 크기
size : 전체 요소의 개수
dtype : 요소의 데이터 타입
itemsize : 각 요소의 바이트 크기
'''
print('차원 :', arr.ndim)
print('차원의 크기 :', arr.shape)
print('원소의 개수 :', arr.size)
print('데이터 타입 :', arr.dtype)
print('각 원소의 바이트 크기 :', arr.itemsize)





