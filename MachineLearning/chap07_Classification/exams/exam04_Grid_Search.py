"""
문4) 다음 조건에 맞게 비선형 SVM 모델과 선형 SVM 모델을 생성하시오. 
  <조건1> 비선형 SVM 모델과 선형 SVM 모델 생성
  <조건2> GridSearch model을 이용하여 best score와 best parameters 구하기  
"""

from sklearn.svm import SVC # svm model 
from sklearn.datasets import load_iris # dataset 
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import accuracy_score # 평가 

# 1. dataset load 
X, y = load_iris(return_X_y= True)
X.shape # (150, 4)

# 2. train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)


# 3. 비선형 SVM 모델 : kernel='rbf'
rbf_model = SVC(kernel='rbf').fit(X=X_train, y=y_train)

y_pred = rbf_model.predict(X_test)
print('비선형 SVM 모델 :', accuracy_score(y_test, y_pred)) 
# 비선형 SVM 모델 : 0.9111111111111111

# 4. 선형 SVM 모델 : kernel='linear' 
linear_model = SVC(kernel='linear').fit(X=X_train, y=y_train)

y_pred = linear_model.predict(X_test)
print('선형 SVM 모델 :', accuracy_score(y_test, y_pred))
# 선형 SVM 모델 : 0.9555555555555556


# 5. Grid Search : 선형과 비선형 SVM 모델 중 분류정확도가 낮은 model 대상으로 5겹 교차검정 수행 
'''
    gamma : {'scale', 'auto'} or float, default='scale'
        Kernel coefficient for 'rbf', 'poly' and 'sigmoid'.

        - if ``gamma='scale'`` (default) is passed then it uses
          1 / (n_features * X.var()) as value of gamma,
        - if 'auto', uses 1 / n_features
        - if float, must be non-negative.
'''    
n_features = 4
scale = 1 / (n_features * X.var()) # 0.06416744863614975
auto = 1 / n_features # 0.25
(scale + auto) / 2 # 평균 = 0.15708372431807488

parmas = {'kernel' : ['rbf', 'linear'],
          'C' : [0.01, 0.1, 1.0, 10, 100],
          'gamma': ['scale', 'auto', 0.157]} # dict 정의 
'''
model 개수 = 30(2 * 5 * 3) 
'''


from sklearn.model_selection import GridSearchCV 

grid_model = GridSearchCV(rbf_model, param_grid=parmas, 
                   scoring='accuracy',cv=5, 
                   n_jobs=-1, verbose=True).fit(X, y) # 전체 데이터셋 반영 
'''
verbose=True : 콘솔 출력 
Fitting 5 folds for each of 30 candidates, totalling 150 fits
''' 

dir(grid_model)
'''
best_score_ : 가장 높은 분류정확도 
best_params_ : 최적의 파라미터 
'''

print('best score :',grid_model.best_score_)
# best score : 0.9800000000000001
print('best params :', grid_model.best_params_)
'''
best params : {'C': 1.0, 'gamma': 'scale', 'kernel': 'linear'}
'''


