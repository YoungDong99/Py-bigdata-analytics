"""
2.nltk.tokenize: 일반 텍스트를 대상으로 토큰을 생성하는 기능 
 - 일반 텍스트 : 문장 토큰화, 단어 토큰화, 정규 표현식을 사용한 토큰화 수행 
"""

import pandas as pd # csv file

# 단계1 : token 생성기 및 데이터 다운로드 
from nltk.tokenize import word_tokenize # 단어 token
from nltk.tokenize import sent_tokenize # 문장 token
from nltk.tokenize import RegexpTokenizer # 정규표현식 token 


# token 생성 데이터 다운로드 
import nltk 
nltk.download('punkt') # punkt data download

 
## 단계2 : csv file 가져오기  
path = r'C:\ITWILL\3_TextMining/data'
data = pd.read_csv(path + '/movies_metadata.csv')
print(data.info())
'''
RangeIndex: 45466 entries, 0 to 45465
Data columns (total 24 columns)
'''

## 단계3 : 필요한 변수 선택 
df = data[['title', 'overview']] # 복수 칼럼 선택 : 중첩list 
df.shape # (45466, 2) : (행, 열)


# overview 칼럼 선택 & 리스트 변환  
overview = df['overview'].tolist() # Series 객체(column) -> list변환 
type(overview) #  list
len(overview) # 45466


## 단계4 : token 생성  
words = [word_tokenize(row) for row in overview[:2] ] 
print(words)

words[0]


# 4.2 문단 -> 문장 token
sentences = [sent_tokenize(row) for row in overview[:2] ] 
print(sentences)

# 4.3 정규표현식을 사용한 토큰화  
text = "Hello, world! This is an example sentence." # 텍스트 데이터

tokenizer = RegexpTokenizer(r'\w+') # 정규표현식 패턴을 사용한 토큰화  
# 패턴 : 알파벳과 숫자로 이루어진 연속된 문자열 토큰 
tokens = tokenizer.tokenize(text) # 토큰 생성 
tokens # ['Hello', 'world', 'This', 'is', 'an', 'example', 'sentence']



