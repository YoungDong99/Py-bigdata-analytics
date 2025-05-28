"""
- 특이값 분해(SVD) 알고리즘 이용 추천 시스템

<준비물>
 scikit-surprise 패키지 설치 
> pip install scikit-surprise : 의존성 문제 발생  
> conda install -c conda-forge scikit-surprise 
"""

import pandas as pd # csv file 
from surprise import SVD # SVD model 
from surprise import Reader, Dataset # SVD dataset 
from surprise.model_selection import train_test_split # data split 

# 1. dataset loading 
ratings = pd.read_csv('C:/ITWILL/5_Python_ML/data/movie_rating.csv')
print(ratings) #  평가자[critic]   영화[title]  평점[rating]


# row(영화제목), column(평가자), cell(평점)
movie_ratings = pd.pivot_table(ratings,
               index = 'title',
               columns = 'critic',
               values = 'rating').reset_index()


# 2. SVD dataset 생성 
reader = Reader(rating_scale=(1, 5)) # 평점 : 1~5
data = Dataset.load_from_df(ratings, reader)


# 3. train/test split 
trainset, testset = train_test_split(data, test_size=0.1,
                                      random_state=1)
type(trainset) # surprise.trainset.Trainset  : 27개 
len(testset) # 4개 


# 4. SVD model 생성 
model = SVD(random_state=123).fit(trainset) 


# 5. 전체 평가셋 예측 
test_pred = model.test(testset)
print(test_pred) # uid=사용자, iid=상품(영화), r_ui=실제평점, est=예측평점 
'''
[Prediction(uid='Mick', iid='Superman', r_ui=3.0, est=3.4245230896766876, details={'was_impossible': False}), 
 Prediction(uid='Claudia', iid='Just My', r_ui=3.0, est=3.1022804985064996, details={'was_impossible': False}), 
 Prediction(uid='Claudia', iid='Snakes', r_ui=3.5, est=3.60996210101588, details={'was_impossible': False}), 
 Prediction(uid='Mick', iid='Lady', r_ui=3.0, est=2.8720504028984464, details={'was_impossible': False})]
'''

# 양식으로 출력 
for row in test_pred :
    print(f'uid = {row.uid}, iid={row.iid}, r_ui={row.r_ui}, est={row.est}')
    
'''
uid = Mick, iid=Superman, r_ui=3.0, est=3.4245230896766876
uid = Claudia, iid=Just My, r_ui=3.0, est=3.1022804985064996
uid = Claudia, iid=Snakes, r_ui=3.5, est=3.60996210101588
uid = Mick, iid=Lady, r_ui=3.0, est=2.8720504028984464
'''
    

# 6. Toby 사용자 영화 추천 예측 
user_id  = 'Toby' # 추천대상자  
items = ['Just My','Lady','The Night'] # 미관람영화(추천영화)  
actual_rating = 0 # 실제평점 

for item_id in items :
    svd_pred = model.predict(user_id, item_id, actual_rating)
    print(svd_pred)

'''
user: Toby       item: Just My    r_ui = 0.00   est = 3.01   
user: Toby       item: Lady       r_ui = 0.00   est = 2.90   
user: Toby       item: The Night  r_ui = 0.00   est = 3.18 -> 추천영화   
'''


