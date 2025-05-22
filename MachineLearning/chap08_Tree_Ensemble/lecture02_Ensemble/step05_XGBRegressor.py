"""
 - XGBoost 회귀트리 예
"""

from xgboost import XGBRegressor # 회귀트리 모델 
from xgboost import plot_importance # 중요변수 시각화 
import matplotlib.pyplot as plt 

import pandas as pd # dataset
from sklearn.model_selection import train_test_split # split 
from sklearn.metrics import mean_squared_error, r2_score # 평가 

# 스케일링 도구 
from sklearn.preprocessing import minmax_scale # 정규화(0~1)
import numpy as np # 로그변환 + 난수 



### 1. dataset load & preprocessing 

path = r'C:\ITWILL\5_Python_ML\data'

# - 1978 보스턴 주택 가격에 미치는 요인을 기록한 데이터 
boston = pd.read_csv(path + '/BostonHousing.csv')
boston.info()
'''
 0   CRIM       506 non-null    float64 : 범죄율
 1   ZN         506 non-null    float64 : 25,000 평방피트를 초과 거주지역 비율
 2   INDUS      506 non-null    float64 : 비소매상업지역 면적 비율
 3   CHAS       506 non-null    int64   : 찰스강의 경계에 위치한 경우는 1, 아니면 0
 4   NOX        506 non-null    float64 : 일산화질소 농도
 5   RM         506 non-null    float64 : 주택당 방 수
 6   AGE        506 non-null    float64 : 1940년 이전에 건축된 주택의 비율
 7   DIS        506 non-null    float64 : 직업센터의 거리
 8   RAD        506 non-null    int64   : 방사형 고속도로까지의 거리 
 9   TAX        506 non-null    int64   : 재산세율
 10  PTRATIO    506 non-null    float64 : 학생/교사 비율
 11  B          506 non-null    float64 : 인구 중 흑인 비율
 12  LSTAT      506 non-null    float64 : 인구 중 하위 계층 비율
 13  MEDV       506 non-null    float64 : y변수 : 506개 타운의 주택가격(단위 1,000 달러)
 14  CAT. MEDV  506 non-null    int64   : 제외  
'''

X = boston.iloc[:, :13] # 독립변수 
X.shape # (506, 13)

y = boston.MEDV # 종속변수 
y.shape #(506,)

# x,y변수 스케일링 
X_scaled = pd.DataFrame(minmax_scale(X), columns=X.columns) # 정규화
y = np.log1p(y) # 로그변환    


###  2. train/val split
X_train, X_val, y_train, y_val = train_test_split(
    X_scaled, y, test_size=0.3)


### 3. model 생성 : 회귀트리활성함수 : 'reg:squarederror'
model = XGBRegressor(objective='reg:squarederror').fit(X=X_train, y=y_train) # objective : 활성함수
print(model)
type(model) # xgboost.sklearn.XGBRegressor

### 4. 중요변수 확인 
fscore = model.get_booster().get_fscore()

# 중요변수 시각화 : x변수명 없음 
plot_importance(model, max_num_features=13) # 13개까지 나타냄 
plt.show()

### 5. model 평가 
y_pred = model.predict(X = X_val)  # 예측치 

mse = mean_squared_error(y_val, y_pred)
print('MSE =',mse) # MSE = 0.018994471699987137

score = r2_score(y_val, y_pred)
print('r2 score =', score) # r2 score = 0.864150216488984


### 6. model save & Testing 
import pickle # binary file 

# model file save 
pickle.dump(model, open('xgb_model.pkl', mode='wb'))

# model file load 
load_model = pickle.load(open('xgb_model.pkl', mode='rb'))


# final model Test 
idx = np.random.choice(a=len(X_scaled), size=200, replace=False) # test set 만들기 

X_test, y_test = X_scaled.iloc[idx], y[idx]

y_pred = load_model.predict(X = X_test) # new test set 

score = r2_score(y_test, y_pred)
print('r2 score =', score) 



