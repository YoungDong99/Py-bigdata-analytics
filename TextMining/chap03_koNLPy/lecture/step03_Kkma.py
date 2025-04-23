"""
꼬꼬마(Kkma) :  서울대학교 연구실에서 개발한 형태소 분석기, 비교적 정확한 분석 결과를 제공(java구현)

문단에서 문장단위로 추출해주는 장점
"""

from konlpy.tag import Kkma

# Kkma 형태소 분석기 생성
kkma = Kkma() # 객체 생성 
dir(kkma)
'''
jki       : 구 분리
morphs    : 형태소
nouns     : 명사
pos       : 형태소 + 품사
sentences : 문장 추출
tagset    : 사용 가능한 품사 태그 확인
'''

# 문단(Paragraph) : 4개 문장 
para = "나는 홍길동 입니다. 나이(age)는 23세 입니다. 나는 대한민국 사람입니다.대한민국을 사랑(LOVE) 합니다."


# 1. 문단 -> 문장 추출 
ex_sent = kkma.sentences(para)  
print(ex_sent)
# ['나는 홍길동 입니다.', '나이 (age) 는 23세 입니다.', '나는 대한민국 사람입니다.', '대한민국을 사랑 (LOVE) 합니다.']


# 2. 문단 -> 명사(단어) 추출 
ex_nouns = kkma.nouns(para)  # 중복 명사 제외, 복합어 분해, 서수(숫자)
print(ex_nouns)
'''
['나', '홍길동', '나이', '23', '23세', '세', '대한', '대한민국', '민국', '사람', '사랑']
-> 복합어 형식으로 명사 추출
'''


# 단어 빈도수
nouns = []  # 명사 저장

for sent in ex_sent :
    #nouns.append(kkma.nouns(sent))  # 중첩리스트로 추가
    nouns.extend(kkma.nouns(sent))  # 단일 list
    
print(nouns)
'''
['나', '홍길동', '나이', '23', '23세', '세', '나', '대한', 
 '대한민국', '민국', '사람', '대한', '대한민국', '민국', '사랑']
'''


# 3. 문단 -> 형태소 추출  
kkma.morphs(para)



# 4. 문단 -> 품사(형태소) 태깅 
ex_pos = kkma.pos(para)
print(ex_pos)   # ('형태소', '품사')

'''
NNG 일반 명사 NNP 고유 명사 NNB 의존 명사 NR 수사 NP 대명사 VV 동사
VA 형용사 VX 보조 용언 VCP 긍정 지정사 VCN 부정 지정사 MM 관형사
MAG 일반 부사 MAJ 접속 부사 IC 감탄사 JKS 주격 조사 JKC 보격 조사
JKG 관형격 조사 JKO 목적격 조사 JKB 부사격 조사 JKV 호격 조사
JKQ 인용격 조사 JC 접속 조사 JX 보조사 EP 선어말어미 EF 종결 어미
EC 연결 어미 ETN 명사형 전성 어미 ETM 관형형 전성 어미 XPN 체언 접두사
XSN 명사파생 접미사 XSV 동사 파생 접미사 XSA 형용사 파생 접미사 XR 어근
SF 마침표, 물음표, 느낌표 SE 줄임표 SS 따옴표,괄호표,줄표
SP 쉼표,가운뎃점,콜론,빗금 SO 붙임표(물결,숨김,빠짐)
SW 기타기호 (논리수학기호,화폐기호) SH 한자 SL 외국어 SN 숫자
NF 명사추정범주 NV 용언추정범주 NA 분석불능범
'''


# NNG : 일반 명사, NNP : 고유 명사,  NP : 대명사 


# 5. 형태소 기준으로 단어 추출 
nouns = [] # 명사 저장 

for word, wclass in ex_pos : # ('형태소', '품사')
    if wclass == 'NNG' or wclass == 'NNP' or wclass=='NP' or wclass=='OL':
        nouns.append(word)

print(nouns) # 단어 








