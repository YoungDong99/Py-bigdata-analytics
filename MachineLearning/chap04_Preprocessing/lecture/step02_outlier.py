######################################
### 2. 이상치 처리 
######################################
"""
 이상치(outlier) 처리 : 정상범주에서 벗어난 값(극단적으로 크거나 작은 값) 처리  
  - IQR(Inter Quentile Range) 방식으로 탐색과 처리   
"""

import pandas as pd 
import matplotlib.pyplot as plt  # plt.boxplot

path = r'C:\ITWILL\5_Python_ML\data'
data = pd.read_csv(path + "/insurance.csv") # 의료비 관련 
data.info()
'''
RangeIndex: 1338 entries, 0 to 1337
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   age       1338 non-null   int64   : 비율척도  
 1   sex       1338 non-null   object 
 2   bmi       1338 non-null   float64 : 비율척도
 3   children  1338 non-null   int64  
 4   smoker    1338 non-null   object 
 5   region    1338 non-null   object 
 6   charges   1338 non-null   float64 : 비율척도
'''
 
# 1. 범주형 변수 이상치 탐색  
data.sex.unique() # ['female', 'male']
data.smoker.unique() # ['yes', 'no']
data.region.unique() # ['southwest', 'southeast', 'northwest', 'northeast']


# 2. 숫자형 변수 이상치 탐색  
des = data.describe() # 요약통계량 
print(des)
'''
               age          bmi     children       charges
count  1338.000000  1338.000000  1338.000000   1338.000000
mean     39.730194    30.524488     1.094918  13270.422265
std      20.224425     6.759717     1.205493  12110.011237
min      18.000000   -37.620000     0.000000   1121.873900
25%      27.000000    26.220000     0.000000   4740.287150
50%      39.000000    30.332500     1.000000   9382.033000
75%      51.000000    34.656250     2.000000  16639.912515
max     552.000000    53.130000     5.000000  63770.428010
'''

# 3. boxplot 이상치 발견 및 처리 

# 1) boxplot 이상치 발견  
plt.boxplot(data.age) # age 이상치  
plt.show()

plt.boxplot(data.bmi) # bmi 이상치 
plt.show()


# 2) 이상치 처리 

# [1] bmi 이상치 제거 
df = data.copy() # 복제
df = df[df.bmi > 0] # 이상치 제거 

plt.boxplot(df.bmi) # bmi 이상치 
plt.show()

# [2] age 이상치 대체   
df2 = data.copy() # 복제
df2[df2.age > 100] # 100세 이상 확인    
df2.loc[df2.age > 100, 'age'] = 100 # 이상치 대체 

plt.boxplot(df2.age) # bmi 이상치 
plt.show()


# 4. IQR방식 이상치 발견 및 처리 

# 1) IQR방식으로 이상치 발견   
'''
 IQR = Q3 - Q1 : 제3사분위수 - 제1사분위수
 outlier_step = 1.5 * IQR
 정상범위 : Q1 - outlier_step ~ Q3 + outlier_step
'''  

Q3 = des.loc['75%', 'age'] # [행이름, 열이름]
Q1 = des.loc['25%', 'age'] 
IQR = Q3 - Q1

outlier_step = 1.5 * IQR # 36.0

minval = Q1 - outlier_step
maxval = Q3 + outlier_step
# 정상범주 
print(f'minval : {minval}, maxval : {maxval}') 
# minval : -9.0, maxval : 87.0

# 2) 이상치 제거  
df3 = data.copy() # 복제 
df3 = df3[(df3.age >= minval) & (df3.age <= maxval)]

# 이상치 확인 
data[(data.age < minval) | (data.age > maxval)]

# 나이 시각화 
df3.age.plot(kind='box')
plt.show()




