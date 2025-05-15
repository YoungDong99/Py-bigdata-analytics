'''  
문1) car_crashes 데이터셋을 이용하여 각 단계별로 다중선형회귀모델을 생성하시오.  
'''

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import seaborn as sn # 데이터셋 로드 

# 미국의 51개 주 자동차 사고 관련 데이터셋 
car = sn.load_dataset('car_crashes')  
car.info()
'''
 0   total           51 non-null     float64 : 치명적 충돌사고 운전자 수 
 1   speeding        51 non-null     float64 : 과속 운전자 비율 
 2   alcohol         51 non-null     float64 : 음주 운전자 비율 
 3   not_distracted  51 non-null     float64 : 주시태만이 아닌 경우 충돌에 연루된 비율  
 4   no_previous     51 non-null     float64 : 이전 사고기록 없는 경우 충돌에 연루된 비율  
 5   ins_premium     51 non-null     float64 : 자동차보험료 
 6   ins_losses      51 non-null     float64 : 보험사가 입은 손해 
 7   abbrev          51 non-null     object : 주이름 
''' 


# 단계1 : abbrev 변수 제거하여 new_df 만들기  
new_df = None 


# 단계2 : total과 비교하여 상관계수가 0.2미만의 모든 변수 제거 후 new_df에 반영  


# 단계3 : new_df에서 종속변수는 total, 나머지 변수는 독립변수  
X = None # 독립변수 
y = None # 종속변수 


# 단계4 : train/test split(70% vs 30%)
x_train, x_test, y_train, y_test = train_test_split(
          X, y, test_size=0.3)


# 단계5. 회귀모델 생성 : train set 이용 
car_model = None 


# 단계6. 모델 평가 : test set 이용  
y_pred = None # 예측치 
y_true = None # 관측치(정답)
 
# 1) MSE
mse = None 
print('MSE =', mse) 

# 2) 결정계수 
score = None    
print('결정계수 = %.5f' % score)









