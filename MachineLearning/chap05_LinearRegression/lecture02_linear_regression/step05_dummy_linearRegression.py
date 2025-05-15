"""
 범주형 변수를 X변수로 사용 - 가변수(dummy) 변환 
"""

import pandas as pd # csv file, 가변수 
from sklearn.model_selection import train_test_split # split 
from sklearn.linear_model import LinearRegression # model 


# 1. csv file load 
path = r'C:\ITWILL\5_Python_ML\data'
insurance = pd.read_csv(path + '/insurance.csv')
insurance.info()



# 2. 불필요한 칼럼 제거 : region
new_df = insurance.drop(['region'], axis= 1)
new_df.info()
'''
 0   age      1338 non-null   int64  
 1   sex      1338 non-null   object  
 2   bmi      1338 non-null   float64
 3   children  1338 non-null   int64
 4   smoker   1338 non-null   object  
 5   charges  1338 non-null   float64 -> y변수 
'''



# 3. X, y변수 선택 
X = new_df.drop('charges', axis= 1)
X.shape #  (1338, 4)

y = new_df['charges']


# 4. 명목형(범주형) 변수 -> 가변수(dummy) 변환 : k-1개 
X.info()
X_dummy = pd.get_dummies(X, columns=['sex', 'smoker'],
               drop_first=True)

X_dummy.info()


# 5. 이상치 확인  
X_dummy.describe() 


# 6. train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X_dummy, y, test_size=0.3, random_state=123)


# 7. model 생성 & 평가 
model = LinearRegression().fit(X=X_train, y=y_train)

model.score(X=X_train, y=y_train)
model.score(X=X_test, y=y_test)










