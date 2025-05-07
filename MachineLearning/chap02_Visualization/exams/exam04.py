'''
lecture03

문4) seaborn의  titanic 데이터셋을 이용하여 다음과 같이 단계별로 시각화하시오.
  <단계1> 'survived','pclass', 'age','fare' 칼럼으로 서브셋 만들기
  <단계2> 'survived' 칼럼을 범주형 변수로 하여 'pclass', 'age','fare' 칼럼 간의 산점도행렬 시각화
'''

import matplotlib.pyplot as plt
import seaborn as sn


titanic = sn.load_dataset('titanic')
print(titanic.info())
'''
 0   survived     891 non-null    int64   : 생존여부(0 or 1)
 1   pclass       891 non-null    int64   : 선실등급(1등석 ~ 3등석)
 2   sex          891 non-null    object   
 3   age          714 non-null    float64 : 나이 
 4   sibsp        891 non-null    int64    
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 : 요금 
'''


#  <단계1> 'survived','pclass', 'age','fare' 칼럼으로 서브셋 만들기  
titanic_df = titanic[['survived','pclass', 'age','fare']]
titanic_df


# <단계2> 'survived' 칼럼을 집단변수로 하여 'pclass', 'age','fare' 칼럼 간의 산점도 행렬 시각화
sn.pairplot(data=titanic_df, hue='survived')
plt.show()


# <단계3> 산점도행렬의 시각화 결과를 아래 변수 기준으로 해설하기
'''
pclass : 3등석 탑승자가 사망비율이 매우 높다.
age : 생존과 사망 모두 중간 연령층이 높다. 
fare : 낮은 요금 탑승자가 사망비율이 높다.
pclass vs age : 대체적으로 1등석 탑승자와 나이가 어릴수록 생존율이 높다.
pclass vs fare : 대체적으로 1등석이고 요금이 높을 수록 생존율이 높다.    
age vs fare :  대체적으로 요금이 높을 수록 생존율이 높다.(나이는 영향 없음)
'''


