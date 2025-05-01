"""
문) 각 단계별로 Naive Bayes 학습모델을 만들고 평가셋으로 평가하시오.
    <조건> X변수 : reviews 칼럼, y변수 : label 칼럼 
"""

import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer # DTM
from sklearn.naive_bayes import MultinomialNB # nb model
from sklearn.metrics import accuracy_score, confusion_matrix # 평가 도구 

# 1. dataset 준비 
path = r'C:\ITWILL\3_TextMining\data'
data = pd.read_csv(path + '/movie_reviews.csv')
print(data.info())
'''
 0   reviews  1492 non-null   object : X변수 
 1   title    1492 non-null   object
 2   label    1492 non-null   int64  : y변수 
''' 
    

# 2. X, y변수 준비 
texts = data.reviews
target = data.label

# 원문 -> dtm 벡터화
dtm = TfidfVectorizer().fit_transform(texts)
dtm_arr = dtm.toarray()


# 3. 훈련셋/평가셋 분류(80% vs 20%) 
from sklearn.model_selection import train_test_split 

X_train, X_test, y_train, y_test = train_test_split(dtm_arr, target, test_size=0.2)

# 4. model 학습 : 훈련셋 
model = MultinomialNB()
model. fit(X = X_train, y = y_train)

# 5. model 평가 : 평가셋 
y_pred = model.predict(X = X_test) # 예측치 
y_true = y_test # 관측치(정답)


# 1) 혼동행렬 
con_mat = confusion_matrix(y_true, y_pred)
print(con_mat)
'''
[[113  36]
 [ 19 131]]
'''


# 2) 분류정확도 
acc = accuracy_score(y_true, y_pred)
print('분류정확도 =', acc)
# 분류정확도 = 0.8160535117056856

