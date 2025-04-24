"""
문1) 네이버 인기글을 수집한 텍스트 파일(cafe-hots.txt)를 대상으로
    다음과 같은 단계별로 단어의 빈도수를 구하고 단어 구름으로 시각화하시오.
"""

from konlpy.tag import Kkma # 형태소 분석기 
from wordcloud import WordCloud # 단어구름 시각화 
from re import match # 단어 전처리 
from collections import Counter # TopN 단어 선정 

# 1. text file read : cafe에서 파일 다운로드 
path = r'C:\ITWILL\3_TextMining\data'
file = open(path + '/cafe-hots.txt', mode='r', encoding="utf-8")
texts = file.read()
file.close()
print(texts)


kkma = Kkma() # 형태소 분석기


# 2. 문장 추출  
sents = kkma.sentences(texts)
print(sents)
len(sents)

# 3. 단어(명사) 추출  
nouns = [] # 중복 명사 저장
for sent in sents :
    nouns.extend(kkma.nouns(sent))

print(nouns)


# 4. 단어 빈도수 & 전처리(단어 길이 1음절 제외, 서수 제외)
nouns_count = {} # 단어 카운터 
for word in nouns :
    if len(word) > 1 and not(match('^[0-9]', word)):
        nouns_count[word] = nouns_count.get(word, 0) + 1

print(nouns_count)


# 5. Top10 word 선정  
top10_word = []

top10_word = Counter(nouns_count).most_common(10)

print(top10_word)

# 6. 단어 구름 시각화 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')


wc_result = wc.generate_from_frequencies(dict(top10_word))

import matplotlib.pyplot as plt 

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기 
plt.show()



