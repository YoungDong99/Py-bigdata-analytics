"""
 시계열자료 시각화 
  - marker, color, line style, label 이용 
"""

import random # 수치 data 생성 
import matplotlib.pyplot as plt # data 시각화 
plt.style.use('ggplot') # 차트내 격차 제공 


# 1. data 생성 : 정규분포
data1 = [random.gauss(mu=0.5, sigma=0.3) for i in range(100)] 
data2 = [random.gauss(mu=0.7, sigma=0.2) for i in range(100)] 
data3 = [random.gauss(mu=0.1, sigma=0.9) for i in range(100)]   


# 2. Fugure 객체 
fig = plt.figure(figsize = (12, 5)) 
chart = fig.add_subplot() # 1개 격자 


# 3. plot : 시계열 시각화 
chart.plot(data1, marker='o', color='blue', linestyle='-', label='data1')
chart.plot(data2, marker='+', color='red', linestyle='--', label='data2')
chart.plot(data3, marker='*', color='green', linestyle='-.', label='data3')
plt.title('Line plots : marker, color, linestyle')
plt.xlabel('index')
plt.ylabel('random number')
plt.legend(loc='best') # 범례 위치 : best 위치 
plt.show()


