"""
  서브플롯(subplot) 차트 시각화 
  figure : 차트 전체 틀
  subplot : 하위 격자
"""

import random # data 생성 
import matplotlib.pyplot as plt # data 시각화 


# 1. subplot 생성 
fig = plt.figure(figsize = (10, 5)) # 차트 크기 지정 
x1 = fig.add_subplot(2,2,1) # 2행2열 - 1번
x2 = fig.add_subplot(2,2,2) # 2행2열 - 2번
x3 = fig.add_subplot(2,2,3) # 2행2열 - 3번
x4 = fig.add_subplot(2,2,4) # 2행2열 - 4번

# 2.차트 데이터 생성 
data1 = [random.gauss(mu=0, sigma=1) for i in range(100)]
data2 = [random.randint(1, 100) for i in range(100)] # 1 ~ 100
cdata = [random.randint(1, 4) for i in range(100)] # 1 ~ 4


dir(fig)
'''
add_subplot()
suptitle() : 차트 제목
'''

# 3. 각 격자그래프 크리기 
x1.hist(data1) # 히스토그램 
x2.scatter(data1, data2, c=cdata) # 산점도 
x3.plot(data2) # 기본 차트 
x4.plot(data1, data2, 'g--') # 기본 차트 : 선 색과 스타일 


# fig 수준 제목
fig.suptitle('super title', fontsize = 20)


# 각 subplot 제목
x1.set_title('hist', fontsize = 15)
x2.set_title('scatter', fontsize = 15)
x3.set_title('default graph', fontsize = 15)
x4.set_title('line graph', fontsize = 15)

plt.show()

############################
# 2개 y축 갖는 그래프 
############################

fig = plt.figure()
axes = fig.add_subplot()
axes2 = axes.twinx()

x = [1,2,3,4]
y = [2,4,6,8]

y2 = [4,6,1,9]

axes.bar(x, y, color='green', label='bar') # 막대그래프 
axes2.plot(x, y2, color='red', label='plot', linestyle='--') # 선 그래프
plt.show()






