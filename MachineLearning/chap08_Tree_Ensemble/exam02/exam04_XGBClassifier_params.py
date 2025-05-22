"""
문4) wine dataset을 이용하여 다음과 같이 다항분류 모델을 생성하시오. 
   <조건1> tree model 200개 학습
   <조건2> tree model 학습과정에서 조기 종료 100회 지정
   <조건3> model의 분류정확도와 리포트 출력   
"""

from xgboost import XGBClassifier # model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine # 다항분류
from sklearn.metrics import classification_report


#################################
## 1. XGBoost Hyper Parameter
#################################

# 1. dataset load
X, y = load_wine(return_X_y=True)
X.shape 
y # 0 ~ 2

# 2. train/test 생성 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=34)

# 3. model 생성 : 다항분류 
xgb = XGBClassifier(objective='multi:softprob', # 활성함수 : softmax 
              eval_metric='mlogloss', # 평가방법 : multi-class  
              early_stopping_rounds=100, # 조기종료 횟수
              n_estimators=200) # 학습 tree 개수 

# 4. model 학습 조기종료 
eval_set = [(X_test, y_test)]

model = xgb.fit(X=X_train, y=y_train, # 훈련셋 
                eval_set=eval_set,  # 평가셋  
                verbose=True) # 콘솔 출력

'''
조기종료 : 126개 tree 
[125]	validation_0-mlogloss:0.08803
'''

# 5. model 평가 : classification_report
y_pred = model.predict(X_test)

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        16
           1       1.00      0.94      0.97        17
           2       0.92      1.00      0.96        12

    accuracy                           0.98        45
   macro avg       0.97      0.98      0.98        45
weighted avg       0.98      0.98      0.98        45
'''


