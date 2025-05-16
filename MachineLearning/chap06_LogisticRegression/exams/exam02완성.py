'''
문2) wine 데이터셋을 이용하여 조건에 맞게 단계별로 로지스틱회귀모델(다항분류)을 생성하시오. 
  조건1> train/test - 70:30비율
  조건2> y 변수 : wine.target 
  조건3> x 변수 : wine.data
  조건4> 모델 평가 : confusion_matrix, 분류정확도[accuracy]
'''

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics # 평가도구 

# 단계1. wine 데이터셋 로드 
wine = load_wine()

# 단계2. x, y변수 선택 
wine_x = wine.data # x변수 
wine_x.shape # (178, 13)
wine_y = wine.target # y변수(0~2) : multi class
 

# 단계3. train/test split(70:30)
X_train, X_test, y_train, y_test = train_test_split(wine_x, wine_y, 
                 test_size=0.3, random_state=123)

# 단계4. model 생성  : solver='lbfgs', multi_class='multinomial'
lg = LogisticRegression(penalty='l2', C=1.0, 
                   solver='lbfgs', max_iter=100,
                   multi_class='multinomial') # 빈 model 

model = lg.fit(X = X_train, y = y_train) # model 학습 

# 단계5. 모델 평가 : accuracy, confusion matrix
y_pred = model.predict(X = X_test) # y예측치 : class예측 
y_pred[:10] # [2, 1, 2, 1, 1, 2, 0, 2, 2, 1]

y_true = y_test # y정답 
y_true[:10] # [2, 1, 2, 1, 1, 2, 0, 2, 2, 1]

acc = metrics.accuracy_score(y_true=y_true, y_pred=y_pred)
print('Accuracy =', acc) # Accuracy = 0.9629629629629629

con_mat = metrics.confusion_matrix(y_true, y_pred)
print(con_mat)
'''
[[13  1  0]   -> class=0 : 1개 오분류 
 [ 0 18  0]   -> class=1 : 없음 
 [ 0  1 21]]  -> class=2 : 1개 오분류  
'''


# 단계6. test으로 y를 확률 예측하고, 첫번째 칼럼은 y정답, 두번째 칼럼은 class=2의 예측치 출력
y_proba = model.predict_proba(X = X_test) # 확률 예측 
y_proba.shape # (54, 3) : 각 class별 확률 예측 
print(y_proba)
'''
      y=0 확률       y=1 확률         y=2 확률 
[[3.62740893e-02 2.48445840e-02 9.38881327e-01]
 [1.38757832e-01 7.77203520e-01 8.40386487e-02]
 [1.31092293e-02 2.73792778e-02 9.59511493e-01]
 [1.92987375e-02 9.60265937e-01 2.04353252e-02]
 [2.83509620e-03 9.96817342e-01 3.47561996e-04]
 [4.96638020e-04 3.47283329e-06 9.99499889e-01]
     :
''' 

# 힌트) DataFrame 이용
import pandas as pd 

result = pd.DataFrame({'y정답':y_true, 'y예측치' : y_proba[:,2]}) 
print(result)
'''
    y정답   y예측치
0     2  0.938881
1     1  0.084039
2     2  0.959511
3     1  0.020436
4     1  0.000348
5     2  0.999500
6     0  0.002243
7     2  0.843381
8     2  0.999861
9     1  0.000006
10    2  0.996617
11    2  0.800700
12    2  0.999426
13    0  0.011226
14    0  0.001098
15    2  0.922597
16    1  0.000036
17    1  0.000042
18    0  0.000350
19    1  0.000081
20    2  0.553277
21    2  0.993744
22    2  0.999964
23    2  0.945606
24    1  0.000069
25    2  0.999076
26    2  0.990768
27    1  0.016764
28    0  0.002620
29    0  0.000119
30    0  0.001305
31    0  0.003751
32    2  0.768174
33    1  0.001337
34    2  0.999338
35    1  0.000854
36    2  0.242703  -> 오분류 
37    0  0.001172
38    1  0.000218
39    1  0.000011
40    2  0.996522
41    2  0.950417
42    0  0.013530
43    0  0.017343
44    1  0.000915
45    0  0.002751
46    0  0.000082
47    1  0.002482
48    0  0.000569
49    1  0.006655
50    1  0.000080
51    2  0.605582
52    2  0.993588
53    1  0.000028
'''