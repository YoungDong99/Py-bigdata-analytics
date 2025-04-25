'''
문2) 우리나라 전체 중학교 2학년 여학생의 평균 몸무게는 52kg이고 편차는 5kg로 알려졌다. 
     모집단에서 2,000명의 여학생을 무작위로 추출하여 표본을 생성하고 시각화하시오.
     <조건1> 히스토그램으로 표본 시각화 
     <조건2> 표본의 통계 구하기 : 표본평균, 표본표준편차, 표본표준오차
            표본표준오차(SE) = 표준편차(s) / √ 표본크기(n)  
            
    <시각화 결과> exam02.pdf 참고         
'''

import random # 표본 생성 
import matplotlib.pyplot as plt # 표본 시각화 
import statistics as st # 표본 통계  



# 단계1 : 표본 생성 
weight = [random.gauss(mu=52, sigma=5) for i in range(2000)] # 모집단에서 2,000명의 여학생 표본 몸무게 
print(weight)
n = len(weight)

# 단계2 : 표본 시각화
plt.hist(weight, bins=100, histtype = 'stepfilled', color = 'blue')

plt.title('중학교 2학년 여학생 몸무게 표본 자료')
plt.xlabel("몸무게 (kg)")
plt.ylabel("빈도수")
plt.show()

# 단계3 : 표본 통계 : 표본평균, 표본표준편차, 표본표준오차 


