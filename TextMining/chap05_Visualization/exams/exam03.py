'''
문3) 다음은 두 기업(APPLE, MS)의 주가를 시계열 자료로 활용하여 시각화하시오.

    <시각화 결과> exam03.pdf 참고             
'''

import pandas as pd # 날짜 자료 생성 
import numpy as np # 수치 자료 생성 
import matplotlib.pyplot as plt # 시각화 

np.random.seed(1234) # 시드값 적용 


# 두 기업 주식 자료 생성 : 2년치 주식 가격 
date = pd.date_range(start='2009-01-01', end='2010-12-31', freq='D') # 년도 : X축 자료  

len(date)
date


# Y축 자료 
APPLE = np.cumsum(np.random.randn(len(date))) + 100 # 애플사 주가 
MS = np.cumsum(np.random.randn(len(date))) + 120 # 마이크로소프트사 주가 


# 주식 가격 데이터 시각화
fig = plt.figure(figsize=(10, 5)) # 차트 크기 
chart = fig.add_subplot() # 1개 격자 

# 3. plot : 시계열 시각화 
chart.plot(date, APPLE, color='red', linestyle='-', label='APPLE')
chart.plot(date, MS, color='blue', linestyle='-', label='MS')
plt.title('애플과 마이크로소프트 주가변동 현환')
plt.xlabel('기간(2009년~2010년 : 월단위)')
plt.ylabel('주식가격')
plt.legend(loc='best') # 범례 위치 : best 위치 
plt.show()







