'''
자전거 대여 서비스 관련 dataset 예측분석

dataset 출처 : UCI 머신러닝 저장소 
https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip


문3) 주어진 데이터셋(data)를 대상으로 단계별로 xgboost 모델을 생성하시오.
   단계1. 불필요한 칼럼 제거 : instant, dteday, casual, cnt
   단계2. X, y변수 선택 : y변수 = registered, X변수 나머지 변수(11개) 
   단계3. train(70) vs test(30) split     
   단계4. xgboost 모델 생성  
   단계5. 중요변수 시각화 & 의미 해석 
   단계6. model 평가 : r2 score   
'''

# dataset 출처 : UCI 머신러닝 저장소 
#https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip

from xgboost import XGBRegressor # 회귀트리 모델 
from xgboost import plot_importance # 중요변수 시각화 
import matplotlib.pyplot as plt

import pandas as pd # dataset
from sklearn.model_selection import train_test_split # split 
from sklearn.metrics import r2_score # 평가 

path = r'C:\ITWILL\5_Python_ML\data\Bike-Sharing-Dataset'

data = pd.read_csv(path + '/day.csv')
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 731 entries, 0 to 730
Data columns (total 16 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   instant     731 non-null    int64  : 일련번호(제외) 
 1   dteday      731 non-null    object : 날짜 
 2   season      731 non-null    int64  : 계절 
 3   yr          731 non-null    int64  : 연도 
 4   mnth        731 non-null    int64  : 월 
 5   holiday     731 non-null    int64  : 휴일 
 6   weekday     731 non-null    int64  : 요일 
 7   workingday  731 non-null    int64  : 근무일 
 8   weathersit  731 non-null    int64  : 날씨 
 9   temp        731 non-null    float64 : 온도
 10  atemp       731 non-null    float64 : 체감온도
 11  hum         731 non-null    float64 : 습도
 12  windspeed   731 non-null    float64 : 풍속
 13  casual      731 non-null    int64   : 비가입자 이용수 
 14  registered  731 non-null    int64   : 가입자 이용수 
 15  cnt         731 non-null    int64   : 전체사용자 이용수 
'''
data.head()

data.iloc[0]

# 단계1. 불필요한 칼럼 제거 : instant, dteday, casual, cnt 
new_data = data.drop(['instant','dteday','casual','cnt'], axis = 1)
new_data.shape #  (731, 12)


# 단계2. X, y변수 선택 : y변수 = registered, X변수 나머지 변수(11개) 
X = new_data.drop(['registered'], axis = 1)
X.info()

# X변수 스케일링 확인 
X.mean(axis = 0)

y = data.registered
y # 10진수 

#  단계3. train(70) vs test(30) split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1)


# 단계4. xgboost 모델 생성 
model = XGBRegressor().fit(X=X_train, y=y_train) 


# 단계5. 중요변수 시각화 & 의미 해석   
fscore = model.get_booster().get_fscore()
print(fscore)
'''
{'season': 233.0, 'yr': 214.0, 'mnth': 338.0, 'holiday': 43.0, 'weekday': 338.0, 'workingday': 55.0, 'weathersit': 89.0, 'temp': 542.0, 'atemp': 387.0, 'hum': 679.0, 'windspeed': 553.0}
'''

# 중요변수 시각화 : x변수명 없음 
plot_importance(model, max_num_features=11) # 11개까지 나타냄 
plt.show()
# 중요변수 Top6 해설 : hum, windspeed, temp, weekday, atemp, mnth : 날씨, 주말, 월 중요 변수 

import seaborn as sn

# 습도(hum) : 평균 습도 이상인 경우 이용자수 많음 
sn.scatterplot(data=data, x='hum', y='registered')
plt.show()

# 풍속(windspeed) : 풍속이 느린경우 이용자수 많음 
sn.scatterplot(data=data, x='windspeed', y='registered')
plt.show()

# 온도(temp) 높을 수록 이용자수 많아짐 
sn.scatterplot(data=data, x='temp', y='registered')
plt.show()

# 주말(weekday) : 평일 이용자수 많음 : 6(토), 0(일)  
sn.barplot(data=data, x='weekday', y='registered')
plt.show()

# 체감온도(atemp) : 높을 수록 이용자수 많음  
sn.scatterplot(data=data, x='atemp', y='registered')
plt.show()

# 월(mnth) : 5월 ~ 10월 이용자 수 많음(겨울과 봄 이용자 감소) 
sn.barplot(data=data, x='mnth', y='registered')
plt.show()

# 단계6. model 평가 
y_pred = model.predict(X = X_test)  # 예측치 

score = r2_score(y_test, y_pred)
print('r2 score =', score) # r2 score = 0.8783299594044056


