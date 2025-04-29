"""
유사 문서 찾기  

<작업절차>
 1. 자연어 -> 문서단어행렬(DTM) 변경 : 벡터화(Vertorize)
 2. 코사인 유사도 적용     
"""

# 문서단어행렬(DTM)
from sklearn.feature_extraction.text import TfidfVectorizer # 벡터화
# 코사인 유사도 
from sklearn.metrics.pairwise import cosine_similarity # 유사도 계산


# 문장(자연어)
sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
]

print(sentences)
len(sentences) # 3


# 1. 대상 문서(자연어) -> DTM(문서단어행렬:희소행렬) 변경
obj = TfidfVectorizer() # 1) 단어생성기 


# 2) 생성된 단어 확인 
fit = obj.fit(sentences)
voca = fit.vocabulary_ # 단어집 
voca  # {'단어': 고유숫자} : 오름차순으로 고유숫자 

# 3) 문서단어행렬(DTM)
sents_dtm = obj.fit_transform(sentences)


# 4) scipy -> numpy array
sents_dtm_arr = sents_dtm.toarray()
print(sents_dtm_arr)

sents_dtm_arr.shape # (3, 31)


# 2. 코사인 유사도 적용 

# 1) 검색 쿼리(search query)
query = ['green plant in his study'] # 검색 문장(1) vs 대상 문장(3) 

# 2) 희소행렬(DTM)
query_dtm = obj.transform(query) # 함수 주의 : 검색 문장 -> dtm 
dir(obj)
'''
fit() : 단어 사전
fit_transform() : 반영 & 변형(dtm)
transform() : 현재 원문 반영X dtm으로만 변형
'''

# 3) scipy -> numpy array
query_dtm_arr = query_dtm.toarray()
query_dtm_arr
query_dtm_arr.shape # (1, 31)


# 4) 코사인 유사도 계산 : 0 ~ 1
sim = cosine_similarity(query_dtm_arr, sents_dtm_arr) # (질문, 원문)
print(sim)  # [[0.25069697, 0.74327606, 0.24964024]]


# 5) 모양 변경 
sim = sim.reshape(3)  # 단일리스트로 변경
type(sim)  # numpy.ndarray 넘파이 다차원배열


# 6) 내림차순 정렬 : index 정렬 
sim_idx = sim.argsort()[::-1]  # [start:stop:step]d
# argsort() : 내용을 기준으로 index 정렬
sim_idx  # [1, 0, 2]



for idx in sim_idx :
    print(f'유사도 = {sim[idx]}, 문서={sentences[idx]}')





