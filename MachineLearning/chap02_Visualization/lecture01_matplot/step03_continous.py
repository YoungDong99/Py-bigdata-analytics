"""
 연속형 변수 시각화 : 산점도, 히스토그램, box-plot  
 - 연속형 변수 : 셀수 없는 숫자형 변수
   예) 급여, 나이, 몸무게 등   
"""

import random # 난수 생성 
import statistics as st # 수학/통계 함수 
import matplotlib.pyplot as plt # data 시각화 

# 차트에서 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'
# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False


# 그래프 자료 생성 
data1 = range(-3, 7) # -3 ~ 6
data2 = [random.random() for i in range(10)] # 0~1사이 난수 실수 
data2

# 1. 산점도 그래프 : 2개 변수 이용, 단일 색상  
plt.scatter(x=data1, y=data2, c='r', marker='o')
plt.title('scatter plot')
plt.show()


# 군집별 산점도 : 군집별 색상 적용 
cdata = [random.randint(a=1, b=4) for i in range(10)]  # 난수 정수(1~4) 
cdata # [2, 1, 3, 4, 1, 4, 3, 2, 2, 4]

plt.scatter(x=data1, y=data2, c=cdata, marker='o')
plt.title('scatter plot')
plt.show()


# 군집별 label 추가 
plt.scatter(x=data1, y=data2, c=cdata, marker='o') # 산점도 

# 각 포인트에 label 적용 : plt.annotate(text=label, xy=좌표)
for idx, val in enumerate(cdata) : # 색인, 내용
    plt.annotate(text=val, xy=(data1[idx], data2[idx]))
plt.title('scatter plot') # 제목 
plt.show()



# 2. 히스토그램 그래프 : 1개 변수, 대칭성 확인     
data3 = [random.gauss(mu=0, sigma=1) for i in range(1000)] 
print(data3) # 표준정규분포(-3 ~ +3) 

# 난수 통계
min(data3) 
max(data3) 

# 평균과 표준편차 
st.mean(data3) 
st.stdev(data3) 


# 정규분포 시각화 
'''
히스토그램 : x축(계급), y축(빈도수)
'''
plt.hist(data3, label='hist1') # bins=10, histtype='bar'  
plt.hist(data3, bins=20, histtype='stepfilled', label='hist2') # 계급,계단형 적용  
plt.legend(loc = 'best') # 범례
plt.show()
'''
loc 속성
best 
lower left/right
upper left/right
center 
'''


# 3. 박스 플롯(box plot)  : 기초통계 & 이상치(outlier) 시각화
data4 = [random.randint(a=45, b=85) for i in range(100)]  # 45~85 난수 정수 
data4

plt.boxplot(data4)
plt.show()

# 기초통계 : 최솟값/최댓값, 사분위수(1,2,3)
min(data4) # 45
max(data4) # 85

# 중위수 
st.median(data4) # 64.0

# 사분위수 : q1, q2, q3
st.quantiles(data4) # [58.0, 65.0, 74.75]

# 이상치 처리 : iqr 방식  
q1 = 58.0
q3 = 74.75
iqr = q3 - q1

outlier_step = 1.5 * iqr

# 정상범위  
minval = q1 - outlier_step # 하한값  
maxval = q3 + outlier_step # 상한값 
print(minval, maxval) # 29.375 ~ 100.375


# 4. 레이블 인코딩 : 10진수 인코딩

import pandas as pd 

path = r'C:\ITWILL\5_Python_ML\data'

insurance = pd.read_csv(path + '/insurance.csv')
insurance.info()
'''
 0   age       1338 non-null   int64  : 나이 
 1   sex       1338 non-null   object 
 2   bmi       1338 non-null   float64
 3   children  1338 non-null   int64  
 4   smoker    1338 non-null   object : 10진수 인코딩 대상 
 5   region    1338 non-null   object 
 6   charges   1338 non-null   float64 : 의료비 
'''


# 1) 이상치 발견과 처리 
insurance.describe() # 요약통계량 

# 2) 이상치 시각화 
plt.boxplot(insurance.age)
plt.show()


# 3) 이상치 처리 : 100세 이하 -> subset 
new_df = insurance[insurance.age <= 100]

plt.boxplot(new_df.age)
plt.show()



# 4) 레이블 인코딩  
from sklearn.preprocessing import LabelEncoder # 인코딩 class 

## 흡연유무  범주 확인  
new_df.smoker.unique() # ['yes', 'no']

# 인코딩 
smoker_encoding = LabelEncoder().fit_transform(new_df.smoker)

# 인코딩 칼럼 추가 
new_df['smoker2'] = smoker_encoding


# age vs charges : 흡연유무 분류 
plt.scatter(x=new_df.age, y=new_df.charges, 
            c=new_df.smoker2, marker='o') # 색상 = 인코딩 칼럼 
plt.show() 



 




