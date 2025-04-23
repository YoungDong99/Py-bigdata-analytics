'''
 문2) html02.html 웹 문서를 대상으로 형태소 분석으로 명사를 추출하여 
    출현빈도 Top5에 해당하는 단어와 빈도를 출력하시오. <출력결과> 참고
    
   <출력 결과>
   ----------------
   Top5 단어
   ----------------
   태그   ->   4
   링크   ->   3
   네이버   ->   3
   줄   ->   2
   바꿈   ->   2 
'''

from konlpy.tag import Okt # 형태소분석  
from collections import Counter # TopN 단어 선택


# 1. file 자료 가져오기 
path = r"C:\ITWILL\3_TextMining\data"
file = open(path + '/html02.html', encoding='utf-8')
data = file.read() # 문자열 읽기 
file.close()


print(data) # 형태소분석을 위한 텍스트 자료(문단) 


# 2. Okt 형태소 분석기 생성 
okt = Okt()


# 3. 명사(단어) 추출 
nouns = okt.nouns(phrase = data)


# 4. 단어 카운트 
wc = {}

for word in nouns :
    wc[word] = wc.get(word, 0) + 1


# 5. TopN 단어 선정
count = Counter(wc)

top5 = count.most_common(5)

print('-'*20)
print('Top 5 단어')
print('-'*20)

for word, cnt in top5 :
    print(word, cnt, sep = ' -> ')





















