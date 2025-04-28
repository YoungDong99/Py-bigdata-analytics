"""
3.nltk.tag: 품사 태깅(part-of-speech tagging)과 관련된 기능
  - 주어진 문장의 단어에 대해 품사 태그를 할당하는 작업 
"""

# 단계1 : 품사 태깅 생성기 및 데이터 다운로드 
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag



import nltk
#nltk.download('punkt') # 토큰 생성에 필요한 데이터
nltk.download('averaged_perceptron_tagger') # 품사 태깅 관련 데이터 
nltk.download('averaged_perceptron_tagger_eng')

# 텍스트 데이터
text = "John likes to watch movies. He also enjoys playing tennis."

# 단계2 : 단어 토큰화 (공백기준)
words = word_tokenize(text)
print(words)

# 단계3 : 품사 태깅 
pos_words = pos_tag(words)


# 품사 태깅 결과 출력
print(pos_words)
'''
[품사 태깅 관련 품사 유형] 
CC: Coordinating Conjunction (등위 접속사)
CD: Cardinal Number (기수)
DT: Determiner (한정사)
EX: Existential There (존재 형태)
FW: Foreign Word (외래어)
IN: Preposition or Subordinating Conjunction (전치사 또는 종속 접속사)
JJ: Adjective (형용사)
JJR: Adjective, Comparative (비교급 형용사)
JJS: Adjective, Superlative (최상급 형용사)
LS: List Item Marker (목록 항목 표시기)
MD: Modal (법조동사)
NN: Noun, Singular or Mass (명사, 단수형 또는 집합형)
NNS: Noun, Plural (명사, 복수형)
NNP: Proper Noun, Singular (고유 명사, 단수형)
NNPS: Proper Noun, Plural (고유 명사, 복수형)
PDT: Predeterminer (선정관사)
POS: Possessive Ending (소유격 종결어미)
PRP: Personal Pronoun (인칭 대명사)
PRP$: Possessive Pronoun (소유 대명사)
RB: Adverb (부사)
RBR: Adverb, Comparative (부사, 비교급)
RBS: Adverb, Superlative (부사, 최상급)
RP: Particle (조사)
SYM: Symbol (기호)
TO: to (to 전치사)
UH: Interjection (감탄사)
VB: Verb, Base Form (동사, 기본형)
VBD: Verb, Past Tense (동사, 과거형)
VBG: Verb, Gerund or Present Participle (동명사 또는 현재 분사형)
VBN: Verb, Past Participle (동사, 과거 분사형)
VBP: Verb, Non-3rd Person Singular Present (동사, 3인칭 단수형이 아닌 현재형)
VBZ: Verb, 3rd Person Singular Present (동사, 3인칭 단수형 현재형)
WDT: Wh-Determiner (관계 한정사)
WP: Wh-Pronoun (관계 대명사)
WP$: Possessive Wh-Pronoun (관계 대명사, 소유형)
WRB: Wh-Adverb (관계 부사)
''' 

final_words = []

for word, wclass in pos_words :
    if wclass == 'NNP' or wclass == 'NNS' or \
        wclass == 'NN' or wclass == 'VB' or wclass == 'VBZ' :
            final_words.append(word)


len(final_words)
print(final_words)
# ['John', 'likes', 'watch', 'movies', 'enjoys', 'tennis']



