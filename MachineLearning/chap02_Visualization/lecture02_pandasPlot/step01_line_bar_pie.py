"""
Pandas 객체 시각화 : 이산형 변수 시각화

  형식) obj.plot(kind='차트유형', 속성)  

  obj : Series(1차), DataFrame(2차)
  kind : bar, barh, pie, scatter 등 
  속성 : 제목, 축이름 등 
"""

import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt 

# 1. 기본 차트 시각화 

# 1) Series 객체 시각화 
ser = pd.Series(np.random.randn(10),
          index = np.arange(0, 100, 10))

ser.plot() # 선 그래프 
plt.show()

# 2) DataFrame 객체 시각화
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one','two','three','fore'])


# 기본 차트 : 선 그래프 
df.plot()  
plt.show()

# 막대차트 
df.plot(kind = 'bar', title='bar chart')
plt.show()


# 2. dataset 이용 
path = r'C:\ITWILL\5_Python_ML\data'

tips = pd.read_csv(path + '/tips.csv')
tips.info()


# 행사 요일별 : 파이 차트 
cnt = tips['day'].value_counts()
cnt.plot(kind = 'pie')
plt.show()


# 요일(day) vs 규모(size) : 교차분할표 
table = pd.crosstab(index=tips['day'], columns=tips['size'])

table
'''
size  1   2   3   4  5  6
day                      
Fri   1  16   1   1  0  0
Sat   2  53  18  13  1  0
Sun   0  39  15  18  3  1
Thur  1  48   4   5  1  3
'''
table.columns  # 열 : [1, 2, 3, 4, 5, 6]
table.index  # 행 : ['Fri', 'Sat', 'Sun', 'Thur']

# 2~5열 선택
table = table.loc[:, 2:5]


# 누적막대그래프 
table.plot(kind='barh', stacked=True,
               title = 'day va size plotting')
# stacked=True : 누적형 
plt.show()


