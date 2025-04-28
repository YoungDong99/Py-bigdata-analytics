"""
1. nltk.corpus : 말뭉치(corpus)는 말+뭉치의 합성어로 언어 데이터를 모아놓은 대규모 텍스트 데이터 모음 
주로 언어학 연구와 자연어 처리(NLP) 작업에서 사용되며, 언어의 구조, 의미, 사용 방식 등을 분석하는 데 활용한다. 

정의: 어떤 언어의 문장, 단어, 대화, 문서 등을 체계적으로 모아 놓은 대규모 텍스트 자료 모음
목적: 언어 연구, 정보검색 시스템 개발, 자연어처리 모델의 학습 및 평가용 데이터로 사용 

※ 주의 : 말뭉치 자료는 import 과정에 제공되지 않고 download 명령으로 다운로드 받아야 사용할 수 있다.
"""
 
import nltk # anaconda 제공 패키지 
import nltk.corpus # corpus 모듈 


# 제공되는 주요 말뭉치 
'''
brown : 브라운대학교 
gutenberg : 구텐베르크 전자책(eBooks) 
movie_reviews : 영화 리뷰 
stopwords : 불용어 
words : 영어 단어 사전 
'''


### 1. 구텐베르크(Project Gutenberg) 말뭉치 가져오기 

# 단계1 : 구텐베르크 말뭉치 데이터 다운로드  
nltk.download('gutenberg')


# 단계2 : 구텐베르크 말뭉치 객체 가져오기 
from nltk.corpus import gutenberg # 객체 


dir(gutenberg) 
'''
fileids() : 말뭉치에서 전체 문서파일 가져오기  
raw() : 문서 파일에서 원문 가져오기  
paras() : 문서 파일에서 문단 가져오기(단어 단위)
sents() : 문서 파일에서 문장 가져오기(단어 단위) 
words() : 문서 파일에서 단어 가져오기 
'''


# 단계3 : 말뭉치에 문서 파일 가져오기  
fileids = gutenberg.fileids()
print(fileids) # *.txt 파일 
len(fileids) # 18개 문서파일  

files = fileids[:5] # 5개의 문서파일 출력
print(files)  # ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt']


# 단계4 : 문서파일에서 원문 가져오기
texts = gutenberg.raw(files) # 5개 문서파일에서 원문 가져오기  
print(texts)
type(texts) # str : 문자열 
len(texts) # 6,397,092개 문자 


# 토큰생성을 데이터 다운로드
nltk.download('punkt')
nltk.download('punkt_tab')


# 단계5 : 문서파일에서 문단 가져오기(단어 단위)   
paras = gutenberg.paras(files) # 5개 문서파일에서 문단 가져오기

print(paras) # 3중list : 문단 > 문장n > 단어n 

len(paras) # 30,157개 문단 : 5개 문서파일의 문단 길이 


# 문단n -> 문단 -> 문장n -> 문장 
sents = [sent for para in paras for sent in para]
len(sents) # 47,039개 문장 

sents[0] # 첫번째 문장 
# ['[', 'Emma', 'by', 'Jane', 'Austen', '1816', ']']


# 단계6 : 문서파일에서 문장 가져오기(단어 단위)   
sents = gutenberg.sents(files)

print(sents)  # 2중list : 문장n > 단어n

len(sents) # 47,039 : 5개 문서파일에서 가져온 문장길이(문장 추출 결과와 동일)


  

# 단계7 : 문서파일에서 단어 가져오기
words = gutenberg.words(files)

print(words) # 단일list : 단어n

len(words) # 1,451,182  : 5개 문서파일에서 가져온 단어길이




### 2. 영어 단어 말뭉치 로드 : 영어 단어장

# 단계1 : 단어 말뭉치 가져오기 
from nltk.corpus import words

dir(words)


# 단계2 : 단어 말뭉치 데이터 다운로드  
nltk.download('words')


# 단계3 : 말뭉치에서 단어 가져오기 
eng_words = words.words()
print(eng_words[:10])  # 처음 10개의 단어 출력
print(eng_words[-10:]) # 마지막 10개의 단어 출력
len(eng_words) # 236736
   

    

### 3. 불용어(stopwords) 말뭉치 로드

# 단계1 : 단어 말뭉치 가져오기 
from nltk.corpus import stopwords

# 단계2 : 단어 말뭉치 데이터 다운로드  
nltk.download('stopwords')


# 단계3 : 말뭉치에서 불용어 가져오기  
stopwords = stopwords.words('english')
print(stopwords) # 인칭대명사, 접속사(and), 부사(about), 형용사(each), 조동사(should)
len(stopwords) # 198
 

