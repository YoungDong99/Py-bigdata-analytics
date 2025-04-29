"""
문3) 주어진 파일의 자료를 이용하여 다음과 같이 word2vec 모델을
     생성하고 키워드를 입력하여 가장 유사한 단어 3개를 출력하는 
     함수를 정의하시오.   

 <조건1> 사용할 칼럼 : review 
 <조건2> word2vec 모델 파라미터 : window=5, min_count=1, sg=1  
 <조건3> 검색 키워드 : action, people, society 
"""

from gensim.models import Word2Vec # model 
from nltk.tokenize import word_tokenize # sentence -> work token
import pandas as pd # csv file


# 1. dataset load 
path = r'C:\ITWILL\3_TextMining\data'
data = pd.read_csv(path + '/movie_reviews.csv')
print(data.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1492 entries, 0 to 1491
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   reviews  1492 non-null   object : 영화후기 
 1   title    1492 non-null   object : 영화제목  
 2   label    1492 non-null   int64  : 긍정/부정 
'''


# 2. token 생성 

# 1) reviews 단어 벡터 생성 
reviews = data['reviews'].tolist()
print(len(reviews))


# 2) 문장 -> 단어
sentences = [word_tokenize(row) for row in reviews]


# 3) model 생성
model = Word2Vec(sentences=sentences, window=5, min_count=1, sg=1 )

dir(model)
dir(model.wv)



# 3. 함수 구현 
def word_search(word) :
    global model
    
    word_search = model.wv.most_similar([word])
    
    top3 = word_search[:3]
    print(top3)



# 함수 호출 : 검색 단어 : action, people, society   
word_search(input('검색 단어 입력 : ')) 













