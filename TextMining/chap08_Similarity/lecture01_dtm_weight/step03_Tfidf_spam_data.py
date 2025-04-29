"""
스팸 메시지 -> 문서단어행렬(DTM) 만들기 

1. csv file 가져오기 
2. texts, target 전처리 
3. max features
4. DTM(TFiDF 가중치)
5. train/test split
# 6. file save
"""

import pandas as pd # csv file 
from sklearn.feature_extraction.text import TfidfVectorizer # DTM(TFiDF 가중치)
import numpy as np # 다차원배열


# 1. csv file 가져오기  
path = r"C:\ITWILL\3_TextMining\data"
spam_data = pd.read_csv(path + '/spam_data.csv', header=None, encoding='utf-8')
# header = None : 제목열 없음

spam_data.info()
'''
RangeIndex: 5574 entries, 0 to 5573
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       5574 non-null   object : spam or ham
 1   1       5574 non-null   object : 원문(메시지)
'''


# 2) target, texts 전처리 : 공백, 특수문자, 숫자
target = spam_data[0]
#target = np.array(target)

texts = spam_data[1]

print('전처리 전')
print(texts)


# << texts 전처리 함수 >> 
import string # texts 전처리
def text_prepro(texts): # 문단(sentences)
    # Lower case : 문단 -> 문장 -> 영문소문자 변경  
    texts = [x.lower() for x in texts]
    # Remove punctuation : 문단 -> 문장 -> 음절 -> 필터링 -> 문장  
    texts = [''.join(ch for ch in st if ch not in string.punctuation) for st in texts]
    # Remove numbers : 문단 -> 문장 -> 음절 -> 필터링 -> 문장 
    texts = [''.join(ch for ch in st if ch not in string.digits) for st in texts]
    # Trim extra whitespace : 문단 -> 문장 -> 공백 제거 
    texts = [' '.join(x.split()) for x in texts]
    return texts

texts = text_prepro(texts)
print(texts)


# 3. max features : 문서단어행렬(DTM) 차원 결정 
fit = TfidfVectorizer().fit(texts) # 단어 생성기 
voca = fit.vocabulary_
len(voca) # 8603

max_features = 5000 # 전체 단어수 


# 4. DTM : max features 지정 
tfidf = TfidfVectorizer(max_features = max_features, stop_words='english')
'''
max_features : 사용할 단어 개수
stop_words : 불용어 제거
'''


# 문서단어 행렬(DTM)  
dtm = tfidf.fit_transform(texts)

# numpy array 변환 
dtm_arr = dtm.toarray()
dtm_arr.shape # (5574, 5000) : (문서개수, 단어개수)
dtm_arr


# 5. train/test split : 70% vs 30%
from sklearn.model_selection import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(
    dtm_arr, target, test_size=0.3)
'''
x변수 : dtm
y변수 : target
'''
x_train.shape # (3901, 5000)
x_test.shape # (1673, 5000)

y_train.shape # (3901,)
y_test.shape # (1673,)

type(x_test) # numpy.ndarray

# 6. file save 
import pickle   # numpy 객체를 그대로 저장

spam_train_test = [x_train, x_test, y_train, y_test]

file = open(path + "/spam_train_test.pkl", mode='wb')
pickle.dump(obj=spam_train_test, file=file)
file.close()












