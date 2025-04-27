"""
DataFrame 자료 참조 
"""

import pandas as pd 


### 1. DF 칼럼(열) 자료 참조  
path = r'C:\ITWILL\3_TextMining\data' # 경로 변경 

emp = pd.read_csv(path + "/emp.csv", encoding='utf-8')
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
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
'''


# 1) 단일 칼럼 
no = emp.No # 방법1 : DF.컬럼명
name = emp['Name'] # 방법2 : DF['컬럼명']


# 2) 복수 칼럼 : 중첩 list 
no_pay = emp[['No','Pay']]


### 2. DF 행 자료 참조
emp.index # (start=0, stop=5, step=1) : 행 이름

emp[0] # KeyError

# 1) 정수 색인 : iloc
emp.iloc[0] # 1행 
emp.iloc[:3] # 1~3행 (start ~ stop-1)

# 2) 명칭 색인 : loc
emp.loc[0] # 1행 
emp.loc[:3] # 1~4행 (start ~ stop)
# 숫자를 색인이 아닌 명칭으로 해석


# 3) 조건식으로 행 선택 
pay350 = emp[emp.Pay > 350] 
print(pay350)


### 3. DF 행열 자료 참조  

# 1) 정수 색인 : DF.iloc[행, 열]
emp.iloc[0:3, 0:3] # 연속 열 선택
emp.iloc[0:3, [0,2]] # 비연속 열 선택  

# 2) 명칭 색인 : DF.loc[행, 열] 
emp.loc[0:3, 'No':'Pay'] # 연속 열 선택 
emp.loc[0:3, ['No','Pay']] # 비연속 열 선택 


 