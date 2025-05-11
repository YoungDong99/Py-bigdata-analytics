#########################################
### 4. 피처 스케일링(feature scaling) 
#########################################

"""
피처 스케일링 : 서로 다른 크기(단위)를 갖는 X변수(feature)를 대상으로 일정한 범위로 조정하는 전처리 작업 
 - 방법 : 표준화, 최소-최대 정규화, 로그변환    
 
 1. 표준화 : X변수를 대상으로 정규분포가 될 수 있도록 평균=0, 표준편차=1 통일  
   -> 회귀모델, SVM 계열은 X변수가 정규분포라고 가정하에 학습이 진행되므로 표준화 적용   
 2. 최소-최대 정규화 : 서로 다른 척도(값의 범위)를 갖는 X변수를 대상으로 최솟값=0, 최댓값=1 통일 
   -> 트리모델 계열(회귀모델 계열이 아닌 경우)에서 서로 다른 척도를 갖는 경우 적용 
 3. 로그변환 : log()함수 이용하여 로그변환   
   -> 왜곡을 갖는 분포 -> 좌우대칭의 정규분포로 변환   
"""

# 1. 함수형 스케일링 도구  
from sklearn.preprocessing import scale, minmax_scale # 표준화, 정규화 
#from sklearn.preprocessing import minmax_scale # 정규화
import numpy as np # 로그변환 + 난수 np.log(y)

# 실습 data 생성 : 난수 정수 생성  
np.random.seed(12) # 시드값 
X = np.random.randint(-10, 100, (5, 4)) # -10~100
print(X)
'''
   x1  x2  x3  x4  
[[ 65  17  -4  -8]
 [ -7  57  66  38]
 [ 12  39  42  -5]
 [  3  79  24  65]
 [ 64 -10  94  66]]
'''

# 1) 표준화 
X_zscore = scale(X) # z = x - mu / sigma
print(X_zscore) # -3 ~ +3

# 2) 정규화 
X_nor = minmax_scale(X) # 0~1 조정 
print(X_nor)

# 3) 로그변환 
X_log = np.log(X) # 밑수 e  
print(X_log)

# RuntimeWarning
np.log(0) # -inf
np.log(0+1) # np.log1p(0)
np.log(-10) # nan

# RuntimeWarning 해결방안 
np.log1p(0) # 0.0
np.log1p(np.abs(-10))

X_log = np.log1p(np.abs(X)) # 밑수 e  
print(X_log)
'''
[[4.18965474 2.89037176 1.60943791 2.19722458]
 [2.07944154 4.06044301 4.20469262 3.66356165]
 [2.56494936 3.68887945 3.76120012 1.79175947]
 [1.38629436 4.38202663 3.21887582 4.18965474]
 [4.17438727 2.39789527 4.55387689 4.20469262]]
'''


# 2. 클래스형 스케일링 도구 
from sklearn.preprocessing import StandardScaler, MinMaxScaler 

import pandas as pd
path = r'C:\ITWILL\5_Python_ML\data'
iris = pd.read_csv(path + "/iris.csv")
iris.info()

# 1) DataFrame 표준화 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X=iris.drop('Species', axis=1)) # Species 칼럼 제외 
print(X_scaled)

# 2) DataFrame 정규화 
scaler2 = MinMaxScaler()
X_scaled2 = scaler2.fit_transform(X = iris.drop('Species', axis = 1)) # Species 칼럼 제외  

X_scaled2


