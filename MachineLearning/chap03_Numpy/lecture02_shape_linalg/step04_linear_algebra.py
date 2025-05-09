"""
 선형대수 관련 함수 
  - 수학의 한 분야 
  - 벡터 또는 행렬을 대상으로 한 연산
  - 응용 : 차원 축소, 행렬 분해(특이값 추출), 코사인 유사도
"""

import numpy as np 

 
## 1. 단위행렬 : 대각원소가 1이고, 나머지는 모두 0인 n차 정방행렬
eye_mat = np.eye(3) 
print(eye_mat)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''


# 정방행렬 x
x = np.arange(1,10).reshape(3,3)
print(x)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''


## 2. 대각성분 추출 : 정분류 빈도수 
diag_vec = np.diag(x)
print(diag_vec) # 대각성분 : [1 5 9]


## 3. 대각합 : 정방행렬의 대각에 위치한 원소들의 합 
trace_scala = np.trace(x) 
print(trace_scala) # 15


## 4. 대각행렬(diagonal matrix) : 대각성분 이외의 모든 성분이 0인 n차 정방행렬
diag_mat = eye_mat * diag_vec
print(diag_mat)
'''
[[1. 0. 0.]
 [0. 5. 0.]
 [0. 0. 9.]]
'''


## 5. 행렬식(determinant) : 대각원소의 곱과 차 연산으로 상수 반환 
'''
 용도 : 역행렬 존재 여부, 행렬식이 0이 아닌 경우 벡터들이 선형적으로 독립 
'''

x = np.array([[3,4], [1,2]])
print(x)
'''
[[3 4]
 [1 2]]
'''

# 선행대수 관련 함수
dir(np.linalg) 
'''
det : 행렬식 
inv : 역행렬 
norm : 노름(벡터 크기)
solve : 연립방정식 해 
svd : 특이값분해 
'''

det = np.linalg.det(x) # numpy.모듈.선형대수함수()
print(det)   # 2.0



## 6. 역행렬(inverse matrix) : 행렬식의 역수와 정방행렬 곱 
'''
용도 : 회귀 분석에서 최소 제곱 추정
    회귀방정식 :  y = X * a(기울기)
    최소 제곱 추정 : 손실를 최소화하는 기울기를 찾는 역할      
'''

inv_mat = np.linalg.inv(x) # numpy.모듈.선형대수함수()
print(inv_mat)
'''
[[ 1.  -2. ]
 [-0.5  1.5]]
'''



## 7. 행렬곱 : 행렬 vs 행렬 곱셈 연산
'''
  - 행렬의 선형결합  : 차원축소 
  - 회귀방정식 계산 : y = X변수 * a(기울기)   
  - 코사인 유사도 계산 
'''
  
A = np.array([1, 2, 3]).reshape(3,1) # 행렬A
B = np.array([2, 3, 4]).reshape(3,1) # 행렬B

A.shape # (3, 1)
B.shape # (3, 1)

A @ B # ValueError


# 1) 행렬내적 : 상수(dot) 반환 

AT = A.T # 전치행렬 : (3, 1) -> (1, 3)
AT.shape # (1, 3)

# 행렬내적 : 기호 표현  
AT @ B  # [[20]]  


# 행렬내적 : 함수 표현  
dot1 = AT.dot(B) # np.dot(AT, B)


# 2) 행렬외적 : 행렬 반환 

BT =  B.T # 전치행렬 

# 행렬외적 : 기호 표현 
A @ BT


# 행렬외적 : 함수표현 
dot2 = A.dot(B.T) 

'''
행렬곱 전제조건 
1. A, B 모두 행렬 
2. A행의 열의차원 = B행렬의 행의차원 
'''


##############################
## 코사인 유사도 예 : ppt.64
##############################

# 노름(norm) : 벡터 크기 
A_norm = np.linalg.norm(A) # 3.7416573867739413
B_norm = np.linalg.norm(B) # 5.385164807134504


# 코사인 유사도 
cosine_sim = (A.T @ B) / (A_norm * B_norm)

print(cosine_sim.reshape(1))  # [0.99258333]


