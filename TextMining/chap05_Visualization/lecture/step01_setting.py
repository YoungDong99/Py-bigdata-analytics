"""
 matplotlib 환경설정 
  - 한글과 음수 부호 시각화 방법 
"""
import random  
import matplotlib.pyplot as plt 

dir(random)
'''
gauss(mu = 0, sigma=1) : 정규분포 난수
randint(a, b) : a ~ b 난수 정수
random() : 0 ~ 1 난수 실수
uniform(a, b) : a ~ b 난수 실수
seed() : 시드값
'''


# 1. 차트 dataset 생성 
data = [random.gauss() for i in range(100)]  # 난수 100개 

print(data) # -3 ~ +3


# 2. 정규분포 시각화 
plt.plot(data)  
plt.title('standard normal distribution random number') 
plt.xlabel('index')  # x축
plt.ylabel('random number')  # y축
plt.show() 

import inspect
print(inspect.getsource(random.gauss))


# 차트에서 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'


# 음수 부호 지원  
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# 3. 정규분포 시각화 : 한글 적용  
plt.plot(data)  # 시각화(선 그래프)
plt.title('표준 정규분포 난수') 
plt.xlabel('색인')
plt.ylabel('난수')
plt.show() 

