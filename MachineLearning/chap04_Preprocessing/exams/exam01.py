# 문1) planets 자료를 이용하여 다음과 같은 단계로 결측치를 처리하시오.


import seaborn as sn # 별칭

# 데이터셋 로드
planets = sn.load_dataset('planets')
planets.info()
'''
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   method          1035 non-null   object 
 1   number          1035 non-null   int64  
 2   orbital_period  992 non-null    float64
 3   mass            513 non-null    float64
 4   distance        808 non-null    float64
 5   year            1035 non-null   int64 
'''
 

# 단계1. 각 변수의 결측치를 확인하고, 결측치 비율이 50% 이상인 칼럼을 찾아서 제거 후 new_df 만들기 


# 단계2. orbital_period 칼럼 기준으로 결측치 제거하여 new_df 현재 객체 반영하기


# 단계3. new_df의 distance 칼럼의 결측치를 0으로 대체하여 현재 객체 반영하기


# 단계4. distance 칼럼에 0으로 대체된 관측치 출력하기   











