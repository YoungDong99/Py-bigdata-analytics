'''
문3) weatherAUS.csv 파일을 시용하여 SVM 모델을 생성하시오.
  단계1> 불필요한 변수 제거 
  단계2> 결측치 확인 및 NaN 값을 가진 모든 행(row) 삭제 
  단계3> X, y변수 선택 
  단계4> y변수 레이블 인코딩 
  단계5> SVM model 생성 및 평가(classification_report) 
'''

import pandas as pd
from sklearn import model_selection
from sklearn.svm import SVC   
from sklearn.metrics import classification_report # 평가 

data = pd.read_csv('C:/ITWILL/5_Python_ML/data/weatherAUS.csv')
print(data.info())
'''
Index: 17378 entries, 0 to 36880
Data columns (total 24 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  ----- 
 0   Date           36881 non-null  object  -> 제거 
 1   Location       36881 non-null  object  -> 제거 
 2   MinTemp        36543 non-null  float64
 3   MaxTemp        36639 non-null  float64
 4   Rainfall       36255 non-null  float64
 5   Evaporation    24035 non-null  float64
 6   Sunshine       23317 non-null  float64
 7   WindGustDir    33513 non-null  object  -> 제거 
 8   WindGustSpeed  33520 non-null  float64
 9   WindDir9am     34072 non-null  object  -> 제거 
 10  WindDir3pm     35919 non-null  object  -> 제거 
 11  WindSpeed9am   35919 non-null  float64
 12  WindSpeed3pm   36235 non-null  float64
 13  Humidity9am    36311 non-null  float64
 14  Humidity3pm    36370 non-null  float64
 15  Pressure9am    33309 non-null  float64
 16  Pressure3pm    33329 non-null  float64
 17  Cloud9am       24381 non-null  float64
 18  Cloud3pm       23899 non-null  float64
 19  Temp9am        36394 non-null  float64
 20  Temp3pm        36437 non-null  float64
 21  RainToday      36255 non-null  object  -> 제거 
 22  RISK_MM        36261 non-null  float64 -> 제거 
 23  RainTomorrow   36261 non-null  object  -> y변수 
'''
 

# [단계1] 변수제거 : 구분자와 문자형 변수  
df = data.drop(['Date','Location','WindGustDir','WindDir9am','WindDir3pm','RainToday','RISK_MM'], axis = 1)
df.shape # (36881, 17)


# [단계2] 각 변수의 결측치 확인 & 결측치가 포함된 전체 행(row) 제거  
df.isnull().sum()
new_data = df.dropna() # 결측치가 포함된 전체 행(row) 제거 
new_data.shape # (17906, 17)

# [단계3] new_data에서 X, y변수 선택 
X = new_data.drop('RainTomorrow', axis = 1) # RainTomorrow 변수를 제외한 나머지 변수 
X.info() # 모두 숫자형(float)

y = new_data.RainTomorrow # RainTomorrow 변수 
y # Yes or No 

# [단계4] y변수 레이블 인코딩 
from sklearn.preprocessing import LabelEncoder # 10진수 인코딩 도구  
y = LabelEncoder().fit_transform(y = y)
y # 0 or 1


# 7:3 비율 train/test 데이터셋 구성 
X_train, X_test, y_train, y_test = model_selection.train_test_split(
            X, y, test_size=0.3, random_state=0) # seed값 


#######################################
# [단계5] SVM model 생성 및 평가 
#######################################

# 선형 SVM
svm_model = SVC(kernel='linear').fit(X=X_train, y=y_train) # 선형 svm

y_pred = svm_model.predict(X = X_test)

report = classification_report(y_test, y_pred)
print(report)
# <평가 결과 예시>
'''
              precision    recall  f1-score   support

           0       0.88      0.95      0.91      4067
           1       0.74      0.54      0.63      1147

    accuracy                           0.86      5214
   macro avg       0.81      0.74      0.77      5214
weighted avg       0.85      0.86      0.85      5214
'''

#f1-score : 정확률과 재현율의 조화평균 = 0.91 = 2 * (0.88*0.95 / (0.88+0.95)) 
#산술평균 : macro avg = 0.81 = (0.88 + 0.74) / 2
#가중평균 : weighted avg = 0.85 = (0.88*4067 + 0.74*1147) / (4067+1147)  


