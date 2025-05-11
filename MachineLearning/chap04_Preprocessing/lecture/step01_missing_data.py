######################################
### 결측치 처리
######################################

'''
 - 결측치 확인 및 처리(대체 또는 제거) 
'''

import pandas as pd

path = r'C:\ITWILL\5_Python_ML\data'
data = pd.read_csv(path +'/dataset.csv') 
data.info()
'''
 0   resident  217 non-null    int64  
 1   gender    217 non-null    int64  
 2   job       205 non-null    float64
 3   age       217 non-null    int64  
 4   position  208 non-null    float64
 5   price     217 non-null    float64
 6   survey    217 non-null    int64  
'''
data.shape # (217, 7) 


# 1. 결측치(NaN) 확인  
data.isnull().any() 
data.isnull().sum() 
'''
job         12
position     9
'''


# 2. 전체 칼럼 기준 결측치 제거 
new_data = data.dropna() 
new_data.shape # (198, 7)
217 - 198 # 19


# 3. 특정 칼럼 기준 결측치 제거   
new_data2 = data.dropna(subset ='job')  
new_data2.shape  # (205, 7)

new_data2.isnull().sum()
'''
job         0
position    7
'''


# 4. 모든 변수 결측치 대체 : 숫자형변수(상수 or 통계 대체)   
new_data3 = data.fillna(0.0) # 0으로 채우기 
new_data3.shape # (217, 7) 
new_data3.isnull().sum()


# 5-1. 특정변수 결측치 대체 : 숫자형변수(상수 or 통계 대체) 
new_data4 = data.copy() # 내용복제
new_data4.isna().sum() 


# 'position' 칼럼 결측치 : 평균 대체  
new_data4['position'] = new_data4['position'].fillna(new_data4['position'].mean())
new_data4.isna().sum()   
# position     0


# 5-2. 특정변수 결측치 대체 : 범주형변수(빈도수가 높은 값으로 대체)  
new_data5 = data.copy() # 내용복제 
new_data5['job'].value_counts()
'''
job
3.0    77
2.0    74
1.0    54
'''

new_data5['job'].fillna(3.0, inplace=True) # inplace=True : 현재 객체 반영 
new_data5.isna().sum()
# job         0


# 6. 결측치 비율 40% 이상 : 해당 컬럼 변수에서 제거 
data.isna().sum() # job 칼럼 제거 
new_data6 = data.drop(['job'], axis = 1)  # 열축 방향 
new_data6.info()


# 각 칼럼의 결측치 비율 계산 
data.isnull().sum() / len(data)
'''
job         0.055300
age         0.000000
position    0.041475
'''








