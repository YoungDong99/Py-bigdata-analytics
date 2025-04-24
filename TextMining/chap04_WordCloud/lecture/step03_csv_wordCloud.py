"""
1. csv file 읽기
2. 칼럼 선택  
3. 문장 추출 : Okt
4. 명사 추출 : Okt
5. 단어 전처리 : 단어 길이 제한 
6. TopN 단어 선정
7. Word Cloud
"""

import pandas as pd  # csv file read
from konlpy.tag import Okt  # 한글 형태소 분석기
from wordcloud import WordCloud   # 단어구름 시각화


# 1. csv file 읽기
path = r'C:\ITWILL\3_TextMining\data'
daum_news = pd.read_csv(path + '/daum_news.csv')


# 2. 칼럼 선택
daum_news.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 21 entries, 0 to 20
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   title   21 non-null     object
 1   news    21 non-null     object  -> (선택)
dtypes: object(2)
memory usage: 468.0+ bytes
'''
news = daum_news.news

print(news)

okt = Okt() # Okt 객체 생성 : 형태소 분석기  


# 3. 문장 추출 : 문자열 변환 
sents = [okt.normalize(str(new)) for new in news ]

print(sents)

# 4. 명사 추출 : Okt 클래스 이용 
nouns = [] 
for sent in sents :
    for noun in okt.nouns(sent): 
        nouns.append(noun)
        
print(nouns)
len(nouns)



# 5. 단어 전처리 : 단어 선정  
final_nouns = [] # 선정 단어  

# list에서 불용어 처리 : '때문', '통해', '대해', '위해'

not_nouns = ['위해', '대해', '통해', '때문', '이번', '라며', '이후', '지난']

for noun in nouns :
    if len(noun) > 1 and noun not in not_nouns :
        final_nouns.append(noun)
        
print(final_nouns)
len(final_nouns)




# 6. Top50 word  
from collections import Counter # class 
top50_word = Counter(final_nouns).most_common(50) # top50 
print(top50_word)


# 7. word cloud 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')


wc_result = wc.generate_from_frequencies(dict(top50_word))

import matplotlib.pyplot as plt 

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기 
plt.show()






