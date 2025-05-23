'''
 문1) 신입사원 면접시험(interview.csv) 데이터 셋을 이용하여 다음과 같이 군집모델을 생성하시오.
 <조건1> 대상칼럼 : 가치관,전문지식,발표력,인성,창의력,자격증,종합점수 
 <조건2> 계층적 군집분석의 완전연결방식 적용 
 <조건3> 덴드로그램 시각화 : 군집 결과 확인   
'''

import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster # 계층적 군집 model
import matplotlib.pyplot as plt

# data loading - 신입사원 면접시험 데이터 셋 
interview = pd.read_csv("C:/ITWILL/5_Python_ML/data/interview.csv", encoding='ms949')
print(interview.info())
'''
RangeIndex: 15 entries, 0 to 14
Data columns (total 9 columns):
'''

# <조건1> subset 생성 : no, 합격여부 칼럼을 제외한 나머지 칼럼 
df = interview.drop(['no', '합격여부'], axis = 1) 
df.shape # (15, 7)


# <조건2> 계층적 군집분석  : 군집화 방식 = 'complete' 
clusters = linkage(y=df, method='complete', metric='euclidean')

# <조건3> 덴드로그램 시각화 : 군집 결과 확인
plt.figure(figsize=(40, 20))
dendrogram(clusters, 
           leaf_rotation=90,
           leaf_font_size=20,)
plt.show()


# <조건4> 군집 자르기 : 최대클러스터 개수 3개 지정  
result_clusters = fcluster(Z=clusters, t=3, criterion='maxclust')
result_clusters # 1 ~ 3


# <조건5> df에 cluster 칼럼 추가 & 군집별 특성 분석(그룹 통계 이용)
df['cluster'] = result_clusters

group = df.groupby('cluster')
group.size()
'''
1    5
2    5
3    5
'''

# 그룹별 특성 분석 
group.mean() # 그룹 통계 
'''
        가치관 전문지식 발표력 인성 창의력 자격증 종합점수
cluster                                         
1        11.0  15.2  19.4  11.0   6.2  0.4  62.8
2        19.0  14.4  15.6  14.8  11.8  1.0  75.6
3        14.4  18.8  10.8   9.4  18.2  0.0  71.6

그룹1 : 전반적으로 점수가 낮은 그룹(자격증 보유 or 미보유) 
그룹2 : 전반적으로 점수가 높은 그룹(자격증 보유)
그룹2 : 전반적으로 점수가 중간 그룹(자격증 미보유) 
'''

# 원형 자료에 그룹2 면접자 적용 
print(interview[df.cluster == 2])
'''
    no  가치관 전문지식 발표력 인성 창의력 자격증 종합점수 합격여부
0   101   20    15     15    15   12     1      77    합격
1   102   19    15     14    18   13     1      79    합격
3   104   18    15     15    14   13     1      75    합격
5   106   20    13     18    15   11     1      77    합격
12  113   18    14     16    12   10     1      70    합격
'''












