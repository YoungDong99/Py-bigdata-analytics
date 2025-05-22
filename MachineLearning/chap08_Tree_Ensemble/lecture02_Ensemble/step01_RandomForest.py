"""
RandomForest 앙상블 모델 
"""

from sklearn.ensemble import RandomForestClassifier # model
from sklearn.datasets import load_wine # dataset 

# 평가 도구 
from sklearn.metrics import confusion_matrix, classification_report

# 1. dataset load
wine = load_wine()

X, y = wine.data, wine.target
X.shape # (178, 13)
y


# 2. model 생성 
'''
주요 hyper parameter(default)
 n_estimators=100 : tree 개수 
 criterion='gini' : 중요변수 선정 기준 
 max_depth=None : 트리 깊이 
 min_samples_split=2 : 내부 노드 분할에 필요한 최소 샘플 수
'''


# 모델 학습
model = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=42)
'''
oob_score=True : ppt.19 
''' 
model.fit(X = X, y = y) # full dataset 적용 


# model 자체 평가 : OOB Score 확인
oob_score = model.oob_score_
oob_error_rate = 1 - oob_score

print(f"OOB Score: {oob_score:.4f}") # OOB Score: 0.9831
print(f"OOB Error Rate: {oob_error_rate:.4f}") # OOB Error Rate: 0.0169



# 3. 평가셋으로 model 평가 
import numpy as np

# 1) 비복원 data 추출 
idx = np.random.choice(a=len(X), size=100, replace=False)
'''
a : 원형자료 크기 
size : 표본 크기 
replace=False : 비복원 추출(중복 불가)
'''
X_test, y_test = X[idx], y[idx]
X_test.shape # (100, 13)

# 2) 예측치 & 평가 
y_pred = model.predict(X = X_test)

con_mat = confusion_matrix(y_test, y_pred)
print(con_mat)


report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        28
           1       1.00      1.00      1.00        40
           2       1.00      1.00      1.00        32

    accuracy                           1.00       100
   macro avg       1.00      1.00      1.00       100
weighted avg       1.00      1.00      1.00       100
'''


# 4. 중요변수 시각화 
print('중요도 : ', model.feature_importances_)

x_names = wine.feature_names # x변수 이름  
x_size = len(x_names) # x변수 개수  

import matplotlib.pyplot as plt 

# 가로막대 차트 
plt.barh(range(x_size), model.feature_importances_) # (y, x)
plt.yticks(range(x_size), x_names)   
plt.xlabel('feature_importances') 
plt.show()


