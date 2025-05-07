"""
Pandas 객체 시각화 : 연속형 변수 시각화  
 - hist, kde, scatter, box 등 
"""

import pandas as pd
import numpy as np # dataset 
import matplotlib.pyplot as plt # chart

# file 경로 
path = r'C:\ITWILL\5_Python_ML\data'

# 1. 산점도 
dataset = pd.read_csv(path + '/dataset.csv')
print(dataset.info())

# 연속형 변수 
plt.scatter(dataset['age'], dataset['price'], c=dataset['gender'])
plt.show()


# 2. hist, kde, box
# DataFrame 객체 
df = pd.DataFrame(np.random.randn(100, 4),
               columns=('one','two','three','fore'))

# 1) 히스토그램
df['one'].plot(kind = 'hist', title = 'histogram')
plt.show()

# 2) 커널밀도추정 
df['one'].plot(kind = 'kde', title='kernel density plot')
plt.show()

# 3) 박스플롯
df.plot(kind='box', title='boxplot chart')
plt.show()


# 3. 산점도 행렬 
from pandas.plotting import scatter_matrix

# 3) iris.csv
iris = pd.read_csv(path + '/iris.csv')
cols = list(iris.columns)

x = iris[cols[:4]] 

# 산점도 matrix 
scatter_matrix(x)
plt.show()


