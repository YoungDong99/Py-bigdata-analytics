"""
  연속형 : 셀수없는 숫자형(나이, 급여, 구매금액)
  연속형 변수 시각화 : 산점도, 히스토그램, box-plot  
"""

import random # 난수 생성 
import statistics as st # 별칭 : 통계 함수 
import matplotlib.pyplot as plt # 별칭 : data 시각화 

dir(st)
'''
mean() : 표본 평균
median() : 중위수
quantiles() : 사분위수
pstdev() : 모집단 표준편차 (모수)
pvariance() : 모집단 분산 (모수)
stdev() : 표본의 표준편차 (통계량)
variance() : 표본 분산 (통계량)
sqrt() : 제곱근
'''

# 차트에서 한글, 음수 부호 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


# 그래프 자료 생성 
data1 = range(-3, 7) # -3 ~ 6
data2 = [random.random() for i in range(10)] 

# 1. 산점도 그래프 : 단일 색상  
plt.scatter(x=data1, y=data2, c='r', marker='o')
plt.title('scatter plot')
plt.show()


# 군집별 산점도 : 군집별 색상 적용 
cdata = [random.randint(1, 4) for i in range(10)]  # 난수 정수 
print(cdata)

plt.scatter(x=data1, y=data2, c=cdata, marker='o')  # marker 생략해도 기본 circle 적용
plt.title('scatter plot')
#plt.show()


## 각 포인터에 레이블 표시 
for idx, value in enumerate(cdata) : 
    plt.annotate(value, xy=(data1[idx]-0.09, data2[idx]+0.02))     
plt.show()


# 2. 히스토그램
data3 = [random.gauss(mu=0, sigma=1) for i in range(1000)] 
print(data3) # 표준정규분포 

# 난수 통계 : 표본 
st.mean(data3)  # 표본 평균
st.stdev(data3) # 표본 표준편차


# 1) 표준정규분포 시각화 
plt.hist(data3, label='hist1') # 기본형 
plt.hist(data3, bins=20, histtype='stepfilled', label='hist2') 
plt.legend(loc = 'best') # 범례
plt.show()
'''
loc 속성
best 
lower left/right
upper left/right
center 
'''

# 2) 일반정규분포와 균등분포 시각화 

# 일반정규분포 : 평균키=170, 표준편차=5   
data4 = [random.gauss(mu=170, sigma=5) for i in range(1000)] 

# 균등분포 : 165 ~ 175   
data5 = [random.uniform(a=165, b=175) for i in range(1000)]  

plt.hist(data4, label='gauss') 
plt.hist(data5, label='uniform')  
plt.legend(loc='best')
plt.show()




# 3. 박스 플롯(box plot)  : 기초통계 & 이상치(outlier) 제공 
data4 = [random.randint(a=45, b=85) for i in range(100)]  
max(data4)
min(data4)
st.mean(data4)

plt.boxplot(data4)
plt.show()

# 박스 플롯 사분위수 : 제1사분위수(25%), 제2사분위(50%:중위수), 제3사분위수(75%)
st.quantiles(data4) 

# 이상치(outlier) 추계 : 상한값, 하한값
data4.extend([120.5, 18.5])

plt.boxplot(data4)
plt.show()






