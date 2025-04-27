'''
문4) bmi.csv 파일의 자료를 이용하여 각 단계별로 통계 분석을 수행하시오.
'''

import pandas as pd 


# 1. DF 칼럼 선택 : 칼럼 선택 목적 
path = r'C:\ITWILL\3_TextMining\data' # 경로 변경 

bmi = pd.read_csv(path + "/bmi.csv", encoding='utf-8')
print(bmi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20000 entries, 0 to 19999
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   height  20000 non-null  int64 
 1   weight  20000 non-null  int64 
 2   label   20000 non-null  object
'''


# 단계1 : height와 weight 요약통계
bmi.describe() # 숫자형 칼럼만 자동 적용 
desc = bmi[['height', 'weight']].describe()
print(desc)

# 단계2 : height와 weight 표준편차 
std = bmi[['height', 'weight']].std()
print(std)

# 단계3 : height와 weight 상관계수 
corr = bmi.height.corr(bmi.weight)
print(corr)

# 단계4 : label 빈도수 
print(bmi.label.value_counts())
'''
label
normal    7677
fat       7425
thin      4898
'''

