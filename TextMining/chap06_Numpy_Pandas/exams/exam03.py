"""
문3) review_data.csv 파일의 칼럼을 이용하여 각 단계별로 작업을 수행하시오.
"""

import pandas as pd

# 1. file load 
path = r'C:\ITWILL\3_TextMining/data'
review_data = pd.read_csv(path + '/review_data.csv', encoding='utf-8')

review_data.info()
'''
RangeIndex: 34525 entries, 0 to 34524
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   id       34525 non-null  int64 
 1   review   34525 non-null  object
 2   label    34525 non-null  int64 : 긍정(1) or 부정(0)
 3   review2  34525 non-null  object : 영화리뷰 
''' 

# 단계1. lable, review2 칼럼 선택 
review_df = review_data[['label', 'review2']]
print(review_df)

# 단계2. label 칼럼의 각 범주에 대한 빈도수 확인 : 긍정(1) or 부정(0) 
label = review_df.label
label.value_counts()
print(label)

# 단계3-1. label 칼럼을 기준으로 긍정문서 전체 행 선택  
pos_all = review_df[label == 1]
print(pos_all)


# 단계3-2. 긍정문서 전체 행에서 앞부분 10개 행 추출 
pos_row10 = pos_all.iloc[:10]
print(pos_row10)


# 단계4-1. label 칼럼을 기준으로 부정문서 전체 행 선택  
neg_all = review_df[label == 0]
print(neg_all)


# 단계4-2. 부정문서 전체 행에서 앞부분 10개 행 추출
neg_row10 = neg_all.loc[:10]
print(neg_row10)


