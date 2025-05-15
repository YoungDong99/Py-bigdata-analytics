# -*- coding: utf-8 -*-
"""
문3) california 주택가격을 대상으로 다음과 같은 단계별로 선형회귀모델을 작성하시오.
"""


from sklearn.datasets import fetch_california_housing # dataset load
from sklearn.linear_model import LinearRegression  # model
from sklearn.model_selection import train_test_split # dataset split

from sklearn.preprocessing import scale # 표준화(mu=0, st=1)  
import numpy as np # 로그변환 : np.log1p()  

# 캘리포니아 주택 가격 dataset load 
california = fetch_california_housing()
print(california.DESCR)


# 단계1 : 특징변수(8개)와 타켓변수(MEDV) 선택  
X = california.data
y = california.target


# 단계2 : 데이터 스케일링 : X변수(표준화), y변수(로그변화)   


# 단계3 : 75%(train) vs 25(test) 비율 데이터셋 split : seed값 적용 


# 단계4 : 회귀모델 생성


# 단계5 : train과 test score 확인  



  
