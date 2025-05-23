'''
계층적 군집분석(Hierarchical Clustering) 
 - 상향식(Bottom-up)으로 계층적 군집 형성 
 - 유클리드안 거리계산식 이용 
 - 숫자형 변수만 사용
'''

from scipy.cluster.hierarchy import linkage, dendrogram # 군집분석 도구 
import matplotlib.pyplot as plt # 시각화 
from sklearn.datasets import load_iris # dataset
import pandas as pd # DataFrame

#########################
# sample data : ppt.11
#########################
df = pd.DataFrame({'x' : [1, 2, 2, 4, 5],
                   'y' : [1, 1, 4, 3, 4]})
print(df)
'''
   x  y
0  1  1  -> p1 
1  2  1  -> p2
2  2  4  -> p3
3  4  3  -> p4
4  5  4  -> p5
'''

# 계층적 군집모형 
model = linkage(df, method='single') # 군집화 방법 : 단일연결법 
'''
method : 'single', 'complete', 'average', 'weighted', 'ward' 
'''
help(linkage)

# 덴드로그램 시각화 
plt.figure(figsize = (25, 10))
dendrogram(model)
plt.show()

print(model)
'''
  p          q       거리(distance) 노드 수   
[[0.         1.         1.         2.        ]
 [3.         4.         1.41421356 2.        ]
 [2.         6.(3+4)    2.23606798 3.        ]
 [5.(0+1)    7.(2+3+4)  2.82842712 5.        ]]
'''

# 1. dataset loading
iris = load_iris() # Load the data

X = iris.data # x변수 
y = iris.target # y변수(target) - 숫자형 : 거리계산 

# X + y 결합  
iris_df = pd.DataFrame(X, columns=iris.feature_names)
iris_df['species'] = y # target 추가 

iris_df.info()

# 2. 계층적 군집분석 
clusters = linkage(iris_df, method='single')
'''
군집화 방식 : ppt.9 참고 
method = 'single' : 단순연결(default)
method = 'complete' : 완전연결 
method = 'average' : 평균연결
method = 'centroid' : 두 중심점의 거리 
'''
print(clusters)
clusters.shape # (149, 4)


# 3. 덴드로그램(dendrogram) 시각화 : 군집수 사용자가 결정 
plt.figure(figsize = (25, 10))
dendrogram(clusters)
plt.show() # 군집수 = 3개 


from scipy.cluster.hierarchy import fcluster # 군집 자르기 도구 
import numpy as np # 클러스터 빈도수 


# 4. 군집(cluster) 자르기 : ppt.17 ~ 18 참고
cut_cluster = fcluster(clusters, t=3, criterion='maxclust') # t=3개
cut_cluster # 1 ~ 3

# 군집(cluster) 빈도수 
unique, counts = np.unique(cut_cluster, return_counts=True)
print(unique, counts)


# 5. DF 칼럼 추가 
iris_df['cluster'] = cut_cluster
iris_df

# 6. 계층적군집분석 시각화 
plt.scatter(iris_df['sepal length (cm)'], iris_df['petal length (cm)'],
            c=iris_df['cluster'])
plt.show()


# 7. 각 군집에 특성 분석 
'''
연속형변수 : 통계(평균, 편차)
이산형변수 : 각 범주 분석  
'''

group = iris_df.groupby('cluster') # 1,2,3
group.size()
'''
1    50
2    50
3    50
'''
# 군집별(cluster) 평균 
group.mean().T
'''
cluster                1      2      3
sepal length (cm)  5.006  5.936  6.588
sepal width (cm)   3.428  2.770  2.974
petal length (cm)  1.462  4.260  5.552
petal width (cm)   0.246  1.326  2.026
species            0.000  1.000  2.000 : 꽃의종별

연속형변수 기준 :
     군집1 : 대체적으로 길이 또는 넓이가 작은 성향 
     군집2 : 대체적으로 길이 또는 넓이가 중간 성향 
     군집3 : 대체적으로 길이 또는 넓이가 큰 성향      
'''


