"""
Seaborn : Matplotlib 기반 다양한 배경 테마, 통계용 차트 제공 
커널 밀도(kernel density), 카운트 플롯, 다차원 실수형 데이터,2차원 카테고리 데이터
2차원 복합 데이터(box-plot), heatmap, catplot 
"""

import seaborn as sn # 별칭 

# 1. 데이터셋 확인 
names = sn.get_dataset_names()
print(names)


# 2. 데이터셋 로드 
iris = sn.load_dataset('iris') # 붖꽃 
type(iris) # pandas.core.frame.DataFram
print(iris.info())
'''
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object 
'''



tips = sn.load_dataset('tips') # 행사팁  
print(tips.info())



titanic = sn.load_dataset('titanic') # 타이타닉 
print(titanic.info())



flights = sn.load_dataset('flights') # 비행탑승객수  
print(flights.info())



