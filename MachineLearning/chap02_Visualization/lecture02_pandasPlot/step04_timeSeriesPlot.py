'''
시계열 데이터 시각화 
'''

import pandas as pd
import matplotlib.pyplot as plt


# 1. 날짜형식 수정(다국어)
path = r'C:/ITWILL/5_Python_ML/data'
cospi = pd.read_csv(path + "/cospi.csv")
print(cospi.info())

# object -> Date형 변환 
cospi['Date'] = pd.to_datetime(cospi['Date'])
print(cospi.info())
cospi


# 2. 시계열 데이터/시각화

# 1개 칼럼 추세그래프 
cospi['High'].plot(title = "Trend line of High column")
plt.show()

# 2개 칼럼(중첩list) 추세그래프
cospi[['High', 'Low']].plot(color = ['r', 'b'],
        title = "Trend line of High and Low column")
plt.show() 


# Date 칼럼으로 index 수정  
new_cospi = cospi.set_index('Date')
print(new_cospi.info())
print(new_cospi.head())


# x축 날짜로 변경
new_cospi[['High', 'Low']].plot(color = ['r', 'b'],
        title = "Trend line of High and Low column")
plt.show() 


# 날짜형 색인 
print(new_cospi.loc['2016']) # 년도 선택 
print(new_cospi.loc['2016-02']) # 월 선택 

# index 오름차순 정렬(범위 선택 선작업)
new_cospi = new_cospi.sort_index()
new_cospi.index

print(new_cospi.loc['2016-01':'2016-02']) # 범위 선택 


# 2016년도 주가 추세선 시각화 
new_cospi_HL = new_cospi[['Open', 'Close']]

new_cospi_HL.loc['2016'].plot(title = "Trend line of 2016 year")
plt.show()

new_cospi_HL.loc['2016-02'].plot(title = "Trend line of 2016 year")
plt.show()


# 3. 이동평균(평활) : 지정한 날짜 단위 평균계산 -> 추세그래프 스무딩  

# 5일 단위 평균계산 : 평균계산 후 5일 시작점 이동 
roll_mean5 = pd.Series.rolling(new_cospi.High,
                               window=5, center=False).mean()
roll_mean5

# 10일 단위 평균계산 : 평균계산 후 10일 시작점 이동
roll_mean10 = pd.Series.rolling(new_cospi.High,
                               window=10, center=False).mean()
roll_mean10

# 이동평균 시각화 : subplot 이용 - 격자 1개  
fig = plt.figure(figsize=(12,4))
chart = fig.add_subplot()

chart.plot(new_cospi['High'], color = 'blue', label = 'High column')
chart.plot(roll_mean5, color='red',label='5 day rolling mean')
chart.plot(roll_mean10, color='green',label='10 day rolling mean')
plt.legend(loc='best')
plt.show()



