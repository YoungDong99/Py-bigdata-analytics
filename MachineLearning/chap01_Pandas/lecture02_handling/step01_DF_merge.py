"""
step01_DF_merge.py

 DF 병합(merge) : 공통칼럼(o) 
 DF3 = DF1(id) + DF2(id)
 
 DF 결합(concat) : 공통칼럼(x) 
"""

import pandas as pd 
pd.set_option('display.max_columns', 100) # 콘솔에서 보여질 최대 칼럼 개수 

path = r'C:\ITWILL\5_Python_ML\data'

wdbc = pd.read_csv(path + '/wdbc_data.csv')
wdbc.info()
'''
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
'''
print(wdbc)

# 전체 칼럼 가져오기 
cols = list(wdbc.columns)
cols 

# 1. DF 병합(merge) : 공통칼럼(o)
DF1 = wdbc[cols[:16]] # 앞부분 16개 변수 
DF2 = wdbc[cols[16:]] # 뒷부분 16개 변수 
# id칼럼 추가 
DF2['id'] = wdbc.id


DF3 = pd.merge(left=DF1, right=DF2, on='id') # 공통칼럼('id')=내부조인 
DF3.shape # (569, 32)


# 2. DF 결합(concat) : 공통칼럼(x)
DF2 = wdbc[cols[16:]]

DF4 = pd.concat(objs=[DF1, DF2], axis = 1) # 열축 기준 결합
DF1.shape # (569, 16)
DF2.shape # (569, 16)
DF4.shape # (569, 32)

DF5 = pd.concat(objs=[DF1, DF2], axis = 0) # 행축 기준 결합 
DF5.shape # (1138, 32)


# 3. Inner join과 Outer join 
name = ['hong','lee','park','kim']
age = [35, 20, 33, 50]

df1 = pd.DataFrame(data = {'name':name, 'age':age}, 
                   columns = ['name', 'age'])
'''
   name  age
0  hong   35
1   lee   20
2  park   33
3   kim   50
'''

name2 = ['hong','lee','kim']
age2 = [35, 20, 50]
pay = [250, 350, 250]

df2 = pd.DataFrame(data = {'name':name2, 'age':age2,'pay':pay}, 
                   columns = ['name', 'age', 'pay'])
'''
   name  age  pay
0  hong   35  250
1   lee   20  350
2   kim   50  250
'''

# on 생략 : 동일 변수명으로 공통칼럼 사용 
inner = pd.merge(left=df1, right=df2, how='inner') # 기본값(inner)
inner
'''
   name  age  pay
0  hong   35  250
1   lee   20  350
2   kim   50  250
'''

outer = pd.merge(left=df1, right=df2, how='outer') # 외부조인   
outer
'''
   name  age    pay
0  hong   35  250.0
1   kim   50  250.0
2   lee   20  350.0
3  park   33    NaN
'''


