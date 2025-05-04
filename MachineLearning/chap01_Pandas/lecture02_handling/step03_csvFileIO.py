"""
step03_csvFileIO.py
"""

import pandas as pd 

path = r'C:\ITWILL\5_Python_ML\data'

# 1. csv file read

# 1) 칼럼명이 없는 경우 
st = pd.read_csv(path + '/student.csv', header=None) 
st # 0     1    2   3 -> 기본 칼럼명 

# 칼럼명 수정 
col_names = ['sno','name','height','weight'] # list 
st.columns = col_names # 칼럼 수정 
print(st)


# 2) 칼럼명 특수문자(.) or 공백 
iris = pd.read_csv(path + '/iris.csv')
print(iris.info())


# 점(.) -> 언더바(_) 교체 
iris.columns = iris.columns.str.replace('.','_') # ('old','new')
iris.info() # Sepal_Length


# 3) 천단위 콤마 서식 -> 숫자형으로 읽기  
pd.read_csv(path + '/국민건강보험_건강검진정보.csv', thousands=",") # 123,123

# 4) 칼럼 구분 : delimiter='\t' or sep="\t"
pd.read_csv(path + '/World Indicators.csv', encoding='utf-16le', sep="\t")


# 2. data 처리 : 파생변수 추가 
'''
비만도 지수(bmi) = 몸무게/(키**2)
'''

bmi = st.weight / (st.height*0.01)**2
bmi
    
# 파생변수 추가 
st['bmi'] = bmi


'''
label : normal, fat, thin 
normal : bmi : 18 ~ 23
fat : 23 초과
thin : 18 미만  
'''

# 3. csv file 저장 
st.to_csv(path + '/st_info.csv', index = None, encoding='utf-8')
# index = None : 행이름 저장 안함 


