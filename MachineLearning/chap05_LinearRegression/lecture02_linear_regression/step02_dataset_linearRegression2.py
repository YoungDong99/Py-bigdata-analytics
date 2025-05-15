"""
sklearn 패키지 
 - python 기계학습 관련 도구 제공 
"""

from sklearn.datasets import load_iris # dataset 
from sklearn.linear_model import LinearRegression # model
from sklearn.model_selection import train_test_split # split
from sklearn.metrics import mean_squared_error, r2_score # 평가도구 


##############################
### load_iris
##############################

# 1. dataset load 
iris = load_iris()
X, y = load_iris(return_X_y=True)
X.shape # (150, 4)


# 2. 변수 선택 
y = X[:,0] # 첫번째 변수 
X = X[:,1:] # 2~4번째 변수 
y.shape # (150,)

X.shape # (150, 3)

# 3. train/test split 
X_train,X_test, y_train,y_test = train_test_split(X, y, 
                 test_size=0.3, random_state=123)

# 4. model 생성 
model = LinearRegression().fit(X=X_train, y=y_train) 

# X변수 기울기 
model.coef_ # [ 0.63924286,  0.75744562, -0.68796484]


# 5. model 평가
y_pred = model.predict(X=X_test)
y_true = y_test

# 1) MSE  
MSE = mean_squared_error(y_true, y_pred)
print('MSE =', MSE) 


# 2) 결정계수(R-제곱)  
score = r2_score(y_true, y_pred)
print('r2 score =', score) 


# 3) 시각화 평가 
import matplotlib.pyplot as plt
plt.plot(y_pred, color='r', linestyle='--', label='pred')
plt.plot(y_true, color='b', linestyle='-', label='Y')
plt.legend(loc='best')
plt.show()

