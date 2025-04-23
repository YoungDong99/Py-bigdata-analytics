"""
Okt(Open Korean Text) : 한글문서를 대상으로 형태소 분석 및 품사 태깅 기능을 제공(python 구현)
"""

from konlpy.tag import Okt # 형태소 분석기
from collections import Counter # TopN 단어 선택

# Okt 형태소 분석기 생성
okt = Okt() # 객체 생성 
dir(okt)

'''
jki       : 구 단위로 구문을 분리하여 반환
morphs    : 형태소만 추출
normalize : 문자열 일반화(반복문자 줄이기, 맞춤법 조정, 특수문자 제거)
nouns     : 명사
phrases   : 구 추출(2개 이상 절)
pos       : 형태소와 품사를 함께 태깅하여 반환
tagset    : 사용 가능한 품사 태그 목록 확인
'''

# 문단(Paragraph) : 3개 문장 
para  = "나는 홍길동 임니다. age는 23세 입니다. 나는 대한민국 사람입니다."


# 1. okt.morphs : 형태소 추출 
okt.morphs(para) # list 


# 2. okt.normalize : 문단을 okt에 적합한 문자열로 변환(일반화) 
text_normal = okt.normalize(para) 
print(text_normal)



# 3. okt.nouns : 명사 추출 : 중복 명사 추출, 서수(x), 복합어 분해(x) 
okt.nouns(text_normal) 
# ['나', '홍길동', '나이', '세', '나', '대한민국', '사람', '대한민국', '사랑']


# 문단이 일반화된 문자열인 경우 : 문단에서 명사 추출   
okt.nouns(para)
# ['나', '홍길동', '나이', '세', '나', '대한민국', '사람', '대한민국', '사랑']



# 4. 품사 부착(단어, 품사) 
ex_pos = okt.pos(text_normal)  # (형태소, 품사)
print(ex_pos) 
'''
'Noun' : 명사 
'Josa' : 조사 
'Adjective' : 형용사 
'Punctuation' : 문장부호 
'Alpha' : 영문 
'Verb' : 동사 
'Number' : 숫자 
'''


# 5. 형태소 -> 단어 추출  
nouns = [] # 명사 저장 

for word, wclass in ex_pos :
    if wclass == 'Noun' or wclass == 'Alpha' :
        nouns.append(word)

print(nouns)


# 6. 단어 빈도수(word count)
new_para  = "나는 홍길동 입니다. age는 23세 입니다. 나는 대한민국 사람입니다. 나는 대한민국을 사랑합니다. 우리 모두 사랑합시다."

ex_pos = okt.pos(new_para)

new_nouns = [] # 명사 저장 

for word, wclass in ex_pos :
    if wclass == 'Noun' or wclass == 'Alpha' :
        new_nouns.append(word)

print(new_nouns)


# 단어 빈도수
wc = {}

for word in new_nouns :
    wc[word] = wc.get(word, 0) + 1
    
print(wc)


# 7. TopN 단어 선정
count = Counter(wc)

top3 = count.most_common(3)

print(top3)







