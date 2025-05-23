'''
UCI ML Repository 데이터셋 url
https://archive.ics.uci.edu/ml/datasets.php
'''

### 기본 라이브러리 불러오기
import pandas as pd
pd.set_option('display.max_columns', 100) # 콘솔에서 보여질 최대 칼럼 개수 
import matplotlib.pyplot as plt



### [Step 1] 데이터 준비 : 도매 고객 데이터셋 
'''
 - 도매 유통업체의 고객 관련 데이터셋으로 다양한 제품 범주에 대한 연간 지출액을 포함  
 - 출처: UCI ML Repository
'''
uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv'
df = pd.read_csv(uci_path)
df.info() # 변수 및 자료형 확인
'''
RangeIndex: 440 entries, 0 to 439
Data columns (total 8 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
 0   Channel           440 non-null    int64 : 유통업체 : Horeca(호텔/레스토랑/카페) 또는 소매(명목)
 1   Region            440 non-null    int64 : 지역 : Lisnon,Porto 또는 기타(명목) - 리스본,포르토(포르투갈)  
 2   Fresh             440 non-null    int64 : 신선함 : 신선 제품에 대한 연간 지출(연속)
 3   Milk              440 non-null    int64 : 우유 : 유제품에 대한 연간 지출(연속)
 4   Grocery           440 non-null    int64 : 식료품 : 식료품에 대한 연간 지출(연속)
 5   Frozen            440 non-null    int64 : 냉동 제품 : 냉동 제품에 대한 연간 지출(연속)
 6   Detergents_Paper  440 non-null    int64 : 세제-종이 : 세제 및 종이 제품에 대한 연간 지출(연속)
 7   Delicassen        440 non-null    int64 : 델리카슨 : 델리카트슨(수입식품) 제품(연속)
'''


### [Step 2] 데이터 탐색

# 데이터 살펴보기
print(df.head())  

# 명목형 변수 
df.Channel.value_counts() # 유통업체
'''
1    298 : Horeca
2    142 : 소매 
'''

df.Region.value_counts() # 유통 지역
'''
3    316 : 기타 
1     77 : Lisnon
2     47 : Porto 
'''

# 연속형 변수 
df.describe() # 나머지 연속형 변수(각 변수 척도 다름) 


### [Step 3] 데이터 전처리

# 분석에 사용할 변수 선택
X = df.copy()

# 설명변수 데이터 정규화
from sklearn.preprocessing import StandardScaler # 표준화 
X = StandardScaler().fit_transform(X)


### [Step 4] k-means 군집 모형 - sklearn 사용

# sklearn 라이브러리에서 cluster 군집 모형 가져오기
from sklearn.cluster import KMeans

# 모형 객체 생성 
kmeans = KMeans(n_clusters=5, n_init=10, max_iter=300, 
                random_state=45) # cluster 5개 
'''
Parameters
----------
n_clusters : int, default=8
n_init : int, default=10 - centroid seeds
max_iter : int, default=300
'''
        
# 모형 학습
kmeans.fit(X)  # KMeans(n_clusters=5) 

# 군집 예측 
cluster_labels = kmeans.labels_ # 예측된 레이블(Cluster 번호)    
print(cluster_labels) # 0 ~ 4



# 데이터프레임에 예측된 레이블 추가
df['Cluster'] = cluster_labels
print(df.head())   

df['Cluster'].value_counts() 
'''
4    212
2    125
0     91
1     11 -> 제거 
3      1 -> 제거 
'''

# 상관관계 분석 
r = df.corr() # 상관계수가 높은 변수 확인 
r
 
# 그래프로 표현 - 시각화
df.plot(kind='scatter', x='Grocery', y='Detergents_Paper', 
        c='Cluster', cmap='Set1', colorbar=True, figsize=(15, 10))
plt.show()  

# 각 클러스터 빈도수 : 빈도수가 적은 클러스터 제거 
print(df.Cluster.value_counts())


# 새로운 dataset 만들기 : 1,3번 클러스터 제거 예 
new_df = df[~((df['Cluster'] == 1) | (df['Cluster'] == 3))]

new_df.shape # (428, 9)
440 - 428 # 12

### [Step 5] 각 cluster별 특성 분석
group = new_df.groupby('Cluster')

# 연속형(숫자형) 변수 분석 
group.mean()
'''
          Channel    Region         Fresh         Milk       Grocery  \
Cluster                                                                
0        1.054945  1.307692  12183.945055  3254.714286   4130.923077   
2        2.000000  2.672000   7877.640000  8913.512000  14212.624000   
4        1.004717  2.995283  13980.273585  3360.995283   3860.905660   

              Frozen  Detergents_Paper   Delicassen  
Cluster                                              
0        3458.252747        860.263736  1149.934066  
2        1339.280000       6149.592000  1537.168000  
4        3760.872642        790.311321  1321.976415 
'''

# 각 군집별 subset 만들기 : 명목형 변수 분석 
cluster0 = new_df[new_df.Cluster == 0]
cluster0.Channel.value_counts() 
'''
1    86 : Horeca
2     5 : 소매업 
''' 
cluster0.Region.value_counts() # [1, 2]
'''
1    63
2    28
'''

cluster2 = new_df[new_df.Cluster == 2]
cluster2.Channel.value_counts() # [2] : 소매업 
cluster2.Region.value_counts() # [3, 1, 2] : 전지역 

cluster4 = new_df[new_df.Cluster == 4]
cluster4.Channel.value_counts() # [1] : Horeca 
cluster4.Region.value_counts() # [3] : 기타

'''
cluster0 : 유통업체는 Horeca, 지역은 리스본, 포르토, 연간 지출액은 중간 그룹(Milk, Detergents_Paper)
cluster2 : 유통업체는 소매업, 지역은 전지역, 연간 지출액은 가장 많은 그룹(Milk, Grocery,Detergents_Paper,Delicassen) 
cluster4 : 유통업체는 Horeca, 지역은 기타, 연간 지출액은 가장 적은 그룹(Grocery, Detergents_Paper)
'''


