"""
numpy & pandas 응용 : 문서단어 행렬(DTM) 만들기 
"""

'''
1.원문(doc)
대한민국은 나의 조국입니다. 
나는 홍길동 입니다.
        
2.문서단어행렬(DTM)
   나  대한민국 조국 홍길동
1  1       1      1    0
2  1       0      0    1 


3.단어문서행렬(TDM)
           1       2 
나         1       1    
대한민국   1       0     
조국       1       0   
홍길동     0       1    
'''


# 원문 텍스트 
"""
대한민국은 나의 조국입니다. 
나는 홍길동 입니다.
"""


# 형태소 분석 후 문장 
texts = """대한민국 나 조국
나 홍길동"""



# 1. 문장 만들기
sent_nouns = [] 

for sent in texts.split(sep='\n') :
    sent_nouns.append(sent.split()) # 중첩list 

print(sent_nouns)
# [['대한민국', '나', '조국'], ['나', '홍길동']]



# 2. 유일한 단어집 만들기  

# 1) 단어집 만들기 : 단어 수집  
nouns = []
for sent in sent_nouns :
    nouns.extend(sent) # 단일 list 

print(nouns)  # ['대한민국', '나', '조국', '나', '홍길동']

# 2) 유일한 단어 
unique_nouns = list(set(nouns))
unique_nouns 

# 3) 단어 정렬 
unique_nouns = sorted(unique_nouns) 
unique_nouns 


# 3. 영(zeros) 행렬 만들기 
import numpy as np 

zeros = np.zeros(shape = (2, 4))  # (2행:문서개수, 4열 : 단어개수)
print(zeros)
'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''

# 4. 문서단어행렬(DTM) 만들기 
import pandas as pd 

dtm = pd.DataFrame(zeros, columns = unique_nouns) # 열이름=단어 
print(dtm)
'''
    나  대한민국  조국  홍길동   : 단어(Term)
0  0.0   0.0     0.0    0.0
1  0.0   0.0     0.0    0.0
'''

for idx, nouns in enumerate(sent_nouns) :
    for noun in nouns :
        dtm.loc[idx, noun] += 1   # dtm.loc[행, 열]
'''
첫 번째 반복에 (idx, nouns) = (0, ['대한민국','나','조국'])
두 번째 반복에 (idx, nouns) = (1, ['나','홍길동'])
'''

print(dtm)
'''
   나    대한민국   조국  홍길동
0  1.0   1.0      1.0   0.0
1  1.0   0.0      0.0   1.0
'''

# 각 단어의 총 출현빈도수
dtm.sum(axis=0) # 행축 합계
'''
나       2.0
대한민국    1.0
조국      1.0
홍길동     1.0
'''

