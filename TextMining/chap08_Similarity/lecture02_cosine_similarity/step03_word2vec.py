"""
유사 단어 검색(추천) 

1. word2vec 개요 
  - 중심단어와 주변단어 벡터 간의 연산으로 유사단어 예측
2. word2vec 유형 
  1) CBOW : 주변단어 학습 -> 중심단어 예측 
  2) SKIP-Gram : 중심단어 -> 주변단어 예측 
"""

from gensim.models import Word2Vec # model 
#import nltk
#nltk.download('punkt') # nltk data download
from nltk.tokenize import word_tokenize # 문장 -> 단어 token
from nltk.tokenize import sent_tokenize # 문단 -> 문장 token
import pandas as pd # csv file


'''
https://www.kaggle.com/rounakbanik/the-movies-dataset
movies_metadata.csv : 파일 다운로드 
'''

# 1. dataset load 
path = r'C:\ITWILL\3_TextMining\data'
data = pd.read_csv(path + '/movies_metadata.csv')
print(data.info())
'''
RangeIndex: 45466 entries, 0 to 45465
Data columns (total 24 columns):
'''

# 2. 변수 선택 & 전처리 
df = data[['title', 'overview']]
dir(df)
'''
isna : 결측치 확인
isnull : 결측치 확인
dropna() : 결측치 행 제거
'''

df.isna().sum()  # 컬럼 단위 결측치 개수
'''
title         6
overview    954
'''

# 실제 결측치 행 확인
df[df['overview'].isna()].head()


df = df.dropna(axis = 0) # 결측치 제거 
df.isna().sum()
'''
title       0
overview    0
'''

df.shape  # (44506, 2)


# 3. token 생성 
# 1) overview 단어 벡터 생성 
overview = df['overview'].tolist() # column -> list변환 
len(overview)  # 44506
print(overview)


# 2) 문장 -> 단어
result = [word_tokenize(row) for row in overview ] 
len(result)  # 44506
print(result[:100])  # 이중 list


# 4. word2vec 
model = Word2Vec(sentences=result, window=5, min_count=1, sg=1) 
'''
sentences : 문장 단어
window : 1회 학습 단어 개수
min_count : 최소 출현 빈도수
sg : 1 = SKIP-Gram, 0 = CBOW
'''

# 5. 유사 단어 검색 
word_search = model.wv.most_similar(['husband']) 

top5 = word_search[:5]
print(top5)
'''
[
 ('boyfriend', 0.8463664650917053), 
 ('lover', 0.8378469347953796), 
 ('fiancé', 0.8202046751976013),
 ('mother', 0.7916310429573059), 
 ('fiance', 0.7847967147827148)
]
'''


# 함수 구현
def word_search(word) :
    global model
    
    word_search = model.wv.most_similar([word]) 
    
    top5 = word_search[:5]
    print(top5)


word_search(input('검색어 입력 : '))










