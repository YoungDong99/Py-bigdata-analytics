"""
문1) 랜덤 시드(seed)를 설정하고, 같은 시드로 시작하여 10~50 사이의 랜덤 정수를 20개 생성하고, 
     3의 배수만 추출하여 빈도수를 출력하시오.
     
 <출력결과> 
  18    2
  36    2
  42    1  
"""

import numpy as np
import pandas as pd # pd.Series


# 1) 시드값 적용 
np.random.seed(234) # 랜덤 시드 


# 2) 10~50 사이의 랜덤 정수를 20개 생성
data = np.random.randint(low=10, high=50, size=20)


# 3) 3의 배수만 추출 
result = data[data % 3 == 0]
result  # [18, 18, 36, 42, 36]


# 4) Series 객체로 변환
ser_obj = pd.Series(result)  # numpy -> pandas 변환


# 5) 빈도수 구하기 : 힌트) value_counts() 이용 
print(ser_obj.value_counts())
'''
18    2
36    2
42    1
'''







