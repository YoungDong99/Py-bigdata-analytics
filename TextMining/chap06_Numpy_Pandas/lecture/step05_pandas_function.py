"""
1. DataFrame의 요약통계량
2. 상관계수
"""

import pandas as pd # 별칭

# 실습용 DataFrame 생성
name = ['hong', 'lee', 'kim', 'park']
age = [35, 45, 55, 25]
pay = [250, 350, 450, 250]
gender = pd.Series(['M', 'M', 'F', 'F'])

frame = pd.DataFrame({'name':name,
                      'age': age, 
                      'pay': pay,
                      'gender':gender})
print(frame)
'''
   name  age  pay gender
0  hong   35  250      M
1   lee   45  350      M
2   kim   55  450      F
3  park   25  250      F
'''


# 1. DataFrame의 요약통계량 : 숫자형 컬럼 대상
desc = frame.describe() 
print(desc)
'''
             age         pay
count   4.000000    4.000000
mean   40.000000  325.000000
std    12.909944   95.742711  : 표준편차
min    25.000000  250.000000
25%    32.500000  250.000000  : 제1사분위
50%    40.000000  300.000000  : 제2사분위(중위수)
75%    47.500000  375.000000  : 제3사분위
max    55.000000  450.000000
'''


# 전체 사원의 나이와 급여 평균 
frame[['age','pay']].mean(axis = 0) # 행축 

# 산포도 : 분산, 표준편차 
frame[['age','pay']].var() # axis = 0
frame[['age','pay']].std() # axis = 0


# 2. 빈도 분석 : 문자형 컬럼 대상
# 빈도수 : 집단변수 
frame['gender'].value_counts()
'''
gender
M    2
F    2
'''

# 유일값 
frame['gender'].unique()
# array(['M', 'F'], dtype=object)


# 3. 상관관계 
frame[['age','pay']].corr()  # -1 ~ +1 
''' 상관계수 행렬
         age      pay
age  1.00000  0.94388
pay  0.94388  1.00000
'''

# 상관계수 상수
frame.age.corr(frame.pay)  # 0.9438798074485388

# 시각화
import matplotlib.pyplot as plt

age = frame.age
pay = frame.pay

plt.plot(age, pay, 'ro')
plt.show()

