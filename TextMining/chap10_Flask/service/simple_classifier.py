"""
간단한 문서 분류기(simple texts classifier) 
"""

import pandas as pd # DataFrame 
from sklearn.feature_extraction.text import TfidfVectorizer # DTM(희소행렬)
from sklearn.naive_bayes import MultinomialNB # nb model
from sklearn.metrics import confusion_matrix, accuracy_score # 평가 


# dataset 만들기 
target = [1,0,1,0,1,0,1,0,1,0] # list 
texts = [
    "I don't like rainy days.",
    "I love spending time with my family.",
    "She isn't feeling well today.",
    "She is an incredibly talented musician.",
    "They haven't finished their homework yet.",
    "They have accomplished so much in their careers.",
    "He can't stand the cold weather.",
    "He always has a positive attitude.",
    "We didn't enjoy the movie at all.",
    "We had a fantastic time on our vacation." ]

frame = pd.DataFrame({'target' : target, 'texts' : texts})

# 훈련용 데이터셋(X, y)  
#print(frame)
'''
   target                                             texts
0       1                          I don't like rainy days.
1       0              I love spending time with my family.
2       1                     She isn't feeling well today.
3       0           She is an incredibly talented musician.
4       1         They haven't finished their homework yet.
5       0  They have accomplished so much in their careers.
6       1                  He can't stand the cold weather.
7       0                He always has a positive attitude.
8       1                 We didn't enjoy the movie at all.
9       0          We had a fantastic time on our vacation.
'''

#frame.info()
'''
0   target  10 non-null     int64  : y변수 
1   texts   10 non-null     object : X변수 
'''

# 1. 훈련용 X, y변수 

# 1) y변수 
y = frame.target   
y # 0 or 1 

# 2) X변수 
texts = frame.texts 

tfidf = TfidfVectorizer()
DTM = tfidf.fit_transform(texts) # 문서 반영 
X = DTM.toarray()
X.shape # (10, 53)


# 2. 학습 model 만들기 
nb = MultinomialNB()
model = nb.fit(X=X, y=y)


# 3. 텍스트 원문 분류 함수   
def classifier(texts_test) :
    global model, tfidf # 학습모델
    
    DTM_test = tfidf.transform([texts_test]) 
    X_test = DTM_test.toarray()
    
    y_pred = model.predict(X = X_test) # y예측 
    y_pred_result = '부정문 입니다.'if y_pred == 1 else '긍정문 입니다.'
    return y_pred_result

# 함수 호출 
'''
y_pred_result = classifier("I don't like chocolate ice cream.")
print(y_pred_result) # 부정문 입니다.
'''

