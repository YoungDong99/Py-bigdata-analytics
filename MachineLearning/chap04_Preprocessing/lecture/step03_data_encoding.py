######################################
### 3. 데이터 인코딩 
######################################

"""
데이터 인코딩 : 머신러닝 모델에서 범주형변수를 숫자형 변수로 변환해주는 전처리 작업
 - 방법 : 레이블 인코딩(label encoding), 원-핫 인코딩(one-hot encoding)   
 - 레이블 인코딩(label encoding) : 트리계열모형(의사결정트리, 앙상블)의 변수 대상(10진수) 
 - 원-핫 인코딩(one-hot encoding) : 회귀계열모형(선형,로지스틱,SVM,신경망)의 변수 대상(2진수) 
   -> 회귀계열모형에서는 인코딩값이 가중치로 적용되므로 원-핫 인코딩으로 변환  
"""


import pandas as pd 

path = r'C:\ITWILL\5_Python_ML\data'
data = pd.read_csv(path + "/skin.csv")
data.info()
'''
RangeIndex: 30 entries, 0 to 29
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype 
---  ------       --------------  ----- 
 0   cust_no      30 non-null     int64  -> 변수 제외 : 구분자 
 1   gender       30 non-null     object -> x변수 
 2   age          30 non-null     int64 
 3   job          30 non-null     object
 4   marry        30 non-null     object
 5   car          30 non-null     object
 6   cupon_react  30 non-null     object -> y변수(쿠폰 반응) 
''' 


## 1. 변수 제거 : cust_no
df = data.drop('cust_no', axis = 1)
df.info()


### 2. 레이블 인코딩 : 트리모델 계열의 x, y변수 인코딩  
from sklearn.preprocessing import LabelEncoder # 인코딩 도구 

# 1) 쿠폰 반응 범주 확인 
df.cupon_react.unique() # array(['NO', 'YES'], dtype=object) 


# 2) 인코딩
encoder = LabelEncoder() # encoder 객체 
label = encoder.fit_transform(df['cupon_react']) # data 반영 
label # 0 or 1

# 3) 칼럼 추가 & 삭제 
df['label'] = label
new_df = df.drop('cupon_react', axis=1) 
new_df.info()

### 3. 원-핫 인코딩 : 회귀모델 계열의 x변수 인코딩  

# 1) k개 목록으로 가변수(dummy) 만들기 
df_dummy = pd.get_dummies(data=new_df, dtype='int') # object형 대상 
df_dummy 

# 2) 특정 변수 선택   
df_dummy2 = pd.get_dummies(data=new_df, columns=['label','gender','job','marry'], dtype='int')
df_dummy2.info() 
    
# 3) k-1개 목록으로 가변수 만들기  : drop_first=True(base 생략) 
df_dummy3 = pd.get_dummies(data=new_df, drop_first=True, dtype='int') # 기준변수 제외
df_dummy3  


###############################
## 가변수 기준(base) 변경하기  
###############################
# 기준(base) 변수 : 오름차순으로 결정 

import seaborn as sn 
iris = sn.load_dataset('iris')

# 1. 가변수(dummy) : k-1개 
iris_dummy = pd.get_dummies(data = iris, columns=['species'], drop_first=True, dtype='int')
# drop_first=True : 첫번째 범주 제외(기준변수)
iris_dummy.columns
# ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_versicolor', 'species_virginica']
    
    
# 2. base 기준 변경 : 범주 순서변경('virginica' -> 'versicolor' -> 'setosa') 
# object -> category 변환 
iris['species'] = iris['species'].astype('category')
iris.info()
iris['species'] = iris['species'].cat.set_categories(['virginica','versicolor','setosa'])


# 3. 가변수(dummy) : k-1개 
iris_dummy2 = pd.get_dummies(data=iris, columns=['species'], drop_first=True, dtype='int')
iris_dummy2.info()


