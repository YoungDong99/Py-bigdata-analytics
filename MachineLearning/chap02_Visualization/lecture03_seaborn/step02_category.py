"""
1. Object vs Category 
  - object : 문자열 순서 변경 불가 
  - category : 문자열 순서 변경 가능 
2. 범주형 자료 시각화 
"""

import matplotlib.pyplot as plt
import seaborn as sn


# 1. Object vs Category 

# dataset load
titanic = sn.load_dataset('titanic')

print(titanic.info())

# subset 만들기 
df = titanic[['survived','age','class','who']]
df.info()
'''
 0   survived  891 non-null    int64   
 1   age       714 non-null    float64 
 2   class     891 non-null    category : 문자형(순서변경 가능)
 3   who       891 non-null    object   : 문자형(순서변경 불가)
'''
df.head()
'''
   survived   age  class    who
0         0  22.0  Third    man
1         1  38.0  First  woman
2         1  26.0  Third  woman
3         1  35.0  First  woman
4         0  35.0  Third    man
'''

df['class'].unique() # ['First', 'Second', 'Third']
df['who'].unique() # ['man', 'woman', 'child']

'''
DF.sort_index() : 색인 정렬 
DF.sort_values(by=칼럼) : 칼럼으로 정렬 
'''

# category형 정렬 
df.sort_values(by = 'class') # category 오름차순
# First > Second > Third

# object형 정렬 
df.sort_values(by = 'who') # object 오름차순 
# child > man > woman


# category형 변수 순서 변경 
df['class_new'] = df['class'].cat.set_categories(['Third', 'Second', 'First'])
# Third > Second > First   

df.info()

df.sort_values(by = 'class_new')
# 정렬순서 : Third > Second > First   


# 2. 범주형 자료 시각화 

# 1) 배경 스타일 
sn.set_style(style='darkgrid')
tips = sn.load_dataset('tips')
print(tips.info())

tips.smoker.value_counts()
'''
No     151
Yes     93
'''

# 2) category형 자료 시각화 : 빈도수 + 막대차트 

# 흡연유무 : 2개 
sn.countplot(x = 'smoker', data = tips) 
plt.title('smoker of tips')
plt.show()

# 행사요일 : 4개 범주 
sn.countplot(x = 'day', data = tips) 
plt.title('smoker of tips')
plt.show()



