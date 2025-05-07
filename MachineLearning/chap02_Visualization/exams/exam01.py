'''
lecture01

문1) iris.csv 파일을 이용하여 다음과 같은 단계로 차트를 그리시오.
    <단계1> 5번 칼럼을 대상으로 레이블 인코딩 
    <단계2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후 인코딩된 칼럼으로 색상 적용
           힌트) plt.scatter(x, y, c) 
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder # 레이블 인코딩 

# iris.csv 파일 읽기 
path = r'C:\ITWILL\5_Python_ML\data'
iris = pd.read_csv(path + '/iris.csv')

print(iris.info())
'''
 0   Sepal.Length  150 non-null    float64 - 1번 칼럼
 1   Sepal.Width   150 non-null    float64
 2   Petal.Length  150 non-null    float64 - 3번 칼럼
 3   Petal.Width   150 non-null    float64
 4   Species       150 non-null    object - 5번 칼럼
'''

# <단계1> 5번 칼럼을 대상으로 레이블 인코딩 후 iris에 칼럼 추가 
iris['Species2'] = LabelEncoder().fit_transform(iris.Species)

print(iris.info())
'''
---  ------        --------------  -----  
 0   Sepal.Length  150 non-null    float64
 1   Sepal.Width   150 non-null    float64
 2   Petal.Length  150 non-null    float64
 3   Petal.Width   150 non-null    float64
 4   Species       150 non-null    object  - 원형 칼럼 
 5   Species2      150 non-null    int32   - 인코딩 칼럼 
'''

iris.Species.value_counts()
'''
setosa        50
versicolor    50
virginica     50
'''
 
iris.Species2.value_counts()
'''
0    50
1    50
2    50
'''

# <단계2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후 인코딩된 칼럼으로 색상 적용
plt.scatter(x=iris['Sepal.Length'], y=iris['Petal.Length'], c=iris['Species2']) 
plt.show()






