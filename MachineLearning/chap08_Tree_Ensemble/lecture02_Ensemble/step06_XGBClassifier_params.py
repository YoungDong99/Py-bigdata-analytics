"""
1. XGBoost Hyper parameters 
2. model 학습 조기 종료(early_stopping) 
3. Best Hyper parameters
"""

from xgboost import XGBClassifier # model 
from sklearn.datasets import load_breast_cancer # 이항분류 dataset 
from sklearn.model_selection import train_test_split # dataset split 
from sklearn.metrics import accuracy_score, classification_report # 평가


### 1. XGBoost Hyper parameters 

# 1) dataset load 
cancer = load_breast_cancer()

x_names = cancer.feature_names
print(x_names, len(x_names)) # 30
y_labels = cancer.target_names
print(y_labels) # ['malignant' 'benign'] : 이항

X, y = load_breast_cancer(return_X_y=True)


# 2) train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3)


# 3) default model 생성 
model = XGBClassifier(n_estimators=100).fit(X_train, y_train) # default 

print(model) # 주요 default parameters 
'''
1.colsample_bytree=1 : 트리 모델 생성 시 훈련셋 샘플링 비율(보통 : 0.6 ~ 1)
2.learning_rate=0.3 : 학습율(보통 : 0.01~0.1) = 0의 수렴속도 
3.max_depth=6 : 트리의 깊이(클 수록 성능이 좋아짐, 과적합 영향)
4.min_child_weight=1 : 자식 노드 분할을 결정하는 가중치(Weight)의 합
  - 값을 작게하면 더 많은 자식 노드 분할(과적합 영향)
5. n_estimators=100 결정 트리 개수(default=100), 많을 수록 고성능
6. objective='binary:logistic', 'multi:softprob'
과적합 조절 : max_depth 작게, min_child_weight 크게 
'''               

# 4) model 평가 
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(acc) # 0.9590643274853801


### 2. 학습 조기 종료 model 생성 
xgb = XGBClassifier(colsample_bytree=1,
                    learning_rate=0.3,
                    max_depth=6,
                    min_child_weight=1,
                    objective='binary:logistic', # 활성함수 
                    eval_metric='logloss',  # 평가방법 
                    early_stopping_rounds=80, # 조기종료 
                    n_estimators=500) # 500개 트리 

# early_stopping_rounds=80 : 80개 트리 생성 후 손실(loss)에 변화가 없는 시점에서 조기종료 

eval_set = [(X_test, y_test)] # model 평가 dataset 

# 1) 학습조기종료 model 생성 
es_model = xgb.fit(X=X_train, y=y_train, 
                eval_set=eval_set,
                verbose=True)
'''
[118]	validation_0-logloss:0.15385
'''

# 2) model 평가 
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(acc) # 0.9590643274853801

report = classification_report(y_test, y_pred)
print(report)


### 3. Best Hyper parameters
from sklearn.model_selection import GridSearchCV # class 

# default parameters 
xgb = XGBClassifier() 

params = {'colsample_bytree': [0.5, 0.7, 1],
          'learning_rate' : [0.01, 0.3, 0.5],
          'max_depth' : [5, 6, 7],
          'min_child_weight' : [1, 3, 5],
          'n_estimators' : [100, 200, 300]} # dict

3 * 3 * 3 * 3 * 3 # 243개 model 생성 

gs = GridSearchCV(estimator = xgb, 
             param_grid = params, cv=5)

model = gs.fit(X=X_train, y=y_train,
       eval_set = eval_set, verbose=True)


print('best score =', model.best_score_)
# best score = 0.969873417721519

print('best parameters :', model.best_params_)
'''
best parameters : {'colsample_bytree': 0.7,
                   'learning_rate': 0.5, 
                   'max_depth': 6, 
                   'min_child_weight': 1, 
                   'n_estimators': 100}
'''


