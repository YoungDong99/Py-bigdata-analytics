"""
간단한 문서 분류기(simple texts classifier) 
"""

import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer # DTM : 벡터화
from sklearn.naive_bayes import MultinomialNB # Naive Bayes model
from sklearn.metrics import confusion_matrix, accuracy_score # model 평가


# 1. dataset 만들기 
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
    "We had a fantastic time on our vacation." ]  # 원문

target = [1,0,1,0,1,0,1,0,1,0]  # 정답(1=부정문, 0=긍정문)


train_set = pd.DataFrame({'target' : target, 'texts' : texts}) 

# 훈련용 데이터셋  
print(train_set)
'''
   target (y)                                        texts (x)
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


# 평가용 데이터셋    
test_texts = ["I don't like chocolate ice cream.",
              "She isn't going to the party tonight.",
              "I love spending time with my family.",
              "They didn't finish their homework on time."] # 원문

test_target= [1,1,0,1] # 정답 

test_set = pd.DataFrame({'target' : test_target, 'texts' : test_texts}) 


# 평가용 데이터셋  
print(test_set)
'''
   target                                       texts
0       1           I don't like chocolate ice cream.
1       1       She isn't going to the party tonight.
2       0        I love spending time with my family.
3       1  They didn't finish their homework on time.
'''


# 2. 훈련용 X, y변수 만들기  

# 1) 훈련용 y변수 
y_train  = train_set.target   # 정답(긍정 or 부정)
print(y_train)


# 2) 훈련용 X변수 
texts = train_set.texts   # 원문
print(texts)


# DTM 생성 
tfidf = TfidfVectorizer()

train_dtm = tfidf.fit_transform(texts)  # 원문 반영 & 변형
X_train = train_dtm.toarray()
print(X_train)
## 수치화 과정


# 3. model 학습 : 훈련셋 이용
model = MultinomialNB()  # 빈 model 생성
model.fit(X_train, y_train)  # 훈련셋 X, y 반영 -> model 훈련


# 4. model 평가 : 평가셋 이용

# 1) 평가용 y변수
y_test = test_set.target # 평가셋 정답 


# 2) 평가용 X변수
test_texts = test_set.texts

# 훈련할 때 만든 방식 그대로 새로운 문장을 숫자로 바꿔줌 (fit 다시 사용X)
dtm_test = tfidf.transform(test_texts) # 함수명 주의
X_test = dtm_test.toarray()
print(X_test)


# 3) y예측치 
y_pred = model.predict(X = X_test)
print(y_pred)  # [1 1 0 1]


# 평가 도구 : 혼동행렬(confusion_matrix)
con_mat = confusion_matrix(y_test, y_pred)  # (평가셋정답, 예측치)
print(con_mat)
'''
    0 1
0 [[1 0]    - 긍정문 1개
1  [0 3]]   - 부정문 3개
'''


# 평가 도구 : 분류정확도(accuracy_score)
acc = accuracy_score(y_test, y_pred)
print(acc)  # 1.0   : 100% 예측



