"""
문1) 브라운대학교 말뭉치의 문서파일 10개를 대상으로 단어를 추출한 후 피클(pickle) 파일로 저장하시오.
     조건> 파일경로 및 파일명 : 'C:\ITWILL\3_TextMining\data\brown_words.pkl'
"""

import nltk # anaconda 제공 패키지

# 단계1 : 브라운대학교 말뭉치(Brown Corpus) 로드 
from nltk.corpus import brown

dir(brown)
'''
fileids
raw
paras
sents
words
'''

# 단계2 : 브라운 대학교 말뭉치 다운로드 
nltk.download('brown')


# 단계3 : 말뭉치에 문서 파일 가져오기    
fileids = brown.fileids()  # # 전체 문서파일 가져오기 
print(fileids)
len(fileids)


# 단계4 : 문서 파일 10개 선택  
files = fileids[:10]


# 단계5 : 문서 파일 10개에서 단어 가져오기 
brown_words = brown.words(files) 
print(brown_words) 
# ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
len(brown_words) # 22,491개 단어 
type(brown_words)


# 단계6 : pickle 파일 저장 : 완성 
import pickle 

path = r'C:\ITWILL\3_TextMining\data'


# file save 
file = open(path + '/brown_words.pkl', mode='wb')
pickle.dump(brown_words, file)
file.close()


# file load 
file = open(path + '/brown_words.pkl', mode='rb')
news_data = pickle.load(file)
print(news_data)



