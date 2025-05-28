'''
surprise Dataset 이용 
'''
import pandas as pd # DataFrame 생성 
from surprise import SVD, accuracy # SVD model 생성, 평가  
from surprise import Reader, Dataset # SVD dataset 생성  
from surprise.model_selection import train_test_split # dataset split 
 
############################
## suprise Dataset
############################

# 1. dataset loading 
ratings = pd.read_csv('C:/ITWILL/5_Python_ML/data/u.data', sep='\t', header=None)
print(ratings) 

# 칼럼명 수정 
ratings.columns = ['userId','movieId','rating','timestamp']
ratings.info() 
'''
RangeIndex: 100000 entries, 0 to 99999
Data columns (total 4 columns):
 #   Column     Non-Null Count   Dtype
---  ------     --------------   -----
 0   userId     100000 non-null  int64
 1   movieId    100000 non-null  int64
 2   rating     100000 non-null  int64
 3   timestamp  100000 non-null  int64
'''

ratings = ratings.drop('timestamp', axis = 1)
 

# 2. pivot table 작성 : 행(사용자), 열(영화제목), 셀(평점)
movie_ratings = pd.pivot_table(ratings,
               index = 'userId',
               columns = 'movieId',
               values = 'rating').reset_index()

movie_ratings.shape # (943, 1683) : (사용자수, 영화개수)



# 3. SVD dataset 
reader = Reader(rating_scale=(1, 5)) # 1 ~ 5점 
data = Dataset.load_from_df(ratings, reader)


# 4. train/test split : 80% vs 20%
trainset, testset = train_test_split(data, random_state=0) # test_size=0.2


# 5. svd model
svd_model= SVD(random_state=123).fit(trainset) # 80,000개 


# 6. 전체 testset 평점 예측
preds = svd_model.test(testset)
print(len(preds)) # 20,000

# 예측결과 출력 : 5명 예측 결과 
print('user\tmovie\trating\test_rating')
for p in preds[:5] : 
    print(p.uid, p.iid, p.r_ui, p.est, sep='\t\t')
  
       
# 7. model 평가 
accuracy.mse(preds) # 평균제곱오차 : 0.8976351072297628
accuracy.rmse(preds) # sqrt(평균제곱오차) : 0.947436070260027


# 8.추천대상자 평점 예측 

# 1) 추천대상자 선정 
movie_ratings.iloc[:5,:11] # 5행 11열 
'''
movieId   1    2    3    4    5    6    7    8    9    10
userId                                                   
1        5.0  3.0  4.0  3.0  3.0  5.0  4.0  1.0  5.0  3.0
2        4.0  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  2.0
3        NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
4        NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
5        4.0  3.0  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN <- 추천대상자 
'''

# 2) 영화10편에 대한 평점 예측 
uid = '5' # 추천대상자 
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 추천대상 영화제목(10개) 
actual_rating = [4.0, 3.0, 0, 0, 0, 0, 0, 0, 0, 0] # 실제 평점 


for iid, r_ui in zip(items, actual_rating):
    pred = svd_model.predict(uid, iid, r_ui) # (사용자, 아이템, 실제평점)
    print(pred)
    
'''
user: 5          item: 1          r_ui = 4.00   est = 3.96   {'was_impossible': False}
user: 5          item: 2          r_ui = 3.00   est = 3.37   {'was_impossible': False}
user: 5          item: 3          r_ui = 0.00   est = 3.23   {'was_impossible': False}
user: 5          item: 4          r_ui = 0.00   est = 3.63   {'was_impossible': False}
user: 5          item: 5          r_ui = 0.00   est = 3.38   {'was_impossible': False}
user: 5          item: 6          r_ui = 0.00   est = 3.83   {'was_impossible': False}
user: 5          item: 7          r_ui = 0.00   est = 3.83   {'was_impossible': False}
user: 5          item: 8          r_ui = 0.00   est = 4.04   {'was_impossible': False}
user: 5          item: 9          r_ui = 0.00   est = 4.02   {'was_impossible': False}
user: 5          item: 10         r_ui = 0.00   est = 3.93   {'was_impossible': False}

추천 item : item: 8, item: 9  
'''
    
    
    
    
    

