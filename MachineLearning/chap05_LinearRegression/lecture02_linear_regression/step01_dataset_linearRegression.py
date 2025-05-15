"""
sklearn 패키지 
 - python 기계학습 관련 도구 제공 
"""

from sklearn.datasets import load_diabetes # dataset 
from sklearn.linear_model import LinearRegression # model
from sklearn.model_selection import train_test_split # 훈련셋/평가셋
from sklearn.metrics import mean_squared_error, r2_score # 평가 도구


# 1. dataset load 
diabetes = load_diabetes() # 객체 반환 : X변수, y변수, 관련자료  
X, y = load_diabetes(return_X_y = True) # X변수, y변수 반환 
x = diabetes.data
y = diabetes.target

X, y = load_diabetes(return_X_y = True)



# 2. X, y변수 특징 
X.mean() # -1.6638274468590581e-16
X.min() # -0.137767225690012
X.max() # 0.198787989657293
X.shape # (442, 10)

# y변수 
y.mean() # 152.13348416289594
y.min() # 25.0
y.max() # 346.0

# y변수 스케일링
import numpy as np

y = np.log1p(y) # 로그변환







# 3. train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, 
                                    test_size=0.3, 
                                    random_state=123) 
'''
test_size : 평가셋 우선
train_size : 훈련셋 우선
random_state : seed값 지정
'''
X_train.shape # (309, 10)
X_test.shape # (133, 10)
y_train.shape # (309,)


# 4. model 생성 : 훈련셋(train set)
lr = LinearRegression() # model object
model = lr.fit(X=X_train, y=y_train) # 훈련셋 적용 : model 학습
dir(model)
'''
coef_ : 기울기(회귀계수)
intercept_ : y 절편
predcit(X) : y예측치
score() : 평가 점수
'''


model.coef_
'''
[  10.45319644, -261.16273528,  538.85049356,  280.72085805,
       -855.24407564,  472.1969838 ,  166.53481397,  309.88981052,
        684.06085168,  102.3789942 ]
'''

model.intercept_  # 152.61082386550538


# 5. model 평가 : 평가셋(test set)
y_pred = model.predict(X=X_test)  
y_true = y_test 


# 1) 평균제곱오차(MSE) : 0수렴 정도
MSE = mean_squared_error(y_true, y_pred)
print('MSE =', MSE)
# 스케일링 전 : MSE = 2926.8196257936324
# 스케일링 후 : MSE = 0.15750036239142082
## 0에 가까울수록 성능이 좋다


# 2) 결정계수   : 1수렴 정도
score = r2_score(y_true, y_pred)
print('r2 score =', score) 
# 스케일링 전 : r2 score = 0.5078253552814805
# 스케일링 후 : r2 score = 0.5153839066428025

