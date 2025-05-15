"""
다항회귀모형(Polynomial regression model) 만들기  
 - X와 y변수가 비선형관계를 가지는 경우 고차항 적용한 회귀모형  
"""

import pandas as pd # csv file load 
import numpy as np # np.nan
from sklearn.linear_model import LinearRegression #선형회귀분석
from sklearn.model_selection import train_test_split # 데이터 split
import seaborn as sns # 비선형모형 예측치 시각화 



## 단계1 : 데이터 준비 : 칼럼명 없음 
df = pd.read_csv(r'C:\ITWILL\5_Python_ML\data\auto-mpg.csv',header=None)


# 1) 칼럼명 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model_year','origin','name']
df.info()


# 2) horsepower 칼럼 전처리 
df['horsepower'].replace('?', np.nan, inplace=True) # 특수문자 결측치 처리 
df.dropna(subset=['horsepower'], inplace=True) # 결측치 제거
df['horsepower'] = df['horsepower'].astype('float') # 실수형 변환


# 3) 분석에 필요한 변수 선택 : 연비, 실린더, 출력, 중량
new_df = df[['mpg', 'cylinders', 'horsepower', 'weight']]



## 단계2 : 변수 탐색 및 선택   

# 상관계수 행렬
new_df.corr()  


# 종속변수 vs 독립변수 선형성 확인
sns.pairplot(data = new_df)
 

# 변수 선택 
X=new_df[['cylinders', 'horsepower', 'weight']] # 독립변수 X
y=new_df['mpg'] # 종속변수 Y


## 단계3 : train/test split 
X_train, X_test, y_train, y_test = train_test_split(
           X, y, test_size=0.3, random_state=10)


## 단계4 : 선형다중회귀모델(다항식 적용 전) & 평가   
model = LinearRegression().fit(X_train, y_train)

score = model.score(X_test, y_test)
print('선형다중회귀모델 score :', score) 



############################################
### 다항회귀모형 : 다항식 적용 
############################################


from sklearn.preprocessing import PolynomialFeatures # x변수 다항식 변환


# 단계1 : 다항회귀모델(2차항) 
poly = PolynomialFeatures(degree=2) # 2차항 적용 객체 

X1_poly = poly.fit_transform(X[['horsepower']]) # horsepower 변수 2차항

X2_poly = poly.fit_transform(X[['weight']]) # weight 변수 2차항


# 단계2 : 다항식 변수 추가 
X_new = X.copy() # 내용 복사  

X_new['horsepower_poly'] = X1_poly[:, 2] # horsepower 변수 2차항 추가 
X_new['weight_poly'] = X2_poly[:, 2] # weight 변수 2차항 추가


# 단계3 : train/test split 
X_train, X_test, y_train, y_test = train_test_split(
           X_new, y, test_size=0.3, random_state=10)


# 단계4 : 다항회귀모형 & 평가  
model = LinearRegression().fit(X_train, y_train)

score = model.score(X_test, y_test)
print('다항회귀모델 score :', score) 




