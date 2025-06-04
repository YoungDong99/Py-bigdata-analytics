"""
<준비물> 
prophet 패키지 설치 
pip install prophet

 - 단순(simple)시계열모델 : 기존 목적변수(Yt)-> 미래 목적변수(Yt+1) 
"""

from prophet import Prophet # 시계열분석 알고리즘 

import pandas as pd # dataset
from sklearn.metrics import r2_score # 평가 

### 1. dataset load 
path = r'C:\ITWILL\5_Python_ML\data\Bike-Sharing-Dataset'
data = pd.read_csv(path + '/day.csv')
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 731 entries, 0 to 730
Data columns (total 16 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   instant     731 non-null    int64  : 일련번호
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
 13  casual      731 non-null    int64   : 비가입자이용수 
 14  registered  731 non-null    int64   : 가입자이용수 
 15  cnt         731 non-null    int64   : 전체사용자이용수 
'''
data.head()


# 변수 선택 : 날짜, 가입자이용수
df = data[['dteday','registered']] # 날짜(x축), 가입자이용수(y축)
df.shape #  (731, 2)

# 날짜/시간 자료형 변환 
df['dteday'] = pd.to_datetime(df['dteday'])

df.info() 

# 칼럼명 수정 
df.columns = ['ds', 'y']


### 2. 시계열자료 추세 & 계절성 확인 
import matplotlib.pyplot as plt 

fig = plt.figure(figsize = (12, 5)) 
chart = fig.add_subplot()  

chart.plot(df.ds, df.y, marker='.', label='time series data')
plt.xlabel('year-month')
plt.ylabel('user number')
plt.legend(loc='best')
plt.show()
# 연 단위, 월 단위 계절성 확인 

### 3. train vs test split  
train = df[(df.ds >= '2011-01-01') & (df.ds <= '2012-10-31')] # 22개월 
train.shape # (670, 2)

test = df[df.ds >= '2012-11-01'] # 2개월 
test.shape # (61, 2)
'''
과거자료 : 670일
미래자료 : 61일
'''


### 4. 시계열모델 생성 
model = Prophet(yearly_seasonality=True, 
                weekly_seasonality=True,
                daily_seasonality=False,
                seasonality_mode='multiplicative') # 빈 시계열모형 

model.fit(train)
''' ppt.11 참고 
yearly_seasonality : 연단위 주기(여름,가을 vs 봄,겨울)
weekly_seasonality : 주단위 주기(주말 vs 평일)
daily_seasonality : 일단위 주기(시간 단위)
seasonality_mode : 가법(additive) 또는 승법(multiplicative) 모델 선택 
'''


### 5. 예측용 데이터 생성 & 예측 
future_date = model.make_future_dataframe(periods=61, freq='D') # 예측 미래시점 : ppt.11
# periods=61, freq='D' : 61일 

future_pred = model.predict(future_date) # 모델 예측 : 61일(670+61=731) 


### 6. 시계열모델 평가 
# 1) 요소분해 : 추세, 계절성 
model.plot_components(future_pred)
plt.show()


# 2) 시계열모델 예측 결과  
fig, ax = plt.subplots(figsize = (12, 5))

model.plot(fcst=future_pred, ax=ax) # ax 적용 
ax.set_title('total user number')
ax.set_xlabel('Date')
ax.set_ylabel('user number')
plt.show()


future_pred.shape # (731, 19)

# 3) 평가 : 예측치 vs 관측치  
y_pred = future_pred.iloc[-61:, -1]
y_test = test.y

score = r2_score(y_test, y_pred) # 0.37451445994051946


# 4) 시계열자료 vs 모델 예측 
plt.plot(test.ds, y_test, c='b', label='real data')
plt.plot(test.ds, y_pred, c='r', label = 'predicted data')
plt.legend()
plt.xticks(rotation=90)
plt.show()



 