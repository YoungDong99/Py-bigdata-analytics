"""
kNN 분류기 구현 
"""

import random # 난수 생성 모듈 
from statistics import sqrt # 제곱근(루트) 함수 

random.seed(100) # 난수 seed값 지정(난수 고정) 

### 단계1. data 생성 

# 1) 기준(p) 1개 : 소숫점 5자리 반올림
p = [round(random.random(), 5), round(random.random(), 5)]

# 2) 대상(q) 10개  : 소숫점 5자리 반올림 
q = [[round(random.random(), 5), round(random.random(), 5)] for i in range(10)]
# [ q[x,y], ....., q10[x,y] ]
print('p : ', p)
print('q :', q)
print('-'*60)



# 단계2. kNN 분류기(클래스 정의) : 변수(데이터) + 메서드(알고리즘)
class kNN :    
    def __init__(self, p, q):
        self.p = p
        self.q = q
        
    def distance(self, Q):
        # 거리 계산
        return round(sqrt((self.p[0] - Q[0])**2 + (self.p[1] - Q[1])**2), 5)
        
    def k_nearest(self, k):
        # 리스트 만들기
        d_list = [(self.distance(Q), Q) for Q in self.q]
        # 정렬
        d_list.sort(key=lambda x: x[0])
        # 최근접이웃 선정
        top = d_list[:k]
        
        distances = [t[0] for t in top]
        
        Qs = [t[1] for t in top]
        return distances, Qs 
    
    
    
# 단계3. kNN 객체 생성             
knn = kNN(p, q) # 생성자(기준, 대상)

for k in [1, 3, 5]:
    distances, Qs = knn.k_nearest(k)
    print(f'k{k} -> {distances}')
    print('real data', end =' ')
    for qs in Qs:
        print(qs, end =' ')
    print('\n')


# 포인트 시각화
import matplotlib.pyplot as plt

# 기준(p) : p[0,1]
# 대상(q) : [q1[0,1], ... q10[0,1]]

x = [ data[0] for data in q ]
y = [ data[1] for data in q ]


plt.scatter(x=p[0], y=[1], c='b')
plt.scatter(x=x, y=y, c='r')
# q 레이블 표시 : plt.text(x, y, name) 
for data in q :
    x = data[0]
    y = data[1]
    name = (x, y) # 텍스트
    plt.text(x, y+0.02, name)




plt.show()























