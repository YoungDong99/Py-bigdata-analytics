'''
lecture02

문2) dataset.csv 파일을 이용하여 다음과 같은 단계로 교차테이블과 누적막대차트를 그리시오.
  <단계1> 교차테이블 결과를 대상으로 만족도 1,3,5만 선택하여  subset 만들기   
  <단계2> 생성된 데이터프레임 대상 칼럼명 수정 : ['seoul','incheon','busan']
  <단계3> 생성된 데이터프레임 대상  index 수정 : ['male', 'female']     
  <단계4> 생성된 데이터프레임 대상 누적가로막대차트 그리기
'''

import pandas as pd
import matplotlib.pyplot as plt

path = r'C:\ITWILL\5_Python_ML\data'
dataset = pd.read_csv(path + '/dataset.csv')
dataset.info()


# 성별(gender)과 만족도(survey) 칼럼으로 교차테이블  작성 
table =  pd.crosstab(index=dataset['gender'], columns=dataset['survey'])
table
'''
survey   1   2   3   4  5
gender                   
1       10  51  44  13  5
2        4  36  42  11  1
'''

# <단계1> 교차테이블(table)를 대상으로 만족도 1,3,5만 선택하여 subset 만들기    
table_sub = table.loc[:, [1,3,5]]
table_sub
'''
survey   1   3  5
gender           
1       10  44  5
2        4  42  1
'''

# <단계2> 생성된 데이터프레임 대상 칼럼명 수정 : ['seoul','incheon','busan'] 
# 힌트) DF.columns 속성 이용 
table_sub.columns = ['seoul','incheon','busan']

# <단계3> 생성된 데이터프레임 대상  index 수정 : ['male', 'female']     
# 힌트) DF.index 속성 이용 
table_sub.index = ['male', 'female'] 

print(table_sub)
'''
        seoul  incheon  busan
male       10       44      5
female      4       42      1
'''

# <단계4> 생성된 데이터프레임 대상 누적가로막대차트 그리기
# 힌트) DF.plot(kind='barh', stacked = True)
table_sub.plot(kind='barh', stacked = True)
plt.show()



