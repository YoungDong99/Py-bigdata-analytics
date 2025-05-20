"""
 - 선형 SVM, 비선형 SVM
"""

from sklearn.svm import SVC # svm model 
from sklearn.datasets import load_breast_cancer # dataset 
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import accuracy_score, classification_report # 평가 

## 1. dataset load 
X, y = load_breast_cancer(return_X_y= True)
X.shape # (569, 30)

X.var() # 52119.70516752481

## 2. train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)


## 3. 비선형 SVM 모델 
svc = SVC(C=1.0, kernel='rbf', gamma='scale')
'''
기본 parameter
 C=1.0 : cost(오분류) 조절 : 결정경계 위치 조정
 kernel='rbf' : 커널트릭 함수 
  -> kernel : {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}
 gamma='scale' : 결정경계 모양 조절 조정 
  -> {'scale', 'auto'} or float
  -> gamma='scale' : 1 / (n_features * X.var())
  -> gamma='auto' : 1 / n_features
'''
scale = 1 / (30 * 52119.70516752481) # 0.0000003695
auto = 1  / 30 # 0.0333
            
model = svc.fit(X=X_train, y=y_train)


# model 평가 
y_pred = model.predict(X = X_test)

acc = accuracy_score(y_test, y_pred)
print('accuracy =',acc) # accuracy = 0.9005847953216374


## 4. 선형 SVM  
svc2 = SVC(C=1.0, kernel='linear') # gamma 사용 안함

model2 = svc2.fit(X=X_train, y=y_train)

# model 평가 
y_pred = model2.predict(X = X_test)

acc = accuracy_score(y_test, y_pred)
print('accuracy =',acc) # accuracy = 0.9707602339181286

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       0.98      0.94      0.96        68
           1       0.96      0.99      0.98       103

    accuracy                           0.97       171
   macro avg       0.97      0.97      0.97       171
weighted avg       0.97      0.97      0.97       171
'''



