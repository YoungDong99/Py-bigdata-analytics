"""
konlpy : 한글 형태소 분석을 제공하는 패키지 
 - 형태소 : 문장을 품사 단위로 쪼개는 과정 

주요 형태소 분석기
 한나눔(Hannanum) : KAIST에서 개발한 한글 형태소 분석기, 복합명사 분해, 어근추출, 명사추출 등의 기능(java구현)
 꼬꼬마(Kkma) : 서울대학교 연구실에서 개발한 형태소 분석기, 비교적 정확한 분석 결과를 제공(java구현)
 코모란(Komoran) : Shineware에서 개발한 형태소 분석기, 대용량 말뭉치에서 학습된 모델을 사용하여 형태소 분석(java 구현)
 Okt(Open Korean Text) : 형태소 분석 및 품사 태깅 기능을 제공하며, 사용자 사전을 추가할 수 있는 기능(python 구현)
 Twitter : 현재 Okt 제공 
"""

import konlpy.tag

dir(konlpy.tag)
'''
 'Hannanum'
 'Kkma'
 'Komoran'
 'Mecab'
 'Okt'
 'Twitter'
'''

from konlpy.tag import Hannanum


# Hannanum 형태소 분석기 생성 
hanna = Hannanum()  # 객체 생성

dir(hanna)
'''
analyze : 복합명사 분해
jhi     : 주어, 목적어, 서술어 등 구 구분 
morphs  : 형태소
nouns   : 명사 ㅊ출
pos     : 품사 태깅
tagset  : 품사 태그 집합 확인
'''


# 분석할 한글 문장
text = "한나눔 형태소 분석기를 사용해보는 예제입니다. 실습하자"


# 1) 명사 추출
nouns = hanna.nouns(text)
print("명사 :", nouns) 
'''
명사 : ['한나눔', '형태소', '분석기', '사용', '예제', '실습하자']
'''

# 2) 형태소 분석  
morphs = hanna.morphs(text)
print("형태소 :", morphs)
'''
형태소 : ['한나눔', '형태소', '분석기', '를', '사용', '하', '어', '보', 
         '는', '예제', '이', 'ㅂ니다', '.', '실습하자']
'''

# 3) 형태소의 품사 태깅 
pos_tags = hanna.pos(text)
print("품사 태깅 :", pos_tags)
'''
N: Noun (명사)
J: Josa (조사)
X: Josa appended to adjective stems (형용사에 붙이는 조사)
E: Eomi (어미)
P: PreEomi (선어말어미)
S: Symbol (기호)
'''

# 4) 문장의 구문 분석
analyze = hanna.analyze(text) 
print(analyze)  
'''
ncn: Common noun (일반 명사)
nqq: Other proper noun (기타 고유 명사)
ncpa: Noun phrase (명사구)
jco: Conjunction (접속 조사)
xsva: Verb stem (동사 어간)
ecx: Case-marking particle (격 조사)
px: PreEomi (선어말어미)
etm: Ending particle (선어말어미)
jp: Josa Particle (조사 어미)
ef: Sentence-final ending (마침표)
sf: Final punctuation (문장 부호)
sy: Other punctuation (기타 부호)
''' 












