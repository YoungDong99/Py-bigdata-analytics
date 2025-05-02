"""
유사 문서 검색 
영화 검색(추천) 시스템 : 코사인 유사도 기반  
"""

import pandas as pd # csv file 
from sklearn.feature_extraction.text import TfidfVectorizer # DTM  
from sklearn.metrics.pairwise import cosine_similarity # 코사인 유사도 

# 1. dataset load 
path = r'C:\ITWILL\3_TextMining\data'
data = pd.read_csv(path + '/movie_reviews.csv')
 
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1492 entries, 0 to 1491
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   reviews  1492 non-null   object
 1   title    1492 non-null   object
 2   label    1492 non-null   int64 
'''
 
# 2. Sparse matrix(DTM) : reviews 대상 

# 1) 단어생성기 
obj = TfidfVectorizer(stop_words='english') 

# 2) 희소행렬 
movie_sm = obj.fit_transform(data['reviews']) # 문장 반영 

# 3) scipy -> numpy array 
movie_sm_arr = movie_sm.toarray()
movie_sm_arr.shape #  (1492, 34641)


# 4) 영화제목 칼럼 추출
title = data.title # data['title']  


# 3. 검색어 -> 영화 검색(추천)  
def movie_search(query) :
    # 1) query 작성
    query_data = [query] # list 변경 
    
    # 2) query DTM 
    query_sm = obj.transform(query_data)
    query_sm_arr = query_sm.toarray() 
    
    # 3) 유사도 계산 
    sim = cosine_similarity(query_sm_arr, movie_sm_arr)     
    sim = sim.reshape(1492) 
    
    # 4) 내림차순 정렬 : index 정렬 
    sim_idx = sim.argsort()[::-1]
        
    global title # 전역변수 사용   
      
    
    # 유사도 & 영화제목 저장 
    sim_result = []  
    movie_title = []  
    
    # 5) Top5 영화추천하기 
    for idx in sim_idx[:5] :
        print(f'similarity : {sim[idx]} \n movie title : {title[idx]}  ')
        
        # [추가] Top5 유사도 & 영화제목 저장
        sim_result.append(sim[idx])
        movie_title.append(title[idx])
        
    return sim_result, movie_title  

# 주의 : 함수 호출 주석 처리      
#movie_search(input('search query input : ')) # action
    
'''
search query input : action
similarity : 0.20192921485638887 
 movie title : Soldier (1998)  
similarity : 0.1958404700223592 
 movie title : Romeo Must Die (2000)  
similarity : 0.18885169874338412 
 movie title : Aliens (1986)  
similarity : 0.18489066174805405 
 movie title : Speed 2: Cruise Control (1997)  
similarity : 0.16658803590038168 
 movie title : Total Recall (1990)
'''

'''
search query input : drama
similarity : 0.1931737274266525 
 movie title : Apollo 13 (1995)  
similarity : 0.11796112357272329 
 movie title : Double Jeopardy (1999)  
similarity : 0.11374906390472769 
 movie title : Practical Magic (1998)  
similarity : 0.11037479275255738 
 movie title : Civil Action, A (1998)  
similarity : 0.09607905933279662 
 movie title : Truman Show, The (1998) 
'''
 


 
 
