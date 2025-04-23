"""
konlpy : 한글 형태소 분석을 제공하는 패키지 
 - 형태소 : 문장을 품사 단위로 쪼개는 과정 

형태소분석기 설치(java 설치 필요) 
(base) pip install konlpy
"""

from konlpy.tag import Okt 

# Okt 형태소 분석기 생성
okt = Okt() # 객체 생성 


# 문단(Paragraph) : 3개 문장 
para  = "나는 홍길동 입니다. age는 23세 입니다. 나는 대한민국 사람입니다."


# 1. okt.normalize : 문단을 okt에 적합한 문자열로 변환(일반화) 
text_normal = okt.normalize(para) 

# 2. okt.nouns : 명사 추출 : 일반화된 문자열에서 명사 추출  
okt.nouns(text_normal) 


print(okt.nouns(text_normal))
