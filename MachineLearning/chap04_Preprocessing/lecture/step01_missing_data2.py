######################################
### 결측치 처리
######################################

'''
- 특수문자를 결측치로 처리하는 방법 
'''

import pandas as pd 
pd.set_option('display.max_columns', 50) # 최대 50 칼럼수 지정

# 자료형 확인 & 변경
data = pd.Series([1,2,'3'])



# 데이터셋 출처 : kaggle
path = r'C:\ITWILL\5_Python_ML\data'
cencer = pd.read_csv(path + '/brastCencer.csv')
cencer.info()
'''
RangeIndex: 699 entries, 0 to 698
Data columns (total 11 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   id               699 non-null    int64  -> 제거 
 1   clump            699 non-null    int64 
 2   cell_size        699 non-null    int64 
 3   cell_shape       699 non-null    int64 
 4   adhesion         699 non-null    int64 
 5   epithlial        699 non-null    int64 
 6   bare_nuclei      699 non-null    object -> 노출원자핵 : 숫자형 변환
 7   chromatin        699 non-null    int64 
 8   normal_nucleoli  699 non-null    int64 
 9   mitoses          699 non-null    int64 
 10  class            699 non-null    int64 -> y변수 
'''

print(cencer.bare_nuclei)
print(cencer['class'].unique()) # [2 4]


## 1. 변수 제거 
df = cencer.drop(['id'], axis = 1) # 열축 기준 : id 칼럼 제거  


## 2. x변수 숫자형 변환 : object -> int형 변환  
df['bare_nuclei'] = df['bare_nuclei'].astype('int') # error 발생 
# ValueError: invalid literal for int() with base 10: '?'


## 3. 특수문자 결측치 처리 & 자료형 변환 

# 1) 특수문자 결측치 대체   
import numpy as np 
df['bare_nuclei'] = df['bare_nuclei'].replace('?', np.nan) 


# 2) 전체 칼럼 단위 결측치 확인 
df.isnull().any() 
df.isnull().sum() # bare_nuclei        16


# 3) 결측치 제거
new_df = df.dropna(subset=['bare_nuclei'])
new_df.shape # (683, 10) : 16개 제거 


# 4) int형 변환 
new_df['bare_nuclei'] = new_df['bare_nuclei'].astype('int64') 
new_df.info()


## 4. y변수 레이블 인코딩 : 10진수 변환 
from sklearn.preprocessing import LabelEncoder 


# 레이블 인코딩 
labels = LabelEncoder().fit_transform(new_df['class']) # data 적용 & 변환   
new_df['labels'] = labels # 칼럼 추가 

new_df.info()

new_df = new_df.drop(['class'], axis = 1)
 
