"""
step02_DF_reshape.py

- DataFrame 모양 변경 
"""

import pandas as pd 

path = r'C:\ITWILL\5_Python_ML\data'

buy = pd.read_csv(path + '/buy_data.csv')

print(buy.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Date         22 non-null     int64
 1   Customer_ID  22 non-null     int64
 2   Buy          22 non-null     int64
'''
buy.shape  # (22, 3)

dir(buy)
'''
stack() : 2d -> 1d
unstack() : 1d -> 2d
duplicated() : 중복행 확인
drop_duplicates() : 중복행 제거
set_index() : 특정 칼럼 색인 적용
'''


# 1. 2차원 -> 1차원 구조 변경
buy_long = buy.stack() 
buy_long.shape  # (66,)


# 2. 1차원 -> 2차원 구조 변경 
buy_wide = buy_long.unstack()
buy_wide.shape  # (22, 3)


# 3. 전치행렬 (행, 열 전환)
buy_tran = buy.T
buy_tran.shape  # (3, 22)


# 4. 중복 행 제거 
buy.duplicated()  # 중복행 확인 : True 값
buy2 = buy.drop_duplicates() # 중복 행 제거
buy2.shape # (20, 3)


# 5. 특정 칼럼을 index 지정 
new_buy = buy.set_index('Date') # 구매날짜 
new_buy

# 날짜 검색 
new_buy.loc[20150101] # 명칭색인 
#new_buy.iloc[20150101] # 오류 : out-of-bounds : 색인 범위 초과 
# 색인 자료형은 int형이지만 동일한 구매날짜를 명칭으로 지정한다.  



