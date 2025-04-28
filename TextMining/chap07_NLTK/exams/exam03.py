"""
문3) movies_metadata.csv 파일의 'overview' 칼럼을 대상으로 단계3에서 '단어 토큰화'한 words를 대상으로 
     단계4에서 '품사 태깅'하고, 단계5에서 '필요한 품사'만 선택하여 단어를 선정하시오.
"""
import pandas as pd

# 단계1 : csv file load 
review_data = pd.read_csv(r'C:\ITWILL\3_TextMining\data\movies_metadata.csv')

# overview 칼럼 선택 
overview = review_data['overview'].to_list()
overview # 영문 텍스트 



# 단계2 : 품사 태깅 생성기 및 데이터 다운로드 
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

import nltk
nltk.download('punkt') # 토큰 생성에 필요한 데이터
nltk.download('averaged_perceptron_tagger') # 품사 태깅 관련 데이터 


# 단계3 : 단어 토큰화 : 예외처리 
words = []

for row in overview :
    try :
        words.extend(word_tokenize(row)) # 단어 토큰화 과정에서 예외발생 
    except :
        pass

len(words)


# 단계4 : 품사 태깅 
pos_words = pos_tag(words)


# 단계5 : 단어 선택 : 명사(), 동사(기본형, 3인칭), 형용사 선택(기본형, 3인칭)
final_words = [] 

for word, wclass in pos_words :
    if wclass == 'NN' or wclass == 'NNS' \
            or wclass == 'VB' or wclass == 'VBP' or wclass == 'JJ' :
                final_words.append(word)
    
    
len(final_words) # 870,667개    
final_words   











