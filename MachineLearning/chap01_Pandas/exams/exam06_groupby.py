"""
lecture02 > step04 관련문제

문6) titanic 데이터셋을 대상으로 아래와 같이 단계별로 처리하시오. 
"""

import seaborn as sns 

titanic = sns.load_dataset('titanic') # seaborn 데이터셋 제공   
titanic.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   survived     891 non-null    int64   
 1   pclass       891 non-null    int64   
 2   sex          891 non-null    object  
 3   age          714 non-null    float64 
 4   sibsp        891 non-null    int64   
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 
 7   embarked     889 non-null    object  
 8   class        891 non-null    category
 9   who          891 non-null    object  
 10  adult_male   891 non-null    bool    
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object  
 13  alive        891 non-null    object  
 14  alone        891 non-null    bool    
'''
 

# 단계1 : age, sex, class, fare, survived 칼럼으로 서브셋 생성 
df = titanic[['age', 'sex', 'class', 'fare', 'survived']]
df.info()
'''
 0   age       714 non-null    float64 
 1   sex       891 non-null    object    : 범주형(2개) 
 2   class     891 non-null    category  : 범주형(3개)
 3   fare      891 non-null    float64 
 4   survived  891 non-null    int64 
'''
 
df['class'].unique() # ['Third', 'First', 'Second']

# 단계2 : class와 sex 칼럼 기준으로 그룹 객체 생성 및 크기 확인 
group = df.groupby(['class', 'sex'])
group.size()
'''
1차      2차 
class   sex       빈도수 
First   female     94
        male      122
Second  female     76
        male      108
Third   female    144
        male      347
'''
        
# 단계3 : 그룹별 평균 구하기 
group_mean = group.mean()
print(group_mean)
'''
                     age        fare  survived
class  sex                                    
First  female  34.611765  106.125798  0.968085
       male    41.281386   67.226127  0.368852
Second female  28.722973   21.970121  0.921053
       male    30.740707   19.741782  0.157407
Third  female  21.750000   16.118810  0.500000
       male    26.507589   12.661633  0.135447
'''
 
# 특정 칼럼(survived) 선택 
group_mean['survived']
      
# 단계4 : 그룹별 평균에서 survived 칼럼 기준 막대차트 시각화  
import matplotlib.pyplot as plt 

group_mean['survived'].plot(kind = 'bar')
plt.show()
# [해설] class가 First, Second이고, sex는 female인 경우 생존율 높음 



