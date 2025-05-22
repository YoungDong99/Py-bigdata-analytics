"""
 범주형 변수를 X변수로 사용 - 가변수(dummy) 변환 
"""

import pandas as pd # csv file, 가변수 
from sklearn.model_selection import train_test_split # split 
#from sklearn.linear_model import LinearRegression # model 
from sklearn.tree import DecisionTreeRegressor #, DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder # 10진수 인코딩
from sklearn.metrics import mean_squared_error, r2_score # 회귀트리 평가 도구   
'''
DecisionTreeClassifier : 분류트리(y=범주형) -> 평가 : 분류정확도, 혼동행렬    
DecisionTreeRegressor : 회귀트리(y=숫자형) -> 평가 : MSE, r2
'''
# 1. csv file load 
path = r'C:\ITWILL\5_Python_ML\data'
insurance = pd.read_csv(path + '/insurance.csv')
insurance.info()
'''
 0   age       1338 non-null   int64  
 1   sex       1338 non-null   object   -> 10진수 인코딩  
 2   bmi       1338 non-null   float64
 3   children  1338 non-null   int64  
 4   smoker    1338 non-null   object  -> 10진수 인코딩
 5   region    1338 non-null   object  : 제거 
 6   charges   1338 non-null   float64 : y변수(의료비)
''' 


# 2. 불필요한 칼럼 제거 : region
new_df = insurance.drop(['region'], axis= 1)
new_df.info()
'''
 0   age      1338 non-null   int64  
 1   sex      1338 non-null   object  -> 10진수 인코딩  
 2   bmi      1338 non-null   float64
 3   children  1338 non-null   int64
 4   smoker   1338 non-null   object -> 10진수 인코딩 
 5   charges  1338 non-null   float64 -> y변수 
'''


# 3. X, y변수 선택 
X = new_df.drop('charges', axis= 1)
X.shape #  (1338, 5)

y = new_df['charges']


# 4. 명목형(범주형) 변수 -> 레이블 인코딩  
X['sex'] = LabelEncoder().fit_transform(X['sex'])
X['smoker'] = LabelEncoder().fit_transform(X['smoker'])


# 6. train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)


# 7. model 생성 & 평가 
model = DecisionTreeRegressor().fit(X=X_train, y=y_train)

model.score(X=X_train, y=y_train) # 0.9994363732623721
model.score(X=X_test, y=y_test) # 0.6469383682969729

y_pred = model.predict(X_test)

score = r2_score(y_true=y_test, y_pred=y_pred)
print(score) # # 0.6469383682969729

print(model.feature_importances_)
# [0.12587999 0.00743874 0.22968752 0.02358122 0.61341253]

import matplotlib.pyplot as plt

plt.barh(y = X.columns, width=model.feature_importances_)
plt.show()



