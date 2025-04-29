"""
TfidfVectorizer  
  1. 단어 생성기(word tokenizer) : 단어 사전(word dictionary) 
  2. 문서단어행렬(DTM) : 해당 문서에서 출현한 단어의 출현 비율로 가중치 제공 
    - TFiDF(Term Frequence inver Document Frequence) 가중치 = TF x iDF 
"""

from sklearn.feature_extraction.text import TfidfVectorizer # 단어 생성기

# 테스트 문장 
sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
]

print(sentences)


# 1. 단어 생성기
tfidf = TfidfVectorizer() # 생성자 


# 2. 단어 사전 
fit = tfidf.fit(sentences) # 문장 적용 
voca = fit.vocabulary_ 
voca
'''
vocabulary_ : 학습 후 생성되는 속성임을 뜻하는 Sklearn의 규칙

tfidf.fit(sentences) : 문장에서 단어들을 뽑아 사전을 만들고 내부 변수에 저장
-> 출력하려면 fit 이후 vocabulary_ 직접 호출해야함
'''

# 3. 문서단어행렬(DTM)
dtm = tfidf.fit_transform(sentences) # 문서 반영 & 변형(dtm)
print(dtm)
'''
 (doc,term)   가중치(weight) 
  (0, 3)	0.2205828828763741 -> 
  (0, 16)	0.2205828828763741
  (0, 25)	0.2205828828763741
  (0, 17)	0.2205828828763741
  (0, 10)	0.2205828828763741
  (0, 1)	0.2205828828763741
  (0, 30)	0.2205828828763741
  (0, 23)	0.1677589680512606
  (0, 24)	0.4411657657527482 -> 문장1, 'the'
  
  (1, 6)	0.4555241832708015 -> 문장2, 'has'  (?) 
'''
  

# scipy -> numpy 희소행렬 변경 
dtm_arr = dtm.toarray()

print(dtm_arr)


###############################################
### max_features 적용 (전체가 아닌 일부만 적용)
###############################################

print('전체 단어수 =', len(voca)) # 전체 단어수 = 31


# new 단어생성기 : 단어 20개만 적용
new_tfidf = TfidfVectorizer(max_features = 20)


# 문서단어행렬(DTM)
DTM2 = new_tfidf.fit_transform(sentences)
print(DTM2)
'''
  (0, 14)	0.4411657657527482
  (0, 5)	0.26055960805891015
  (0, 11)	0.2205828828763741
  (0, 2)	0.2205828828763741
  (0, 15)	0.2205828828763741
  (0, 9)	0.1677589680512606
  (0, 24)	0.4411657657527482
  (0, 23)	0.1677589680512606
  (0, 30)	0.2205828828763741
  (0, 1)	0.2205828828763741
  (0, 10)	0.2205828828763741
  (0, 17)	0.2205828828763741
  (0, 25)	0.2205828828763741
  (0, 16)	0.2205828828763741
  (0, 3)	0.2205828828763741
'''

# scipy -> numpy 희소행렬 변경 
DTM2_arr = DTM2.toarray()


print(DTM2_arr)
DTM2_arr.shape # (3, 20)















