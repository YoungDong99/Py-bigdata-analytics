"""
문2) 아래와 같은 단계로 kMeans 알고리즘을 적용하여 확인적 군집분석을 수행하시오.

 <조건> 변수 설명 : tot_price : 총구매액, buy_count : 구매횟수, 
                   visit_count : 매장방문횟수, avg_price : 평균구매액

  단계1 : 3개 군집으로 군집화 
  단계2: 원형데이터에 군집 예측치 추가  
  단계3 : tot_price 변수와 가장 상관계수가 높은 변수로 산점도(색상 : 클러스터 결과)  
  단계4 : 산점도에 군집의 중심점 시각화
  단계5 : 군집별 특성분석 : 우수고객 군집 식별
"""

import pandas as pd
from sklearn.cluster import KMeans # kMeans model
import matplotlib.pyplot as plt


sales = pd.read_csv("C:/ITWILL/5_Python_ML/data/product_sales.csv")
print(sales.info())
'''
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
tot_price      150 non-null float64 -> 총구매금액 
visit_count    150 non-null float64 -> 매장방문수 
buy_count      150 non-null float64 -> 구매횟수 
avg_price      150 non-null float64 -> 평균구매금액 
'''

# 단계1 : 3개 군집으로 군집화
model = KMeans(n_clusters=3).fit(sales)
 
# 단계2: 원형데이터에 군집 예측치 추가
pred = model.predict(sales)
pred # 0 ~ 2
  
sales['predict'] = pred 

# 단계3 : tot_price 변수와 가장 상관계수가 높은 변수로 산점도(색상 : 클러스터 결과)
sales.corr().loc['tot_price']  
'''
tot_price      1.000000
visit_count    0.817954
buy_count     -0.013051
avg_price      0.871754  -> 가장 상관계수가 높은 변수
predict       -0.371636
'''

# 산점도 : x=tot_price, y=avg_price 
plt.scatter(x=sales.tot_price, y=sales.avg_price,
            c=sales.predict)

# 단계4 : 산점도에 군집의 중심점 시각화
centers = model.cluster_centers_
print(centers) # 각 변수의 중심점 
'''
tot_price  visit_count  buy_count   avg_price
[[5.006      0.244      3.284      1.464     ]
 [5.9016129  1.43387097 2.75483871 4.39354839]
 [6.85       2.07105263 3.07105263 5.74210526]]
'''

# 중앙값 추가 : tot_price vs avg_price 
plt.scatter(x=centers[:,0], y=centers[:,3], 
            c='r', marker='D')
plt.show()


# 단계5 : 군집별 특성분석 : 우수고객 군집 식별
group = sales.groupby('predict')    

# 그룹별 통계 
group.mean()   
'''
         tot_price  visit_count  buy_count  avg_price
predict                                              
0         6.853846     2.053846   3.074359   5.715385
1         5.006000     0.244000   3.284000   1.464000
2         5.883607     1.434426   2.747541   4.388525
'''
# 0번 군집 : 다른 군집에 비해서 평균 총구매금액과 방문횟수가 많다.  


