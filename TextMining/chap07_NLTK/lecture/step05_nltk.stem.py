"""
4.nltk.stem: 단어의 표제어 추출(lemmatization)과 어간 추출(stemming)을 통해서 단어의표준화를 제공한다. 

1) 표제어(lemmatization)는 단어의 사전적인 기본 형태를 의미한다. 따라서 표제어 추출은  
     단어의 다양한 형태를 하나의 표준 형태로 통합하여 단어의 일관성과 정확성을 향상

2) 어간(stem)은 단어의 핵심 의미를 담고 있는 부분으로 단어에서 어미, 접미사 등을 제거하고 남은 기본형

예) "running", "runs", "ran"과 같은 단어들은 모두 동일한 동사 "run"의 다른 형태 (표제어)
"""


import nltk
from nltk.stem import WordNetLemmatizer # 표제어 추출과 어간 추출
from nltk.tokenize import word_tokenize # 단어 토큰 생성 
nltk.download('punkt') # 토큰 생성에 필요한 데이터 
nltk.download('wordnet') # 단어의 의미와 관계(동의어, 반의어 등)에 필요한 데이터 


# WordNetLemmatizer 객체 생성
lemmatizer = WordNetLemmatizer()

dir(lemmatizer) # lemmatize



# 단어 표준화 함수 정의
def word_lemmatization(text):
    # 문장을 단어로 토큰화
    words = word_tokenize(text)    
    
    # 각 단어의 표준화 수행 : 동사 어간 처리 
    #lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]
    
    lemmatized_words = [lemmatizer.lemmatize(word, pos='v') if word != 'am' else word for word in words]
    
    '''
    pos 파라미터 : 품사(part-of-speech) 태그 지정
     'a': 형용사 (Adjective)
     'n': 명사 (Noun) : 기본값 
     'v': 동사 (Verb)
     'r': 부사 (Adverb)
    '''
        
    return ' '.join(lemmatized_words) # 표준화된 단어 반환

# 예시 문장
sentence = "I am running and eating food"

# 단어 표준화 적용
standardized_sentence = word_lemmatization(sentence)


print(standardized_sentence)  # I be run and eat food
# I am run and eat food

