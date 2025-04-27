"""
문1) 다음과 같은 data와 base를 대상으로 numpy의 broadcast 연산 방식을 적용하여     
     유클리드 거리계산식으로 두 자료의 거리를 단계별로 구하시오.
     
     유클리드 거리계산식 = sqrt( sum((p - q)^2) )
"""

import random # 난수 생성 
from statistics import sqrt # 제곱근

random.seed(100) # 난수 seed값 지정 

### 단계1. data 생성 
# 1) 대상 데이터 1개  
data = [round(random.random(),5), round(random.random(),5)]

# 2)기준 데이터 1개 
base = [round(random.random(),5), round(random.random(),5)]

print('data :', data) # data : [0.14567, 0.45493]
print('base :', base) # base :  [0.77078, 0.70551]


# 유클리드 거리계산식 = sqrt( sum((p - q)**2) )

import numpy as np

# 단계1 : numpy 배열 만들기(data -> q, base -> p) 
q = np.array(data)
p = np.array(base)

# 단계2 : 차의 제곱 = (p - q)**2
diff = (p - q) ** 2 

# 단계3 : 합 = sum((diff)
diff_sum = sum(diff)


# 단계4 : 제곱근 : sqrt(diff_sum)
distance = sqrt(diff_sum)

print('두 점의 거리 =', distance) 


## 한 줄 수식
distance = sqrt(sum((p - q) ** 2 ))
print('두 점의 거리 =', distance) 

