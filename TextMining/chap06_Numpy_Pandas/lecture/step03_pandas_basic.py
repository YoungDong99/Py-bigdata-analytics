"""
Series & DataFrame

1. Series 자료 특징 
 - 1차원 구조
 - index와 value 구성

2. DataFrame 자료구조 특징 
 - 2차원 행렬구조(DB의 Table 구조와 동일함)
 - 칼럼 단위 상이한 자료형 
"""

import pandas as pd 


# 1. Series 객체 생성
ages = [35, 45, 55, 25]  # list
ser = pd.Series(ages) 
print(ser) 
'''
색인 자료
------------
0    35
1    45
2    55
3    25
dtype: int64
'''
ser[0]  # 35
ser[3]  # 25

ser.shape  # (4,) : 1차원(4개 원소)
dir(ser) # 분석도구
'''
index : 색인 추출
values : 값 추출

'''

ser.index # (start=0, stop=4, step=1) : 0부터 3까지 1씩 증가하는 인덱스
ser.values # [35, 45, 55, 25]


# 2. DataFrame 객체 생성 

# 1) list와 dict 이용  
names = ['hong', 'lee', 'kim', 'park']
ages = [35, 45, 55, 25]
pays = [250, 350, 450, 250]

frame = pd.DataFrame({'name':names, 'age': ages, 'pay': pays}) # dict
print(frame)
''' (테이블 형식)
   name  age  pay
0  hong   35  250
1   lee   45  350
2   kim   55  450
3  park   25  250
'''

frame.shape # (4, 3) : 4행 3열


# 행 이름과 열이름 
frame.index  # (start=0, stop=4, step=1)
frame.columns  # ['name', 'age', 'pay']

# DF 칼럼 추가 : Series 객체 이용 
gender = pd.Series(['M', 'M', 'F', 'F'])

frame['gender'] = gender # 성별 칼럼 

print(frame)
'''
   name  age  pay gender
0  hong   35  250      M
1   lee   45  350      M
2   kim   55  450      F
3  park   25  250      F
'''

type(frame)  # pandas.core.frame.DataFrame

dir(frame)

frame.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    4 non-null      object   : 문자형
 1   age     4 non-null      int64    : 정수형
 2   pay     4 non-null      int64    : 정수형
 3   gender  4 non-null      object   : 문자형
dtypes: int64(2), object(2)
memory usage: 260.0+ bytes
'''

# 숫자형 컬럼 : 수학/통계
age = frame.age   # DF.컬럼명 or DF['컬럼명']
age.mean()

pay = frame.pay
pay.mean()



# 문자형 컬럼(성별 범주 ) : 빈도분석
print(frame.gender.value_counts())   # 방법1
print(frame['gender'].value_counts()) # 방법2 (컬럼명에 공백, 특수문자 있을 시)
'''
M    2
F    2
'''


# 2) numpy 객체 이용
import numpy as np

data = np.arange(12).reshape(3, 4)  # 2차원 배열
print(data)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

# 1열 선택
# data[행,열]
data[:,1]  # [1, 5, 9] : 행 전체선택, 1열 지정
data[2,:]  # [ 8,  9, 10, 11]

frame2 = pd.DataFrame(data, columns=['a','b','c','d']) # 칼럼명 지정 

print(frame2)
'''
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''

# 1열 선택
# frame.칼럼명
frame2.a
'''
0    0
1    4
2    8
'''
