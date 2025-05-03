"""
1. DataFrame의 요약통계량 
2. 상관계수
"""

import pandas as pd 

path = r'C:\ITWILL\5_Python_ML\data'

product = pd.read_csv(path + '/product.csv')


# DataFrame 정보 보기 
product.info()


# 앞부분/뒷부분 관측치 5개 보기 
product.head()
product.tail()

# 1. DataFrame의 요약통계량 
summ = product.describe()
print(summ)
'''
                a           b           c
count  264.000000  264.000000  264.000000
mean     2.928030    3.132576    3.094697
std      0.970345    0.859657    0.828744
min      1.000000    1.000000    1.000000
25%      2.000000    3.000000    3.000000
50%      3.000000    3.000000    3.000000
75%      4.000000    4.000000    4.000000
max      5.000000    5.000000    5.000000
'''
summ.loc['mean']
q1 = summ.loc['25%']
q3 = summ.loc['75%']

result = q3 - q1
result

# 행/열 통계
product.shape # (264, 3)
product.sum(axis = 0) # 행축  
product.sum(axis = 1) # 열축 


# 산포도 : 분산, 표준편차 
product.var() # axis = 0
product.std() # axis = 0

# 빈도수 : 집단변수 
product['a'].value_counts()
'''
3    126
4     64
2     37
1     30
5      7
'''


# 유일값 
product['b'].unique()  # [4, 3, 2, 5, 1]

# 2. 상관관계 
cor = product.corr()
print(cor) # 상관계수 행렬 


