"""
문1) 다음과 같은 100명의 여행지 평점 데이터를 이용하여 여행지를 추천하는 모델을 단계별로 작성하시오. 
"""

import pandas as pd
import numpy as np
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split


np.random.seed(42)  


# 1. 사용자-여행지 평점 데이터 생성 (100명)
user_ids = np.random.randint(1, 31, size=100)  # 사용자 ID
destinations = ['Paris', 'London', 'Rome', 'New York', 'Tokyo', 'Seoul', 'Sydney', 'Bangkok', 'Berlin', 'Barcelona']
destination_choices = np.random.choice(destinations, size=100)
ratings = np.random.randint(1, 6, size=100)  # 평점 1~5

# 데이터프레임 생성
data = {
    'user_id': user_ids,
    'destination': destination_choices,
    'rating': ratings
}

df = pd.DataFrame(data)
df.info()
'''
RangeIndex: 100 entries, 0 to 99
Data columns (total 3 columns):
 #   Column       Non-Null Count  Dtype 
---  ------       --------------  ----- 
 0   user_id      100 non-null    int32  : 사용자 
 1   destination  100 non-null    object : 여행지 
 2   rating       100 non-null    int32  : 평점 
'''


# 2. 피벗테이블 
ptable = pd.pivot_table(df, 
                        values='rating', # 셀 : 평점(1~5점) 
                        index='user_id', # 행 : 사용자 
                        columns='destination') # 열 : 아이템(여행지)
print(ptable)
'''
destination  Bangkok  Barcelona  Berlin  ...  Seoul    Sydney  Tokyo
user_id                                  ...                        
1                NaN        3.0     NaN  ...    NaN       NaN    NaN
2                2.0        NaN     1.0  ...    NaN       NaN    5.0
3                2.0        NaN     2.5  ...    NaN       NaN    NaN
4                NaN        4.0     2.0  ...    2.0       NaN    4.0
5                NaN        2.0     NaN  ...    NaN       NaN    NaN
6                NaN        NaN     NaN  ...    NaN       NaN    3.0
7                NaN        1.0     NaN  ...    NaN  1.000000    1.0
8                2.0        NaN     NaN  ...    NaN  5.000000    NaN
9                NaN        NaN     NaN  ...    5.0       NaN    NaN
10               NaN        NaN     NaN  ...    NaN       NaN    4.0  <- 추천대상자 
생략 
29               3.5        NaN     NaN  ...    4.0  3.000000    1.0
30               NaN        NaN     2.0  ...    NaN       NaN    NaN
'''


# 3. rating 데이터셋 생성 
reader = Reader(rating_scale = (1,5)) # 평점 범위 
data = Dataset.load_from_df(df, reader)


# 4. 데이터 분할 : trainset(95%) vs testsest(5%)
trainset, testset = train_test_split(data,
                                     test_size=0.05,
                                     random_state=1)

len(testset) # 5개

# 5. svd model 생성 : 훈련셋 이용 
model = SVD(random_state=1).fit(trainset) # 95개 학습 

dir(model)
'''
predict() : 추천대상자 평점 예측 
test() : 평가셋으로 평가 
'''
# 6. svd model 평가 & 평점예측 : 평가셋 이용 x
test_pred = model.test(testset)
print(test_pred)

# 양식으로 출력 
for row in test_pred :
    print(f'user={row.uid}, iid={row.iid}, r_ui={row.r_ui}, est={row.est}')
    
# 평가예측 <출력결과 예시>   
'''
user=28, iid=Barcelona, r_ui=4.0, est=3.1126639943197794
user=26, iid=Bangkok, r_ui=1.0, est=2.8592551341465215
user=20, iid=Tokyo, r_ui=3.0, est=2.6574761160796845
user=11, iid=Berlin, r_ui=2.0, est=2.3336751512884515
user=17, iid=Sydney, r_ui=4.0, est=2.7606909529538224
'''



# 7. 추천대상자(user_id = 10) 추천대상자를 대상으로 10개 도시의 평점 예측 

print(ptable.loc[10]) # 현재 10번 사용자(user_id)의 10개 도시 평점 현황   
'''
destination
Bangkok      NaN
Barcelona    NaN
Berlin       NaN
London       NaN
New York     NaN
Paris        NaN
Rome         1.0
Seoul        NaN
Sydney       NaN
Tokyo        4.0
'''

user_id = '10' # 추천대상자 
items = sorted(destinations)  # 10개 여행지(도시) 오름차순 정렬 
actual_rating = [0,0,0,0,0,0,1.0,0,0,4.0] # 실제 평점 

print('추천대상자 :', user_id)
for iid, rating in zip(items, actual_rating) :
    y_pred = model.predict(user_id, iid, rating)
    print(y_pred)   

'''
추천대상자 : 10est = 2.56   {'was_impossible': False}
user: 10         item: Barcelona  r_ui = 0.00   e
user: 10         item: Bangkok    r_ui = 0.00   st = 2.67   {'was_impossible': False}
user: 10         item: Berlin     r_ui = 0.00   est = 2.59   {'was_impossible': False}
user: 10         item: London     r_ui = 0.00   est = 3.08   {'was_impossible': False}
user: 10         item: New York   r_ui = 0.00   est = 2.56   {'was_impossible': False}
user: 10         item: Paris      r_ui = 0.00   est = 2.66   {'was_impossible': False}
user: 10         item: Rome       r_ui = 1.00   est = 2.79   {'was_impossible': False}
user: 10         item: Seoul      r_ui = 0.00   est = 2.96   {'was_impossible': False}
user: 10         item: Sydney     r_ui = 0.00   est = 2.87   {'was_impossible': False}
user: 10         item: Tokyo      r_ui = 4.00   est = 2.65   {'was_impossible': False}
'''










