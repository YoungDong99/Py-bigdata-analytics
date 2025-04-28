"""
6.nltk.cluster : 텍스트 군집화, 유사문서끼리 분류   
"""

'''
단계1. 필요한 라이브러리 가져오기
''' 
import nltk
from nltk.cluster import KMeansClusterer  
from nltk.corpus import stopwords # 불용어 
from nltk.tokenize import word_tokenize # 단어생성기 
import numpy as np # 영행렬 
import pandas as pd # 문서단어행렬 


'''
단계2. 데이터 준비
 - 간단한 문서 집합을 정의하여 클러스터링 자료 사용 
'''

# 문서 데이터셋 
documents = [  # 정답 없음 : 비지도 학습
    "I love watching movies",
    "The movie was fantastic and exciting",
    "Hiking is a great outdoor activity",
    "I enjoy going on hikes in the mountains", # 1
    "Movies are a great way to relax",
    "Mountains and nature hikes are my favorite activities" # 1 
]



'''
단계3. 전처리 및 특성 추출
 - 문서를 토큰화하고, 불용어(stopwords) 제거 후, 각 문서 벡터화
'''

# 불용어 설정
stop_words = set(stopwords.words('english'))


# 문서 토큰화 & 벡터화 함수
def document_features(document):
    tokens = word_tokenize(document.lower()) # 토큰화 
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words] # 벡터화  
    return tokens


# 각 문서 벡터화 
vectorized = [document_features(doc) for doc in documents]
'''
벡터화 : 문장을 컴퓨터가 처리할 수 있도록 숫자로 바꾸는 작업
'''

print(vectorized)
'''
[
 ['love', 'watching', 'movies'], 
 ['movie', 'fantastic', 'exciting'], 
 ['hiking', 'great', 'outdoor', 'activity'], 
 ['enjoy', 'going', 'hikes', 'mountains'], 
 ['movies', 'great', 'way', 'relax'], 
 ['mountains', 'nature', 'hikes', 'favorite', 'activities']
]
'''


# 단어 수집 & 중복단어 제거       
all_words = []
for word_vec in vectorized :
    all_words.extend(word_vec)


all_words = list(set(all_words)) # 중복제거 



# 문서 벡터화
def vectorize(documents, all_words):
    zeros = np.zeros( (len(documents), len(all_words)) ) # 영행렬
    dtm = pd.DataFrame(zeros, columns = all_words) # 문서단어행렬 
       
    for doc, word_vec in enumerate(vectorized) : 
        for word in word_vec :
            dtm.loc[doc, word] += 1 # 각 문서의 단어빈도수   

    return dtm


# 문서단어행렬 : 모든 문서 벡터화
dtm = vectorize(documents, all_words)
print(dtm)
'''
   going  nature  movie  love  ...  hiking  watching  great  activities
0    0.0     0.0    0.0   1.0  ...     0.0       1.0    0.0         0.0
1    0.0     0.0    1.0   0.0  ...     0.0       0.0    0.0         0.0
2    0.0     0.0    0.0   0.0  ...     1.0       0.0    1.0         0.0
3    1.0     0.0    0.0   0.0  ...     0.0       0.0    0.0         0.0
4    0.0     0.0    0.0   0.0  ...     0.0       0.0    1.0         0.0
5    0.0     1.0    0.0   0.0  ...     0.0       0.0    0.0         1.0
'''


'''
단계4. K-평균 클러스터링 수행
 - KMeansClusterer를 사용하여 클러스터링 수행
'''

# 클러스터링 설정 
num_clusters = 2  # 두 개의 그룹으로 나누기

# 분류기 : 클러스터링 객체 생성
clusterer = KMeansClusterer(num_clusters, 
                            distance=nltk.cluster.util.cosine_distance, 
                            repeats=25)
'''
num_clusters : 클러스터 개수
distance : 거리 측정 방식 – 여기선 코사인 거리(cosine distance)
repeats : 클러스터링 반복 횟수 (다른 초기값 시도해서 안정적인 결과 유도)

코사인 거리 : 벡터들이 이루는 각도(유사도) 를 기준으로 문서의 유사성을 측정하는 방법
-> 단어의 출현 패턴이 비슷하면 각도가 작아짐 = 유사한 문서라고 판단
'''


# 분류기에 데이터셋 적용 
clusters = clusterer.cluster(dtm.values, assign_clusters=True)
'''
dtm.values : 문서-단어 행렬의 넘파이 배열 (2차원 벡터)
→ 각 문서가 숫자 벡터로 표현됨	
assign_clusters=True : 문서들을 클러스터에 직접 할당해서 결과 리턴
''' 

# 클러스터 결과 출력
for i, cluster in enumerate(clusters):
    print(f"Document {i} is in cluster {cluster}")
    
'''
Document 0 is in cluster 0
Document 1 is in cluster 0
Document 2 is in cluster 0
Document 3 is in cluster 1
Document 4 is in cluster 0
Document 5 is in cluster 1
'''




    
    
    
    
    
    