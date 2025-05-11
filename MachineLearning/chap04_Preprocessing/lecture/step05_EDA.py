"""
탐색적자료분석(Exploratory Data Analysis)
 - 수집 데이터를 다양한 각도에서 관찰하고 이해하는 과정
 - 그래프나 통계적 방법으로 자료를 직관적으로 파악하는 과정
 - 파생변수 생성, 독립변수와 종속변수 관계 탐색  

 예) 포루투갈의 2차교육과정에서 학생들의 음주에 영향을 미치는 요소는 무엇인가? 
"""

import pandas as pd

path = r'C:\ITWILL\5_Python_ML\data'
student = pd.read_csv(path + '/student-mat.csv')
student.info()

'''
학생들의 음주에 미치는 영향을 조사하기 위해 6가지의 변수 후보 선정
독립변수 : sex(성별), age(15~22), Pstatus(부모거주여부), failures(수업낙제횟수), famrel(가족관계), grade(G1+G2+G3 : 연간성적) 
          grade : 0~60(60점이 고득점), Alcohol : 0~500(100:매우낮음, 500:매우높음)으로 가공
종속변수 : Alcohol = (Dalc+Walc)/2*100 : 1주간 알코올 섭취정도  
'''

# 1. subset 만들기 
df = student[['sex','age','Pstatus','failures','famrel','Dalc','Walc','G1','G2','G3']]
df.info()
'''
RangeIndex: 395 entries, 0 to 394
Data columns (total 10 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   sex       395 non-null    object : 성별(F, M)
 1   age       395 non-null    int64  : 나이(15 ~ 22)
 2   Pstatus   395 non-null    object : 부모거주여부(T, A)
 3   failures  395 non-null    int64  : 수업낙제횟수(0,1,2,3)
 4   famrel    395 non-null    int64  : 가족관계(1,2,3,4,5)
 5   Dalc      395 non-null    int64  : 1일 알콜 소비량(1,2,3,4,5)   
 6   Walc      395 non-null    int64  : 1주일 알콜 소비량(1,2,3,4,5)  
 7   G1        395 non-null    int64  : 첫번째 학년(0~20)
 8   G2        395 non-null    int64  : 두번째 학년(0~20) 
 9   G3        395 non-null    int64  : 마지막 학년(0~20) 
'''

# 1. 문자형 변수의 빈도수와 숫자형 변수 통계량 확인  
df.sex.value_counts() # 문자형 변수 
df.Pstatus.value_counts() # 문자형 변수 

df.describe() # 숫자형 변수 


# 2. 파생변수 만들기 
grade = df.G1 + df.G2 + df.G3 # 성적 
grade.describe() # 4 ~ 58 

Alcohol = (df.Dalc + df.Walc) / 2 * 100 # 알콜 소비량 
Alcohol.describe() # 100 ~ 500(100:매우낮음, 500:매우높음)

# 1) 파생변수 추가 
df['grade'] = grade 
df['Alcohol'] = Alcohol

# 2) 기존 변수 제거
new_df = df.drop(['Dalc','Walc','G1','G2','G3'], axis = 1) # 칼럼 기준 제거 
new_df.info()
'''
 0   sex       395 non-null    object : x변수 
 1   age       395 non-null    int64  
 2   Pstatus   395 non-null    object 
 3   failures  395 non-null    int64  
 4   famrel    395 non-null    int64  
 5   grade     395 non-null    int64  
 6   Alcohol   395 non-null    float64 : y변수 
'''

import seaborn as sn # 시각화 도구 
import matplotlib.pyplot as plt # plt.show()


# 3. EDA : 종속변수(Alcohol) vs 독립변수 탐색 

### 연속형(y) vs 범주형(x)  : 막대차트 

# 1) Alcohol vs sex
sn.countplot(x='sex',  data=new_df) # 명목형 변수 빈도수  
plt.show()

sn.barplot(x='sex', y='Alcohol', data=new_df) # x축:범주형, y축:연속형  
plt.show()

# 2) Alcohol vs Pstatus
sn.countplot(x='Pstatus',  data=new_df) # 명목형 변수 빈도수
plt.show()

sn.barplot(x='Pstatus', y='Alcohol', data=new_df)  
plt.show()


### 연속형(y) vs 이산형(x) : 막대차트 

# 1) Alcohol vs failures
new_df.failures.value_counts()

sn.countplot(x='failures',  data=new_df) 
plt.show()

sn.barplot(x='failures', y='Alcohol', data=new_df)
plt.show()

# 2) Alcohol vs famrel
sn.barplot(x='famrel', y='Alcohol', data=new_df)
plt.show()


### 연속형(x) vs 연속형(y) : 산점도 

# 1) Alcohol vs age  
sn.scatterplot(x="age", y="Alcohol", data=new_df) 
plt.show() # y축으로 분산 

# 같은 연령대별 음주량 평균으로 시각화 
group = new_df.groupby('age')
result = group['Alcohol'].mean()  
result
'''
age
15    162.804878
16    185.576923
17    204.591837
18    198.170732
19    170.833333
20    216.666667
21    300.000000
22    500.000000
''' 
sn.scatterplot(x=result.index, y=result.values) # 행이름, 알콜평균 
plt.show()


# 2) Alcohol vs grade  
sn.scatterplot(x="grade", y="Alcohol", data=new_df) 
plt.show() # x축으로 분산


# 같은 점수대별 음주량 평균으로 시각화  
group = new_df.groupby('grade')
result = group['Alcohol'].mean()

sn.scatterplot(x=result.index, y=result.values) # 행이름, 알콜평균 
plt.show()

'''
[EDA 결과] 
남학생이 여학생에 비해서 음주량이 많고, 
낙제과목이 적고, 가족관계가 좋을 수록 음주량이 적다.
부모의 거주상태는 음주량에 큰 영향이 없다.
대체적으로 나이가 많고 점수가 낮을 수록 음주량이 증가한다.
'''


