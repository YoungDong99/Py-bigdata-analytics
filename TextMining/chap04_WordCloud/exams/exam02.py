"""
문2) review_data.csv 파일의 'review2' 칼럼을 대상으로 다음과 같이 
    단계별로 단어의 빈도수를 구하고, 단어 구름으로 시각화하시오.
"""
import pandas as pd
from konlpy.tag import Okt
from wordcloud import WordCloud 

# 1. file load 
path = r'C:\ITWILL\3_TextMining\data'
review_data = pd.read_csv(path + '/review_data.csv', encoding='utf-8')

print(type(review_data))  # <class 'pandas.core.frame.DataFrame'> 
# 테이블 구조를 갖는 데이터 프레임

review_data.info()
'''
RangeIndex: 34525 entries, 0 to 34524
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   id       34525 non-null  int64 
 1   review   34525 non-null  object
 2   label    34525 non-null  int64 
 3   review2  34525 non-null  object  -> 선택할 칼럼 
''' 

# 2. review2 칼럼 선택 
reviews = review_data.review2

print(reviews)


# 3. 문장 추출 :  Okt 클래스 이용
okt = Okt()
sents = [okt.normalize(str(review)) for review in reviews]

print(sents)


# 4. 명사 추출 : Okt 클래스 이용 
nouns = []
for sent in sents :
    for noun in okt.nouns(sent) :
        nouns.append(noun)

print(nouns)


# 5. 전처리 : 2음절~5음절 단어 선정  
final_nouns = []
for noun in nouns :
    if len(noun) > 1 :
        final_nouns.append(noun)

print(final_nouns)


# 6. Top100 word 선정  
from collections import Counter
top100_word = Counter(final_nouns).most_common(100)
print(top100_word)


# 7. 단어 구름 시각화 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')


wc_result = wc.generate_from_frequencies(dict(top100_word))

import matplotlib.pyplot as plt 

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기 
plt.show()







