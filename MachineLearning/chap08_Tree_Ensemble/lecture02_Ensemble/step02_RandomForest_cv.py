'''
홀드아웃검증 : 70%(훈련셋) vs 30%(검정셋)

k겹 교차검증(cross validation)
 - 전체 dataset을 k등분 
 - 검정셋과 훈련셋을 서로 교차하여 검정하는 방식 
'''

from sklearn.datasets import load_digits # 0~9 손글씨 이미지 
from sklearn.ensemble import RandomForestClassifier # RM model 
from sklearn.metrics import accuracy_score # 평가 
from sklearn.model_selection import cross_validate # 교차검정 
import numpy as np # Testset 선정

# 1. dataset load 
digits = load_digits()

X = digits.data
y = digits.target

X.shape # (1797, 64) 
y.shape # (1797,)

# 2. model 생성 : tree 100개 학습 
model = RandomForestClassifier().fit(X, y) # full dataset 이용 


# 3. Test set 선정 
idx = np.random.choice(a=len(X), size=500, replace = False)
X_test = X[idx]
y_test = y[idx]



# 4. 평가셋 이용 : model 평가(1회) 
y_pred = model.predict(X = X_test) # 예측치  
y_pred 

accuracy = accuracy_score(y_test, y_pred)
print(accuracy) # 1.0


# 5. k겹 교차검정 이용 : model 평가(5회)  
score = cross_validate(model, X_test, y_test, cv=5) # k=5
print(score)
'''
{'fit_time': array([0.12758255, 0.11774015, 0.1210134 , 0.13260102, 0.11556125]), 
 'score_time': array([0.00407791, 0.00352859, 0.0040524 , 0.00562596, 0.00368023]), 
 'test_score': array([0.95, 0.96, 0.94, 0.96, 0.95])}
'''
scores = score['test_score']

print('평가결과 =', scores.mean()) # 평가결과 = 0.952



