"""
k평균 이용 : 문서 군집화(clustering) 
"""

from sklearn.feature_extraction.text import TfidfVectorizer # 벡터화
from sklearn.cluster import KMeans # 군집화 model
import numpy as np # 다차원 배열


# 예제 문서 데이터
documents = [
    "I don't like rainy days.",
    "She isn't feeling well today.",
    "They haven't finished their homework yet.",
    "He can't stand the cold weather.",
    "We didn't enjoy the movie at all.",
    "I love spending time with my family.",
    "She is an incredibly talented musician.",
    "They have accomplished so much in their careers.",
    "He always has a positive attitude.",
    "We had a fantastic time on our vacation."
]

# TF-IDF 벡터화
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
print(tfidf_matrix)


# K-평균 클러스터링 수행
num_clusters = 2  # 두 개의 그룹으로 나누기
kmeans = KMeans(n_clusters=num_clusters)  # Kmeans 빈 model 생성
kmeans.fit(tfidf_matrix)  # model 학습

dir(kmeans)
print(kmeans.labels_)  # [1 0 1 1 1 1 0 1 1 1]


# 클러스터 결과 출력
for i in range(num_clusters):
    cluster = np.where(kmeans.labels_ == i)[0] # 조건식의 True인 요소의 인덱스 반환
    print(f"Cluster {i+1}:")
    for doc_index in cluster :
        print(f" - {documents[doc_index]}")       

        