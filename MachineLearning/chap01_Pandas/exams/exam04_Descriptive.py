'''  
lecture01 > step03 관련문제

문5) tips.csv 파일을 읽어와서 다음과 같이 처리하시오.
   <단계1> 파일 정보 보기 
   <단계2> header를 포함한 앞부분 5개 관측치 보기 
   <단계3> header를 포함한 뒷부분 5개 관측치 보기 
   <단계4> 숫자 칼럼 대상 요약통계량 보기 
   <단계5> 흡연자(smoker) 유무 빈도수 계산  
   <단계6> 요일(day) 칼럼의 유일한 값 출력 
'''

import pandas as pd

path = r"c:\ITWILL\5_Python_ML\data" # file 경로 변경

tips = pd.read_csv(path + '/tips.csv')

# <단계1> 파일 정보 보기
tips.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 7 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   total_bill  244 non-null    float64
 1   tip         244 non-null    float64
 2   sex         244 non-null    object 
 3   smoker      244 non-null    object 
 4   day         244 non-null    object 
 5   time        244 non-null    object 
 6   size        244 non-null    int64  
'''

# <단계2> header를 포함한 앞부분 5개 관측치 보기 
tips.head()

# <단계3> header를 포함한 뒷부분 5개 관측치 보기 
tips.tail()

# <단계4> 숫자 칼럼 대상 요약통계량 보기 
tips.describe()

# <단계5> 흡연자(smoker) 유무 빈도수 계산  
tips['smoker'].value_counts()

# <단계6> 요일(day) 칼럼의 유일한 값 출력 
tips.day.value_counts()

