'''
문2) wdbc_data.csv 파일을 읽어와서 단계별로 x, y 변수를 생성하시오.
     <단계1> 파일 가져오기, 정보 확인 
     <단계2> x, y변수 선택 : 
             y변수 : diagnosis 
             x변수 : id 칼럼 제외 나머지 30개 칼럼
     <단계3> y변수의 범주('B', 'M')를 기준으로 서브셋 만들기
            B_tumor = 'B'범주를 갖는 서브셋 
            M_tumor = 'M'범주를 갖는 서브셋             
'''
import pandas as pd

path = r"c:/ITWILL/5_Python_ML/data" # file 경로 변경 

# <단계1> 파일 가져오기, 정보 확인 
wdbc = pd.read_csv(path + "/wdbc_data.csv", encoding='utf-8')
wdbc.shape
wdbc.info()


# 전체 변수 가져오기
names = list(wdbc.columns)
print(names)


# <단계2> y변수, x변수 선택
y = wdbc.diagnosis # diagnosis 칼럼 
x = list(wdbc.columns.drop(['id'])) # id 칼럼 제외 나머지 30개 칼럼

print(x)

# <단계3> y변수의 범주('B', 'M')를 기준으로 서브셋 만들기
print(y.unique())

B_tumor = wdbc[y == 'B']
M_tumor = wdbc[y == 'M'] 

B_tumor.shape  # (357, 32)
M_tumor.shape  # (212, 32)

