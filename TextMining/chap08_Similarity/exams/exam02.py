"""
문2) 한국영화 후기(review_data.csv) 파일을 대상으로 아래와 같은 조건으로
     키워드를 입력하여 관련 영화 후기를 검색하는 함수를 정의하시오.   

 <조건1> 사용할 칼럼 : review2 
 <조건2> 사용할 문서 개수 : 1번째 ~ 5000번째   
 <조건3> 코사인 유사도 적용 - 영화 후기 검색 함수
         -> 검색 키워드와 가장 유사도가 높은 상위 3개 review 검색  
 <조건4> 검색 키워드 : 액션영화, 시나리오, 중국영화 
        -> 위 검색 키워드를 하나씩 입력하여 관련 후기 검색   
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. dataset load 
path = r'C:\ITWILL\3_TextMining\data'
data = pd.read_csv(path + "/review_data.csv")
data.info() 
'''
 0   id       34525 non-null  int64 
 1   review   34525 non-null  object
 2   label    34525 non-null  int64 
 3   review2  34525 non-null  object -> 사용할 칼럼 
'''
print(data.head())


# 사용할 문서 5,000개 제한  
review = data.review2[:5000] # 1번째 ~ 5000번째 문서 
print(review)

# 2. sparse matrix 생성 : overview 칼럼 대상 
tfidf = TfidfVectorizer()

review_dtm_arr = tfidf.fit_transform(review)  # 전체 data['review2'] → review (5000개만)

review_dtm_arr.shape  # (5000, 19361)


# 3. cosine 유사도 : 영화 후기 검색 함수  
def review_search(query) : 
    # 1) query 작성
    query_list = [query] # list 변경 
    
    # 2) query DTM 
    query_dtm = tfidf.transform(query_list)
    query_dtm_arr = query_dtm.toarray() 
    
    # 3) 유사도 계산 
    sim = cosine_similarity(query_dtm_arr, review_dtm_arr) 
    sim = sim.reshape(5000) # 모양변경 : 2d -> 1d
    
    # 4) 내림차순 정렬 : index 정렬 
    idxs = sim.argsort()[::-1]
        
    global review # 전역변수 사용 
    
    # 5) Top5 영화추천하기 
    for idx in idxs[:3] :
        print(f'similarity : {sim[idx]} \n movie title : {review[idx]}  ')


# 4. 검색 키워드 : 액션영화, 시나리오, 중국영화   
review_search(input('검색할 키워드 입력 : '))






