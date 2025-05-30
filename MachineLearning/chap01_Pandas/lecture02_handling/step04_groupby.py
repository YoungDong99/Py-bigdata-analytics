"""
- 범주형 변수를 이용한 자료처리 

1. 범주형 변수 이용 subset 만들기 
2. 범주형 변수 이용 그룹 & 통계량 
3. apply() 함수 : DataFrame 객체에 외부함수 적용
4. map()함수 : Series 객체에 외부함수 적용 
"""

import pandas as pd 

 
path = r'C:\ITWILL\5_Python_ML\data'

# dataset load & 변수 확인
wine = pd.read_csv(path  + '/winequality-both.csv')
print(wine.info())
'''
RangeIndex: 6497 entries, 0 to 6496
Data columns (total 13 columns):
0   type                  6497 non-null   object : 집단변수(red, white)    
 :
12  quality               6497 non-null   int64 : 와인품질 
'''    

#wine.fixed acidity
wine['fixed acidity']

# 칼럼 공백 -> '_' 교체 
wine.columns = wine.columns.str.replace(' ', '_')
wine.head()
print(wine.info())


# 5개 변수 선택 : subset 만들기 
wine_df = wine.iloc[:, [0,1,4,11,12]] # 위치 기반
print(wine_df.info()) 

# 특정 칼럼명 수정 
columns = {'fixed_acidity':'acidity', 'residual_sugar':'sugar'} # {'old','new'} 
wine_df = wine_df.rename(columns = columns) 
wine_df.info()
    
# 집단변수 확인 : 와인유형   
print(wine_df.type.unique()) # ['red' 'white'] : 범주형변수 
print(wine_df.type.nunique()) # 2

# 이산변수 확인 : 와인 품질    
print(wine_df.quality.unique()) # [5 6 7 4 8 3 9] : 이산형변수(범주형변수) 
print(wine_df.quality.value_counts())


# 1. 범주형 변수 기준 subset 만들기 

# 1) 1개 집단 기준  
red_wine = wine_df[wine['type']=='red']  # [조건식]
red_wine.shape # (1599, 5)

white_wine = wine_df[wine['type']=='white']
white_wine.shape # (4898, 5)

# 2) 2개 이상 집단 기준 : type[red, white, blue] 가정 
two_wine_type = wine_df[wine_df['type'].isin(['red','white'])] 

two_wine_type.type.value_counts()
'''
white    4898
red      1599
'''


# 3) 범주형 변수 기준 특정 칼럼 선택 : 1차원 구조
red_wine_quality = wine.loc[wine['type']=='red', 'quality']  # red 품질 
white_wine_quality = wine.loc[wine['type']=='white', 'quality'] # white 품질 
red_wine_quality.shape # (1599,)
white_wine_quality.shape # (4898,)


# 2. 범주형 변수 기준 group & 통계량

# 1) 범주형변수 1개 이용 그룹화 
type_group = wine_df.groupby('type') # DF.groupby('칼럼명')

# 각 집단별 빈도수 
type_group.size()  
'''
red      1599
white    4898
'''

# 그룹객체에서 그룹 추출 
red_df = type_group.get_group('red')
white_df = type_group.get_group('white')

    
# 그룹별 통계량 
print(type_group.sum()) # 그룹별 합계 
print(type_group.mean()) # 그룹별 평균(대표값)
'''
        acidity     sugar    alcohol   quality
type                                          
red    8.319637  2.538806  10.422983  5.636023
white  6.854788  6.391415  10.514267  5.877909
'''


# 2) 집단변수 2개 이용 : 나머지 변수(3개)가 그룹 대상 
wine_group = wine_df.groupby(['type','quality']) # 2개 x 7개 = 최대 14  

# 각 집단별 빈도수
wine_group.size()
'''
1차  -> 2차 
type   quality     빈도수 
red    3            10
       4            53
       5           681
       6           638
       7           199
       8            18
white  3            20
       4           163
       5          1457
       6          2198
       7           880
       8           175
       9             5
'''
       
# 그룹 통계 시각화 
grp_mean = wine_group.mean() # 그룹별 평균 
grp_mean

type(grp_mean) # pandas.core.frame.DataFrame

import matplotlib.pyplot as plt 

grp_mean.plot(kind = 'bar') # DF.plot(kind='유형')
plt.show()


# 3. apply() 함수 
'''
DF객체.apply(함수명)
'''
# 1) 사용자 함수 : 0 ~ 1 사이 정규화 
def normal_df(x):
    nor = ( x - min(x) ) / ( max(x) - min(x) )
    return nor


# 2) 2차원 data 준비 : wine 데이터 적용 
wine_x = wine_df.iloc[:, 1:] # 숫자변수만 선택 

wine_x # [6497 rows x 4 columns]

# 함수호출(DF)
# normal_df(wine_x) : 오류 


# 3) apply 함수 적용 : 열(칼럼) 단위로 실인수 전달   
wine_nor = wine_x.apply(normal_df) 
print(wine_nor.describe()) # 정규화 확인 


# 4. map() 함수   
'''
Series객체.map(함수명)
'''

# 1) 인코딩 함수 
def encoding_df(x):
    encoding = {'red':[1,0], 'white':[0,1]}
    return encoding[x]

# 2) 1차원 data 준비 
wine_type = wine_df['type'] # 와인유형 


# 3) map 함수 적용 
label = wine_type.map(encoding_df)
label


