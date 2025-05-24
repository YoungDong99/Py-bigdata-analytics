"""
Sample data 이용 연관규칙 모델 

준비 : mlxtend 패키지 설치
pip install mlxtend   
"""

import pandas as pd
pd.set_option('display.max_columns', 100) # 콘솔에서 보여질 최대 칼럼 개수
from mlxtend.frequent_patterns import apriori, association_rules # model 


# 1. sample data 생성  
data = {
    'User': [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10],
    'Item': ['milk', 'bread', 'bread', 'butter', 'milk', 'butter',
             'bread', 'milk', 'butter', 'bread', 'butter', 'milk',
             'milk', 'bread']
}

# 데이터프레임 생성
df = pd.DataFrame(data)
print(df) 


# 트랜잭션과 아이템 크기 
df.User.nunique() # 전체 트랜잭션 크기 = 10
df.Item.nunique() # 전체 아이템 크기 = 3

    
# 2. 트랜잭션(transaction) 데이터 만들기 : One-Hot Encoding 변환
group = df.groupby(['User','Item']) 

transaction = group.size().unstack().fillna(0) # 결측치 0 채우기 
print(transaction)
'''
Item  bread  butter  milk
User                     
1       1.0     0.0   1.0
2       1.0     1.0   0.0
3       0.0     1.0   1.0
4       1.0     0.0   0.0
5       0.0     1.0   1.0
6       1.0     0.0   0.0
7       0.0     1.0   0.0
8       0.0     0.0   1.0
9       0.0     0.0   1.0
10      1.0     0.0   0.0
'''


# 부울형(True/False) 변환  
transaction = transaction.astype(bool) 


# 3. 아이템 선택(Apriori 알고리즘 이용) : 지지도(1차)=0.1 기준   
frequent_itemsets = apriori(transaction, min_support=0.1, max_len=5, use_colnames=True) # 최소 지지도 0.1 
'''
transaction : 거래자료 
min_support : 최소 지지도 
max_len=5 : item 최대 길이 
use_colnames : item 이름 사용 여부 
'''

print(frequent_itemsets)  
'''
   support         itemsets
0      0.5          (bread)
1      0.4         (butter)
2      0.5           (milk)
3      0.1  (bread, butter)
4      0.1    (bread, milk)
5      0.2   (milk, butter)
'''

# 4. 연관 규칙 생성 : 신뢰도(2차)=0.2 기준  
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.2)  
'''
 metric="confidence" : 평가기준(신뢰도) or metric="lift" : 평가기준(향상도) 
 min_threshold=0.2 : 최소 신뢰도 0.2 이상  
'''  

print(rules) # 연관규칙 : 지지도(1차)=0.1 이상 & 신뢰도(2차)=0.2 이상 
'''
antecedents  consequents : 연관 규칙의 선행사건(A)과 후행사건(B) 항목
    예) (bread) => (butter) : 빵을 구매한 사람이 버터를 구매할 가능성
antecedent support : 선행사건(A) 발생한 비율 = A / 전체거래수 
    예) bread = 5 / 10 = 0.5 
consequent support : 후행사건(B) 발생한 비율 = B / 전체거래수 
    예) butter = 4 / 10 = 0.4  
support : 지지도 = (A ∩ B) / 전체거래수
    예) (bread) => (butter) : = 1 / 10 = 0.1 
confidence : 신뢰도(조건부 확률) = (A ∩ B) / LHS 거래수 
    에) (bread) => (butter) : = 1 / 5 = 0.2 
lift : 향상도(두 항목의 독립성을 고려한 연관관계 강도) = confidence / 지지도(RHS) 
    예) (bread) => (butter) : 0.2 / 0.4 = 0.5 

zhangs_metric : Zhang의 메트릭, 향상도(left) 평가 지표(left 평가 지표 : -1~1)
jaccard : LHS와 RHS의 교집합을 전체 합집합에 대한 비율(두 항목의 유사도 : 0~1)
        jaccard = (A ∩ B) / A + B - (A ∩ B) 
'''


print("\n연관 규칙 평가 지표 :")
final_rules = rules[['antecedents','consequents','support','confidence','lift','zhangs_metric','jaccard']]

print(final_rules)


# 5. 연관 규칙 시각화
import networkx as nx # 연관 네트워크 
import matplotlib.pyplot as plt # 시긱화 


""" 연관 규칙 네트워크 그래프 """ 
def plot_rules(rules, weight, top_n=10): # (rules, n)    
    rules = rules.nlargest(top_n, 'confidence') # 신뢰도 기준, 상위 n개  
    G = nx.DiGraph() # 네트워크 그래프 

    for _, rule in rules.iterrows():
        G.add_edge(rule['antecedents'], rule['consequents'], # 노드 : 타원  
                   weight=rule[weight]) # 엣지 : 가중치

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 6))
    nx.draw_networkx(G, pos, with_labels=True, node_color="lightblue", node_size=3000, edge_color="gray")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(f"Association Rules Graph : {weight}")
    plt.show()


# 함수호출 
plot_rules(final_rules, 'lift') # 두 항목의 연관관계 지표(0~1)  

plot_rules(final_rules, 'zhangs_metric') # lift 연관관계 평가 지표(-1 ~ 1)

plot_rules(final_rules, 'jaccard') # 두 항목 간의 유사성 측정 지표(0 ~ 1)


