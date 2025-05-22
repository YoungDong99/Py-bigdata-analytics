'''
 문2) 다음 데이터 셋을 이용하여 단계별로 Decision Tree 모델을 생성하시오.
'''

import pandas as pd # csv file read
from sklearn.model_selection import train_test_split # dataset split 
from sklearn.tree import DecisionTreeClassifier # model
from sklearn.metrics import confusion_matrix, classification_report # model evaluation


path = r'C:\ITWILL\5_Python_ML\data'
data = pd.read_csv(path +'/dataset.csv') 
data.info()
'''
RangeIndex: 217 entries, 0 to 216
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   resident  217 non-null    int64    : x변수(명목척도) 
 1   gender    217 non-null    int64    : x변수(명목척도) 
 2   job       205 non-null    float64  : x변수(명목척도) 
 3   age       217 non-null    int64    : x변수(비율척도) 
 4   position  208 non-null    float64  : y변수(명목척도) 
 5   price     217 non-null    float64  : x변수(비율척도) 
 6   survey    217 non-null    int64    : x변수(등간척도)  
'''
 

# 단계1 : 결측치를 포함한 모든 행 제거 후 new_data 생성 
data.isnull().sum() # 각 칼럼의 결측치 총개수 
data.shape # (217, 7)

new_data = data.dropna()
new_data.shape # (198, 7)


from sklearn.preprocessing import LabelEncoder # 인코딩 도구

# 단계2 : 변수 인코딩 대상(명목척도) : resident, gender, job, position  
new_data.resident = LabelEncoder().fit_transform(new_data.resident)
new_data.gender = LabelEncoder().fit_transform(new_data.gender)
new_data.job = LabelEncoder().fit_transform(new_data.job)
new_data.position = LabelEncoder().fit_transform(new_data.position)
new_data.head()

# 단계3 : new_data에서 X, y변수 선택 
X = new_data.drop('position', axis=1) # 'resident','gender','job','age','price','survey'
y = new_data.position # 'position'


# 단계4 : 훈련 데이터 75, 테스트 데이터 25 나누기 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state = 123)


# 단계5 : 기본모델 만들기 
model = DecisionTreeClassifier(random_state=123).fit(X_train, y_train)

print(model.feature_importances_) # 중요변수 : age 
# [0.02609452 0.01043615 0.02821553 0.90053866 0.02831448 0.00640066]

y_pred = model.predict(X = X_test)


# 단계6. 기본모델 평가 : 혼동행렬, classification_report  
conf_matrix = confusion_matrix(y_true=y_test, y_pred=y_pred) # 혼동 행렬
print(conf_matrix)
'''
[[16  0  0  0  3]
 [ 0  9  0  0  1]
 [ 0  0  7  0  0]
 [ 0  1  0  5  0]
 [ 0  2  0  0  6]]
'''

classification_report = classification_report(y_true=y_test, y_pred=y_pred) 
print(classification_report)
'''
              precision    recall  f1-score   support

           0       1.00      0.84      0.91        19
           1       0.75      0.90      0.82        10
           2       1.00      1.00      1.00         7
           3       1.00      0.83      0.91         6
           4       0.60      0.75      0.67         8

    accuracy                           0.86        50
   macro avg       0.87      0.87      0.86        50
weighted avg       0.89      0.86      0.87        50
'''


# 단계7 : best parameter 찾기 
from sklearn.model_selection import GridSearchCV # best parameters

parmas = {'criterion' : ['gini', 'entropy'], # 중요변수 선택 
          'max_depth' : [None, 3, 4, 5, 6],  # 트리 깊이 
          'min_samples_split': [2, 3, 4]}  # 내부노드 분할 최소 샘플 수 



# 1) 기본 model을 대상으로 5겹 교차검정으로 수행
grid_model = GridSearchCV(model, param_grid=parmas, 
                   scoring='accuracy',cv=5, n_jobs=-1).fit(X, y)

dir(grid_model)
'''
best_params_ : best 파라미터 
best_score_ : best 점수 
'''

# 2) Best score 확인 
print(grid_model.best_score_) # 0.9294871794871795

# 3) Best parameters 확인  
print(grid_model.best_params_)
# {'criterion': 'gini', 'max_depth': 4, 'min_samples_split': 2}

