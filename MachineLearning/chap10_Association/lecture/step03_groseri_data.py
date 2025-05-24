"""
식료품(Groseri) 데이터 이용 연관규칙 모델
"""

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder # 트랜잭션 data 
from mlxtend.frequent_patterns import apriori, association_rules # model 


# 1. 파일 경로로 CSV 파일 읽기 
path = r'C:\ITWILL\5_Python_ML\data'
data = pd.read_csv(path + '/groceries.csv', header=None) # 제목 없음 

data_arr = data.values


# 2. 줄 단위 트랜잭션 변환
transactions = []
for row in data.values:
    transactions.append([str(item) for item in row if str(item) != 'nan']) # 결측치 제외 

transactions # 중첩list : [거래1[상품1, 상품2,...], 거래n[상품1, 상품2,...]]

# 3. 트랜잭션 인코딩 : 문서단어행렬(DTM) : 가중치 True/False 
te = TransactionEncoder() 
te_ary = te.fit(transactions).transform(transactions)
te_ary.shape # (9835, 169) : (트랜잭션수=9835, 아이템수=169)

# DataFrame 변환
df = pd.DataFrame(te_ary, columns=te.columns_)
df

# 4. 항목 선택(Apriori 알고리즘 이용) : 지지도(1차)=0.01 기준(이상)    
frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)



# 5. 연관 규칙 생성 : 신뢰도(2차)=0.5 기준(이상) 
rules = association_rules(frequent_itemsets, metric="confidence", 
                          min_threshold=0.5) 

print(rules) # 15개 규칙 : 지지도(1차)=0.01 & 신뢰도(2차)=0.5
'''
min_threshold=0.5 : 15개 
min_threshold=0.4 : 62개
min_threshold=0.3 : 125개 
'''
 
print("\연관 규칙 평가 메트릭 :")
final_rules = rules[['antecedents','consequents','support','confidence','lift','zhangs_metric','jaccard']]

# 칼럼명 변경 
final_rules.columns = ['lhs','rhs','support','confidence','lift','metric','jaccard']

# 지지도=0.01 & 신뢰도=0.5
print(final_rules[['lhs','rhs','lift']]) 
'''
                                       lhs                 rhs      lift
0               (other vegetables, butter)        (whole milk)  2.244885
1          (citrus fruit, root vegetables)  (other vegetables)  3.029608
2                           (yogurt, curd)        (whole milk)  2.279125
3        (other vegetables, domestic eggs)        (whole milk)  2.162336
4            (pip fruit, other vegetables)        (whole milk)  2.025351
5            (rolls/buns, root vegetables)  (other vegetables)  2.594890
6        (tropical fruit, root vegetables)  (other vegetables)  3.020999
7                (yogurt, root vegetables)  (other vegetables)  2.584078
8   (other vegetables, whipped/sour cream)        (whole milk)  1.984385
9               (other vegetables, yogurt)        (whole milk)  2.007235
10           (rolls/buns, root vegetables)        (whole milk)  2.046888
11       (tropical fruit, root vegetables)        (whole milk)  2.230969
12               (yogurt, root vegetables)        (whole milk)  2.203354
13                (tropical fruit, yogurt)        (whole milk)  2.024770
14            (yogurt, whipped/sour cream)        (whole milk)  2.052747

중심어 : rhs=(whole milk), rhs=(other vegetables)
'''



# 6. 연관 규칙 시각화
import networkx as nx # 연관 네트워크 
import matplotlib.pyplot as plt # 시긱화 


""" 연관 규칙 네트워크 그래프 """
def plot_rules(rules, weight, top_n=10): 
    rules = rules.nlargest(top_n, 'confidence') # 신뢰도 기준 상위 10개 rule 선저   
    G = nx.DiGraph() # 네트워크 그래프 

    for _, rule in rules.iterrows():
        G.add_edge(rule['lhs'], rule['rhs'], # 노드 : 타원  
                   weight=rule[weight]) # 엣지 : 가중치

    pos = nx.spring_layout(G)
    plt.figure(figsize=(15, 8))
    nx.draw_networkx(G, pos, with_labels=True, node_color="lightblue", node_size=3000, edge_color="gray")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(f"Association Rules Graph : {weight}")
    plt.show()


# 함수 호출 
plot_rules(final_rules, 'lift') # 향상도 기준(lift=1:독립, lift>1:양의상관, lift<1:음의상관) 

plot_rules(final_rules, 'metric') # lift 평가기준(-1 ~ 1) 

plot_rules(final_rules, 'jaccard') # 상품의 유사성(0 ~ 1)


# 7. 중심어 기준 subset 만들기 

## 1) 'whole milk' 중심어 기준 subset 만들기 
whole_milk = final_rules[final_rules.rhs==frozenset({'whole milk'})] 
whole_milk
len(whole_milk) # 11개 


plot_rules(whole_milk, 'lift') # 향상도 기준
plot_rules(whole_milk, 'jaccard') # 상품의 유사성
plot_rules(whole_milk, 'support') # 지지도 기준 : 함께 구매할 비율 

## 2) 'other vegetables' 중심어 기준 subset 만들기 
other_vege = final_rules[final_rules.rhs==frozenset({'other vegetables'})] 
other_vege # 4개 

plot_rules(other_vege, 'lift')



