'''
 문1) html01.html 웹 문서를 대상으로 다음 조건에 맞게 형태소 분석으로 단어를 추출하시오. <출력결과> 참고
      <조건1> 추출 단어 품사 : NNG(일반 명사), NNP(고유 명사), OL(영문)
      <조건2> 2음절~5음절 사이의 길이를 갖는 단어 선정 : len() 이용 
      <조건3> 중복 단어 제외 : set() 이용 
      <조건4> 단어 목록 출력 
    
   <단어 목록>
   ['광고', 'html', '정보', 'UTF-8', '제목', 'nav', 'li', '작성자', '저작권', 'title', 
    '보호', 'head', 'ul', '구분', '태그', '부여', 'meta', '개인', '로그', '머리말', '보조', 
    'body', '꼬리말', 'aside', '시멘', '게이', '문서', '주요', '내용', '의미', '사이트', '메뉴', '소개']
'''

from konlpy.tag import Kkma # 형태소분석  


# 1. file 자료 가져오기 
path = r"C:\ITWILL\3_TextMining\data"
file = open(path + '/html01.html', encoding='utf-8')
data = file.read() # 문자열 읽기 
file.close()


print(data) # 형태소분석을 위한 텍스트 자료(문단) 


# 2. Okt 형태소 분석기 생성 
kkma = Kkma()

ex_pos = kkma.pos(data)


# 3. 단어 추출 : NNG(일반 명사), NNP(고유 명사), OL : 영문
nouns = [] # 단어 저장 

for word, wclass in ex_pos : # ('형태소', '품사')
    if wclass == 'NNG' or wclass == 'NNP' or wclass=='NP' or wclass=='OL':
        nouns.append(word)

print(nouns)
print('단어 개수 :', len(nouns))


# 4. 2음절~5음절 길이 단어 선정  
final_nouns = []

for w in nouns :
    if len(w) >= 2 and len(w) <= 5 :
        final_nouns.append(w)


# 5. 중복 단어 제거 & 단어목록 출력

final_nouns = list(set(final_nouns))

print('\n최종 단어 목록')
print(final_nouns)
print('단어 갯수 :', len(final_nouns))


















