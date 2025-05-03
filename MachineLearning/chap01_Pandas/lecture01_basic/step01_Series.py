"""
Series 객체 특징 
 - pandas 1차원(vector) 자료구조 
 - DataFrame의 칼럼 구성요소 
 - 수학/통계 관련 함수 제공 
 - indexing/slicing 기능 
"""

import pandas as pd  
from pandas import Series 


# 1. Series 객체 생성 

# 1) list 이용 
price = pd.Series([3000,2000,1000,5200]) 
print(price)
'''
0    3000
1    2000
2    1000
3    5200
'''


# 2) dict 이용 
person = Series({'name':'홍길동', 'age':35, 'addr':'서울시'}) 
print(person)
''' (명칭 색인)
name    홍길동
age      35
addr    서울시
'''
person['name']  # '홍길동'


# 2. indexing/slicing 
ser = Series([4, 4.5, 6, 8, 10.5])  
print(ser)
'''
0     4.0
1     4.5
2     6.0
3     8.0
4    10.5
'''


ser[:] # 전체 원소 
ser[0] # 1번 원소 
ser[:3] # start~2번 원소 
ser[3:] # 3~end 원소 


# 3. Series 결합과 NA 처리 
s1 = pd.Series([3000, None, 2500, 2000],
               index = ['a', 'b', 'c', 'd'])  # index 생략시 기본 숫자형

s2 = pd.Series([4000, 2000, 3000, 1500],
               index = ['a', 'c', 'b', 'd'])


# Series 결합(사칙연산)
s3 = s1 + s2
print(s3)
'''
a    7000.0
b       NaN
c    4500.0
d    3500.0
'''


dir(s3) # 결측치 관련 메서드 
'''
fillna()  : 결측치 채우기 
isna()    : 결측치(True)
isnull()  : 결측치(True) 
notnull() : 결측치(False)
'''

# 결측치 처리(NaN)
'''
 - Not a Number
 - 잘못된 입력으로 인해 계산을 할 수 없음을 나타내는 기호
'''
# 결측치 발견
s3.isna()
s3.isnull()
''' (결측치 True)
a    False
b     True
c    False
d    False
'''

s3.notnull()
''' (결측치 False)
a     True
b    False
c     True
d     True
'''

result = s3.fillna(s3.mean())
print(result)

result2 = s3.fillna(0)
print(result2)


# 결측치 제거 
result3 = s3[s3.notnull()]  # [조건식] : 식 대신 T/F 반환하는 함수 사용
result4 = s3[~(s3.isna())]  # True -> False : 결과 동일
print(result3)
print(result4)
'''
a    7000.0
c    4500.0
d    3500.0
'''

s3[s3 > 0]  # 연산자로 결측치 제거
'''
a    7000.0
c    4500.0
d    3500.0
'''


# 4. Series 연산 

# 1) 범위 수정 
print(ser)
ser[1:4] = 5.0  # 범위 내의 값 전부 5.0으로 수정



# 2) broadcast 연산 
print(ser * 0.5) 

# 3) 수학/통계 함수 
ser.mean() # 평균
ser.sum() # 합계
ser.var() #  분산
ser.std() # 표준편차
ser.max() # 최댓값
ser.min() # 최솟값
ser.mode() # 최빈수 : 5.0

