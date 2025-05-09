"""
random 모듈
 - 난수 생성 함수 제공 
"""

import numpy as np # 난수 모듈  
import matplotlib.pyplot as plt # 그래프


# random 모듈의 난수 관련 함수 
dir(np.random)
'''
binomial : 이항분포(이산확률)
choice : a에서 size만큼 선택 
gamma : 감마분포(연속확률) 
normal : 정규분포(연속확률)  
poisson : 포아송분포(이산확률) 
rand : 0 ~ 1 실수 
randint : a ~ b 정수(이산확률) 
randn : 표준정규분포(연속확률)  
random : 0 ~ 1 실수 
sample : 표본추출 
seed : 시드값    
shuffle : 행 단위 섞기 
uniform : 균등분포(연속확률)  
'''


## 1. 난수 실수와 정수  

# 1) 난수 실수 
data = np.random.rand(5, 3) # (행, 열)
print(data)

# 차원 모양
print(data.shape) # (5, 3) 

# 난수 통계
print(data.min()) 
print(data.max()) 
print(data.mean()) 

# 2) 난수 정수  
data = np.random.randint(165, 175, size=50) # (행, 열)
print(data)

# 차원 모양
print(data.shape) # (50,)

# 난수 통계
print(data.min()) 
print(data.max()) 
print(data.mean()) 



## 2. 이항분포 
np.random.seed(12)
np.random.binomial(n=1, p=0.5, size=10)  
'''
n : 시행횟수
p : 성공확률
size : 표본수
'''
# [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]

np.random.binomial(n=10, p=0.5, size=10) 
# [4, 5, 7, 7, 1, 5, 5, 5, 6, 3]  -> 10번던져서 성공한 횟수


## 3. 정규분포
height = np.random.normal(173, 5, 2000)   # (mu, sigma, size)
print(height) # (2000,)

height2 = np.random.normal(173, 5, (500, 4))
print(height2) # (500, 4)


# 난수 통계
print(height.mean()) 
print(height2.mean()) 

# 정규분포 시각화 
plt.hist(height, bins=100, density=True, histtype='step')
plt.show()


## 4. 표준정규분포 : mu=0, sigma=1
standNormal = np.random.randn(500, 3) # 500x3
print(standNormal.mean())



# 정규분포 시각화 
plt.hist(standNormal[:,0], 
         bins=100, density=True, histtype='step', label='col1')
plt.hist(standNormal[:,1], 
         bins=100, density=True, histtype='step', label='col2')
plt.hist(standNormal[:,2], 
         bins=100, density=True, histtype='step',label='col3')
plt.legend(loc='best')
plt.show()


## 5. 균등분포 
uniform = np.random.uniform(10, 100, 1000)
plt.hist(uniform, bins=15, density=True)
plt.show()





