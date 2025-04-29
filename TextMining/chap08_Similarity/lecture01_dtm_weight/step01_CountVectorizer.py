"""
CountVectorizer  
  1. 단어 생성기(word tokenizer) : 단어 사전(word dictionary) 
  2. 문서단어행렬(DTM) : 해당 문서에서 출현한 단어의 빈도수(TF)로 가중치 제공  
     - TF(Term Frequence) 가중치 : 단어출현빈도수  
"""

import string # texts 전처리 
from sklearn.feature_extraction.text import CountVectorizer 


# 1. texts 전처리
texts = ["우리나라    대한민국, 우리나라 만세", "비아그라 500GRAM 정력 최고!",
         "나는 대한민국 우리나라 사람", "보험료 15000원에 평생 보장 마감 임박",
         "나는 홍길동"]


# texts 전처리 함수 
def text_prepro(texts):
    # Lower case 
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers 
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts


final_texts = text_prepro(texts)
print(final_texts)
'''
['우리나라 대한민국 우리나라 만세', '비아그라 gram 정력 최고', 
 '나는 대한민국 우리나라 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''

# 2.texts 전처리 파일 저장  
path = r'C:\ITWILL\3_TextMining\data'
file = open(file=path + '/final_texts.txt', mode='w')   # 파일 생성
for row in final_texts :
    file.write(row)
    file.write('\n')
    
file.close() # 객체 닫기 



# 3. 단어 생성기 
count = CountVectorizer() # 단어 생성기 (객체 생성)
fit = count.fit(final_texts) # 원문 반영
voca = fit.vocabulary_ # 단어 사전 
voca # {'단어': 고유번호}


# 4. 문서단어행렬(DTM)  
DTM = count.fit_transform(final_texts)  # 원문 반영 & 변형(dtm) 
print(DTM)
'''
  (행,열)  가중치(TF)
  (0, 9)	2     -> 문자1, 우리나라(9) -> 2회 출현
  (0, 2)	1
  (0, 4)	1
  (1, 7)	1
  (1, 0)	1
  (1, 12)	1
  (1, 13)	1
  (2, 9)	1     -> 문장3, 우리나라(9) -> 1번 출현
  (2, 2)	1
  ...
'''

dir(DTM)  # toarray : 다차원 배열 변환
DTM_arr = DTM.toarray()

print(DTM_arr)
'''
[[0 0 1 0 1 0 0 0 0 2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0]
 [0 1 1 0 0 0 0 0 1 1 0 0 0 0 0 0]
 [0 0 0 1 0 1 1 0 0 0 1 1 0 0 1 0]
 [0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1]]
'''


DTM_arr.shape  # (5, 16)



