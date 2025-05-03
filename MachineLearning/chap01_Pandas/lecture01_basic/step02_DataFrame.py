"""
DataFrame 자료구조 특징 
 - 2차원 행렬구조(DB의 Table 구조와 동일함)
 - 칼럼 단위 상이한 자료형 
"""

import pandas as pd 
from pandas import DataFrame 


# 1. DataFrame 객체 생성 

# 1) list와 dict 이용 
names = ['hong', 'lee', 'kim', 'park']
ages = [35, 45, 55, 25]
pays = [250, 350, 450, 250]


# key -> 칼럼명, value -> 칼럼값 
frame = pd.DataFrame({'name':names, 'age': ages, 'pay': pays})
frame
'''
   name  age  pay
0  hong   35  250
1   lee   45  350
2   kim   55  450
3  park   25  250
'''


# 객체 정보 
frame.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3 : 행 길이
Data columns (total 3 columns): 열 길이
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    4 non-null      object : 문자형
 1   age     4 non-null      int64  : 숫자형
 2   pay     4 non-null      int64  : 숫자형
dtypes: int64(2), object(1)
'''


# 2) numpy 객체 이용
import numpy as np

data = np.arange(12).reshape(3, 4) # 1d -> 2d
print(data) 
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''


# numpy -> pandas
frame2 = DataFrame(data, columns=['a','b','c','d'])
frame2
'''
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''


# 2. DF 칼럼 참조 
path = r'C:/ITWILL/5_Python_ML/data' # 경로 지정
emp = pd.read_csv(path + "/emp.csv", encoding='utf-8')
type(emp)  # 외부파일로 DataFrame 만들기
print(emp.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   No      5 non-null      int64 
 1   Name    5 non-null      object
 2   Pay     5 non-null      int64 
'''

print(emp)
'''
    No   Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
'''


# 1) 단일 칼럼
no = emp.No # 방법1
print(no)
name = emp['Name'] # 방법2
print(name)


# 2) 복수 칼럼  
df = emp[['No','Pay']]  # 중첩 리스트 형식
print(df)


# 3. DataFrame 행열 참조 

# 1) loc 속성 : 명칭 기반 
emp.loc[0, :] # 1행 전체 
emp.loc[0] # 열 생략 가능 
emp.loc[0:2] # 1~3행 전체 (0,1,2 선택)
# 숫자 색인은 명칭으로 해석
emp.loc[0:2, ['Name','Pay']] # 2행과 3행의 Name과 Pay : 색인이 명칭이면 명칭사용
# 숫자 색인은 명칭으로 해석 


# 2) iloc 속성 : 숫자 위치 기반 
emp.loc[0] # 1행 전체 
emp.iloc[0:2] # 1~2행 전체 (0,1 선택)
emp.iloc[:,1:] # 2번째 칼럼 이후 연속 칼럼 선택
#emp.iloc[:, ['No', 'Pay']] # 명칭 색인 : 오류
emp.iloc[:, [0, 2]]

# 행,열 선택
emp.iloc[[0,2], [0,2]]
'''
    No  Pay
0  101  150
2  103  500
'''

# 4. subset 만들기 : old DF -> new DF

# 1) 특정 칼럼 선택
subset1 =  emp[['Name', 'Pay']]  # 복수컬럼 선택
print(subset1)


# 2) 특정 행 제외 
subset2 = emp.drop(1) # 2행 제외  
print(subset2)


# 3) 조건식으로 행 선택   
subset3 = emp[emp.Pay >= 350] # 급여 350 이하 제외 
print(subset3)


# 논리연산자 이용 : &(and), |(or), ~(not) 
emp[(emp.Pay >= 300) & (emp.Pay <= 400)] # 급여 300 ~ 400   
emp[~ ((emp.Pay >= 300) & (emp.Pay <= 400))] # not 300~400
emp[(emp.Pay >= 400) | (emp.Name == '홍길동')] # 급여 400 이상과 홍길동


# 4) 칼럼값 이용 : 범주형 칼럼 대상
iris = pd.read_csv(path + '/iris.csv')  # 붖꽃
iris.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Sepal.Length  150 non-null    float64
 1   Sepal.Width   150 non-null    float64
 2   Petal.Length  150 non-null    float64
 3   Petal.Width   150 non-null    float64
 4   Species       150 non-null    object  : 꽃의 종(3가지)
'''

#iris.Sepal.Length  # 오류
iris['Sepal.Width']  # 특수문자(.) 포함된 칼럼 선택 방법

print(iris.Species.unique()) # ['setosa' 'versicolor' 'virginica']

subset4 = iris[iris.Species.isin(['setosa', 'virginica'])]
subset4.shape  # (100, 5)


# 5) columns 이용 : 칼럼이 많은 경우 칼럼명 이용  
iris = pd.read_csv(path + '/iris.csv')
iris  # [150 rows x 5 columns]

names = list(iris.columns) # 전체 칼럼명 list 반환 
names # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

# x변수(독립변수) 선택 
iris_x = iris[names[:4]]  # 변수 4개
iris_x  # [150 rows x 4 columns]

iris_y = iris.Species  # 칼럼명 이용
iris_y = iris[names[-1]]  # 변수 이용
iris_y # 결과 동일


# (변수없이)컬럼명으로 선택하는 방법
iris[['Sepal.Length', 'Petal.Length']]

# 행 개수 선택 방법
iris_z = iris[:3]
iris_z  
