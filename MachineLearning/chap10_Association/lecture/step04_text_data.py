"""
자연어를 대상으로 한 연관어 분석   
"""


import pandas as pd # DataFrame 생성  
from nltk.tokenize import word_tokenize # token 생성 
from mlxtend.preprocessing import TransactionEncoder # 트랜잭션 인코딩 
from mlxtend.frequent_patterns import apriori, association_rules # 연관규칙 


# 문장(자연어)
sentences = [
    "Mr Green killed Colonel Mustard in the study with the candlestick Mr Green is not a very nice fellow",
    "Professor Plum has a green plant in his study",
    "Miss Scarlett watered Professor Plum green plant while he was away from his office last week"
]

'''
Green씨는 서재에서 머스타드 대령을 촛대로 죽였습니다. Green씨는 좋은 사람이 아닙니다.
Plum 교수는 녹색 식물을 연구중에 있습니다.
Scarlett 양은 지난 주 Plum교수가 사무실에 없는 동안 그의 녹색 식물에 물을 주었습니다.
'''

len(sentences) # 3


# 1. 문장 -> 단어벡터 생성 
transactions = [word_tokenize(row) for row in sentences] 
transactions #[문장1[단어, 단어], 문장2[단어, 단어], 문장3[단어, 단어]]


# 2. 트랜잭션 데이터 생성  
te = TransactionEncoder() 
te_ary = te.fit(transactions).transform(transactions)
te_ary.shape # (3, 33) : (문장=트랜잭션수, 단어=아이템수)

# DataFrame으로 변환
df = pd.DataFrame(te_ary, columns=te.columns_)
print(df)



# 3. 지지도=0.5 기준 아이템셋 선정 
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)
print(frequent_itemsets)


# 4. 신뢰도=0.5 기준 연관 규칙 생성
rules = association_rules(frequent_itemsets, metric="confidence", 
                          min_threshold=0.5) 

print(rules) # 지지도=0.5 & 신뢰도=0.5
len(rules) # 192

# 5. 연관 규칙 평가 메트릭 
final_rules = rules[['antecedents','consequents','support','confidence','lift','zhangs_metric','jaccard']]

# 칼럼명 변경 
final_rules.columns = ['lhs','rhs','support','confidence','lift','metric','jaccard']

# 지지도, 신뢰도, 향상도 
print(final_rules[['lhs','rhs','support','confidence','lift']])



# 6. 연관 규칙 시각화
import networkx as nx # 연관 네트워크 
import matplotlib.pyplot as plt # 시긱화 

def plot_rules(rules, weight, top_n=10): 
    """ 연관 규칙 네트워크 그래프 """
    rules = rules.nlargest(top_n, 'confidence') # 신뢰도 기준, 상위10개 rule 선택  
    G = nx.DiGraph() # 네트워크 그래프 

    for _, rule in rules.iterrows():
        G.add_edge(rule['lhs'], rule['rhs'], # 노드 : 타원  
                   weight=rule[weight]) # 엣지 : 가중치('lift','zhangs_metric','jaccard')

    pos = nx.spring_layout(G)
    plt.figure(figsize=(15, 8))
    nx.draw_networkx(G, pos, with_labels=True, node_color="lightblue", node_size=3000, edge_color="gray")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(f"Association Rules Graph : {weight}")
    plt.show()


# 함수 호출 
plot_rules(final_rules, 'lift') # 향상도 기준  

plot_rules(final_rules, 'jaccard') # 유사성 기준 



