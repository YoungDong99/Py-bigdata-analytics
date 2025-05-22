'''
 문2) iris dataset을 이용하여 다음과 같은 단계로 XGBoost model을 생성하시오.
'''

import pandas as pd # file read
from xgboost import XGBClassifier # model 생성 
from xgboost import plot_importance # 중요변수 시각화  
import matplotlib.pyplot as plt # 중요변수 시각화 
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import confusion_matrix, classification_report # model 평가 


# 단계1 : data set load 
iris = pd.read_csv("C:/ITWILL/5_Python_ML/data/iris.csv")

# 변수명 추출 
cols=list(iris.columns)
col_x=cols[:4] # x변수명 
col_y=cols[-1] # y변수명 


# 단계2 : 훈련/검정 데이터셋 생성
train_set, test_set = train_test_split(iris, test_size=0.25, random_state=123)

# X, y변수 분할 
X_train = train_set[col_x]
y_train = train_set[col_y]
y_train.unique() # ['versicolor', 'setosa', 'virginica']

X_test = test_set[col_x]
y_test = test_set[col_y]
y_test.unique() # ['versicolor', 'setosa', 'virginica']

# y변수 인코딩 
from sklearn.preprocessing import LabelEncoder # 10진수 인코딩 

y_train = LabelEncoder().fit_transform(y_train) # 0 ~ 2
y_test = LabelEncoder().fit_transform(y_test) # 0 ~ 2

# 단계3 : model 생성 : train data 이용
model = XGBClassifier(n_estimators=100, # tree 개수 
                      objective='multi:softprob',# 활성함수  
                      eval_metric='mlogloss',
                      random_state = 123) # 평가방법


# model 학습  
eval_set = [(X_test, y_test)] # 평가셋
 
# tree 1개 생성 : 훈련셋, 평가셋 
model.fit(X_train, y_train, # 훈련셋 
          eval_set = eval_set, # 평가세 
          verbose=True) # tree생성 출력 
'''
[0]	validation_0-mlogloss:0.74867     : tree1 평가 
 :
[99]	validation_0-mlogloss:0.14622 : tree100 평가 
'''
     
# 단계4 :예측치 생성 : test data 이용  
y_pred = model.predict(X_test) 

# 단계5 : 중요변수 확인 & 시각화  
print(model.feature_importances_)
# [0.00640904 0.02363814 0.4814888  0.488464  ]

plot_importance(model) 
plt.show() # 3번, 4번 


# 단계6 : model 평가 : confusion matrix, accuracy, classification_report
print(confusion_matrix(y_test, y_pred))
'''
[[13  0  0]
 [ 0 13  3]
 [ 0  0  9]]
'''

print(classification_report(y_test, y_pred))
'''
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        13
           1       1.00      0.81      0.90        16
           2       0.75      1.00      0.86         9

    accuracy                           0.92        38
   macro avg       0.92      0.94      0.92        38
weighted avg       0.94      0.92      0.92        38
'''


