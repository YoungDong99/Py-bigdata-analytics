"""
로지스틱회귀모델을 이해를 위한 오즈(odds)와 로짓(logit) 그리고 시그모이드(sigmoid)   
 - 선행회귀모델을 이용하여 이항범주(Yes or No)를 예측하기 위한 로지스틱회귀모델의 도구 
 
 - 오즈(odds) : 실패(y=0)확률에 대한 성공((y=1)확률의 비  = p / 1-p
 - 로짓(logit) : 오즈를 로그 변환한 값 = log(오즈) 
 - 시그모이드(sigmoid) : 로짓값을 0 ~ 1 사이 확률로 변환하는 함수      
"""

import numpy as np


### 1 . 성공확률(p)와 오즈(odds)      

p = 0.2 # 성공확률(y=1) : 50% 미만   
odds1 = p / (1-p) # 0.25  


p = 0.5 # 성공확률(y=1) : 50% 
odds2 = p / (1-p) # 1.0 

p = 0.9 # 성공확률(y=1) : 50% 이상  
odds3 = p / (1-p)  # 9.0


p=0 # 성공확률 : 0%
p / (1-p) # 0    

p=1 # 성공확률 : 90%
p / (1-p) # Error(계산불가) : 무한대(Inf)    


# [해설] 성공확률(p)=50% 이면 오즈(odds)=1, 50% 미만 이면 0쪽으로, 50% 이상 이면 +Inf쪽으로 이동 



### 2. 오즈(odds)와 로짓(logit)
# 형식) 로짓 = log(odds) 
 
logit1 = np.log(odds1) # odds=0.25 -> -1.386 : X가 감소하는 방향으로 y에 영향
# 예) X = 나이, y=질병여부(1 or 0) : 나이가 어릴수록 질병(1)일 확률 증가 
 
logit2 = np.log(odds2) # odds=1.0 -> 0.0 : X는 y 영향 없음 

logit3 = np.log(odds3) # odds=9.0 -> 2.19 : X가 증가하는 방향으로 y에 영향
# 예) X = 나이, y=질병여부(1 or 0) : 나이가 많을수록 질병(1)일 확률 증가 

# [해설] 오즈(odds)=1 일때 로짓(logit)=0 기준으로 -Inf와 +Inf 뱡향으로 완만한 S자 곡선    



# sigmoid 함수 : S자 모양의 비선형 함수  
def sigmoid(x):
    return 1 / (1 + np.exp(-x))



### 3. 로짓(logit)과 시그모이드(sigmoid)
sig1 = sigmoid(logit1) # logit=-1.386 ->  0.2

sig2 = sigmoid(logit2) # logit=0.0 ->  0.5

sig3 = sigmoid(logit3) # logit=2.19 ->  0.89


# [해설] 로짓(logit)=0 일때 시그모이드(sigmoid)=0.5 기준으로 0~1 사이에서 S자 곡선 



### 4. cut off와 y예측치 
y_pred1 = 1 if sig1 > 0.5 else 0  # 0(y=0) 

y_pred2 = 1 if sig2 > 0.5 else 0  # 0(y=0) 

y_pred3 = 1 if sig3 > 0.5 else 0  # 1(y=1) 
# [해설] cut off = 0.5 기준으로 시그모이드 값이 0.5 이상이면 1 미만이면 0  


