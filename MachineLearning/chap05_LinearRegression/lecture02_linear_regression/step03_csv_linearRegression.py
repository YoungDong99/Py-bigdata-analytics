"""
csv file 자료 + 회귀모델  
"""

import pandas as pd # csv file read
from sklearn.linear_model import LinearRegression # model 
from sklearn.metrics import mean_squared_error, r2_score # 평가도구 
from sklearn.model_selection import train_test_split # split


# 1. dataset load
path = r'C:\ITWILL\5_Python_ML\data' # file path 

iris = pd.read_csv(path + '/iris.csv')
print(iris.info())

# 2. 변수 선택 
cols = list(iris.columns)
cols # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

y_col = cols.pop(2) # 3칼럼 추출 & 제외 
y_col 

x_cols = cols[:-1]
x_cols 

X = iris[x_cols] 
y = iris[y_col] 


# 3. train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)


X_train.shape # (105, 3)
X_test.shape # (45, 3)


# 4. model 생성 : train set 
lr = LinearRegression()
model = lr.fit(X_train, y_train)


# 5. model 평가 : test set 
y_pred = model.predict(X = X_test)


mse = mean_squared_error(y_true = y_test, y_pred = y_pred)
print(mse) 

score = r2_score(y_true = y_test, y_pred = y_pred)
print(score) 





