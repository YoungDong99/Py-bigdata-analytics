'''
- XGBoost 앙상블 모델 테스트
- Anaconda Prompt에서 패키지 설치 
  pip install xgboost
'''

from xgboost import XGBClassifier # model  
from xgboost import plot_importance # 중요변수(x) 시각화  
from sklearn.datasets import make_blobs # 클러스터 생성 dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

import xgboost

dir(xgboost)
'''
XGBClassifier : 분류트리(y=범주형변수) 
XGBRegressor : 회귀트리(y=연속형변수) 
'''


# 1. 데이터셋 로드 : blobs
X, y = make_blobs(n_samples=2000, n_features=4, centers=3, 
                   cluster_std=2.5, random_state=123)
'''
n_samples : 데이터셋 크기 
n_features : X변수 개수 
centers : y변수 class 개수 
cluster_std : 데이터 복잡도 
'''

X.shape # (2000, 4)
y # 0, 1, 2

# blobs 데이터 분포 시각화 
plt.title("three cluster dataset")
plt.scatter(X[:, 0], X[:, 1], s=100, c=y,  marker='o') # color = y범주
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()


# 2. 훈련/검정 데이터셋 생성
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3)



# 3. XGBOOST model : y class=2개(binary class)
'''
model = XGBClassifier(n_estimators=100, # tree 개수 
                      objective='binary:logistic',# 활성함수  
                      eval_metric='logloss') # 평가방법 
'''
# 3. XGBOOST model : y class=3개(multi class)
model = XGBClassifier(n_estimators=100, # tree 개수 
                      objective='multi:softprob',# 활성함수  
                      eval_metric='mlogloss') # 평가방법
'''
이항분류(binary-class classification) : objective='binary:logistic' 
eval_metric='logloss'

다항분류(multi-class classification) : objective='multi:softprob' 
eval_metric='mlogloss'
'''

# model 학습  
eval_set = [(X_test, y_test)] # 평가셋
 
# tree 1개 생성 : 훈련셋, 평가셋 
model.fit(X_train, y_train, # 훈련셋 
          eval_set = eval_set, # 평가세 
          verbose=True) # tree생성 출력 


# 4. model 평가 
y_pred = model.predict(X_test) 
acc = accuracy_score(y_test, y_pred)
print('분류정확도 =', acc) 
'''
class = 3 : 분류정확도 = 0.9233333333333333
class = 2 : 분류정확도 = 0.9983333333333333
'''

report = classification_report(y_test, y_pred)
print(report)


# 5. fscore 중요변수 시각화  
fscore = model.get_booster().get_fscore()
print("fscore:",fscore) 
# fscore: {'f1': 5.0, 'f2': 49.0, 'f3': 13.0}
# fscore: {'f0': 924.0, 'f1': 915.0, 'f2': 962.0, 'f3': 819.0}

# 중요변수 시각화
plot_importance(model) 
plt.show()



