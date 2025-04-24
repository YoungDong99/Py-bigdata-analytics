'''
<작업순서> 
1. text file 읽기 
2. 문장 추출
3. 명사 추출 : Kkma
4. 단어 전처리 : 단어 길이 제한, 숫자 제외 
5. 단어, 단어빈도수 준비 
6. 단어 시각화 : 막대와 선 그래프 이용
'''

from konlpy.tag import Kkma # class - 형태소 
import matplotlib.pyplot as plt # 별칭 : 그래프 시각화  


# 1. text file 읽기 
path = r'C:\ITWILL\3_TextMining\data'

file = open(path + '/text_data.txt', mode='r', encoding='utf-8')
data = file.read()
print(data)

kkma = Kkma() # Kkma 객체 생성 


# 2. 문장 추출 : 문단(str) -> 문장(list) 
ex_sent = kkma.sentences(data)
print(ex_sent)  # 문장 list 


# 3. 명사 추출 : 문장(5개) -> 명사 
nouns = kkma.nouns(data)  # 문단 -> 명사 (중복 명사 제외)
print(nouns)
print(len(nouns))  # 18

# 중첩 list로 생성됨
#nouns = [ kkma.nouns(sent) for sent in ex_sent ]  

# 문장 -> 명사 (중복 명사 허용)
nouns = []
for sent in ex_sent :
    nouns.extend(kkma.nouns(sent))

print(nouns)
print(len(nouns))  # 24


# 4. 단어 전처리 
from re import match # 숫자 제외 

nouns_count = {} # 단어 카운터 

for noun in nouns : 
    # 선정 단어 : 2음절 이상 & 서수 제외
    if len(noun) > 1 and not(match('^[0-9]', noun)) :
        nouns_count[noun] = nouns_count.get(noun, 0) + 1

print(nouns_count)

# 5. 단어와 단어빈도수 준비         
words = []
count = []

for word, cnt in nouns_count.items() :
    words.append(word)
    count.append(cnt)


# 6. 단어 시각화 : 그래프 이용 

# 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'

# 막대그래프
plt.bar(words, count, color='blue')  # 막대차트 > x축 : 단어, y축 : 빈도수
plt.title('텍스트 빈도 분석')  # 차트 제목
plt.xticks(rotation=90)  # x축이름 90도 회전
plt.show()  # 차트 보이기

# 선 그래프
plt.plot(count, words, color='blue')  # 막대차트 > x축 : 빈도수, y축 : 단어
plt.title('텍스트 빈도 분석')  # 차트 제목
plt.show()




