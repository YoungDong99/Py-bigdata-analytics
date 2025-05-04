"""
피벗테이블(pivot table) 
  - DF 객체를 대상으로 행과 열 그리고 교차 셀에 표시될 칼럼을 지정하여 만들어진 테이블 
   형식) pivot_table(DF, values='교차셀 칼럼',
                index = '행 칼럼', columns = '열 칼럼'
                ,aggFunc = '교차셀에 적용될 함수')  
"""

import pandas as pd 

path = r'C:\ITWILL\5_Python_ML\data'

# csv file 가져오기 
pivot_data = pd.read_csv(path + '/pivot_data.csv')
pivot_data.info()
'''
 0   year     8 non-null      int64  : 년도 
 1   quarter  8 non-null      object : 분기 
 2   size     8 non-null      object : 매출규모
 3   price    8 non-null      int64  : 매출액 
'''

# 1. 핏벗테이블 작성
ptable = pd.pivot_table(data=pivot_data, 
               values='price', 
               index=['year','quarter'], 
               columns='size', aggfunc='sum')


print(ptable)
'''
size          LARGE  SMALL
year quarter              
2016 1Q        2000   1000
     2Q        2500   1200
2017 3Q        2200   1300
     4Q        2800   2300
'''


# 핏벗테이블 시각화
import matplotlib.pyplot as plt
ptable.plot(kind='barh', stacked=True)
plt.show()


# 2. 범주형 변수 기준 통계구하기  
iris = pd.read_csv(path + '/iris.csv')
iris.info()


# 꽃의 종별 꽃받침길이와 꽃잎길이 통계 구하기  
table = pd.pivot_table(iris, values=['Sepal_Length', 'Petal_Length'], # 교차셀 칼럼
                       columns='Species', # 열 칼럼 
                       aggfunc= [sum, 'mean']) # 집계함수 

print(table)
'''
                sum                        mean                     
Species      setosa versicolor virginica setosa versicolor virginica
Petal.Length   73.1      213.0     277.6  1.462      4.260     5.552
Sepal.Length  250.3      296.8     329.4  5.006      5.936     6.588
'''

