"""
Naive Bayes 분류기
"""

from sklearn.naive_bayes import MultinomialNB # Naive Bayes model
from sklearn.metrics import accuracy_score, confusion_matrix # 평가 
from sklearn.preprocessing import LabelEncoder # 10진수 인코딩 
import pickle

# 1. file save
path = r"C:\ITWILL\3_TextMining\data"
file = open(path + "/spam_train_test.pkl", mode='rb')
spam_train_test = pickle.load(file=file)
file.close()



X_train, X_test, y_train, y_test = spam_train_test
X_train.shape  # (3901, 5000)
X_test.shape   # (1673, 5000)

y_train.shape  # (3901,)
y_test.shape  # (1673,)


#######################
### 2. NB model
#######################

'''
model = MultinomialNB()
model.fit(X = x_train, y = y_train)
'''

# model 학습 : 휸련셋
model = MultinomialNB().fit(X = X_train, y = y_train)  
dir(model)  # y = predict(X)

# model 평가 
y_pred = model.predict(X = X_test) # 예측치 
y_true = y_test # 정답 y_true : 실제값이라는 의미(코드 가독성을 위해)
'''
predict : 모델이 학습을 마친 후, 새로운 데이터가 들어왔을 때 결과(예측값)를 알려주는 함수
'''

acc = accuracy_score(y_true, y_pred)
print('분류정확도 =', acc) # lebel 균형 
# 분류정확도 = 0.9659294680215182(예측 정확도 퍼센트)


con_mat = confusion_matrix(y_true, y_pred)  # 성적표 역할
print(con_mat)
'''
실제값 \ 예측값   ham(N)  spam(P)
ham(N)     [[1457(TN)    2(FP)]   1457 / 1459 = 0.9986291980808774
spam(P)     [  55(FN)  159(TP)]]   159 / 214 =  0.7429906542056075
'''

#정확률(Precision) = TP / (TP + FP) : 예측치 
#재현율(Recall) = TP / (TP + FN) : 관측치 

Precision = 159 / (159 + 2) # 0.9875776397515528 (정확률)
Recall = 159 / (159 + 55) # 0.7429906542056075 (재현율)

'''
정확률 : 스팸이라고 예측한 것 중에 실제 스팸은 얼마나 되는가?
재현율 : 실제 스팸중에 모델이 얼마나 많이 잡아냈는가?
'''


# lebel 불균형
F1_score =  2 * ((Precision * Recall) / (Precision + Recall))
print(F1_score) # 0.848

'''
F1 점수 : Precision과 Recall을 모두 고려해서 균형 있게 모델을 평가하기 위한 방법
'''









