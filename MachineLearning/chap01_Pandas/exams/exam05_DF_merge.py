'''   
lecture02 > step01 관련문제

문5) iris.csv 파일을 읽어와서 다음과 같이 처리하시오.
   <단계1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
   <단계2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기 
   <단계3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
   <단계4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성      
'''

import pandas as pd

path = r'C:\ITWILL\5_Python_ML\data'

iris = pd.read_csv(path + '/iris.csv')
print(iris.info())

# <단계1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
col1 = iris['Sepal.Length']
col2 = iris['Sepal.Width']
col3 = iris['Petal.Length']
col4 = iris['Petal.Width']


# <단계2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기
col1.sum()
col1.mean()
col1.std()

col4.sum()
col4.mean()
col4.std()

# <단계3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
df1 = pd.concat(objs=[col1, col2], axis = 1)
df2 = pd.concat(objs=[col3, col4], axis = 1)

df1
df2

# <단계4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성
iris_df = pd.concat(objs=[df1, df2], axis = 1)

iris_df
# [150 rows x 4 columns]

