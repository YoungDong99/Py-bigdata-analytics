''' 
문1) score.csv 파일을 읽어와서 다음과 같은 단계로 처리하시오.
   <단계1> tv 칼럼이 0인 관측치 2개 삭제 (조건식 이용)
   <단계2> score, academy 칼럼만 추출하여 DataFrame 생성
   <단계3> score, academy 칼럼의 평균 계산 : <<출력 결과 >> 참고 
       
   
<<출력 결과 >>
score      76.500
academy     1.625   
'''

import pandas as pd

path = r"c:\ITWILL\5_Python_ML\data" # file 경로 변경 

score = pd.read_csv(path + '/score.csv')
print(score.info())
print(score)


# <단계1> tv 칼럼이 0인 관측치 2개 삭제
new_df = score[score.tv != 0] 

new_df.shape # 차원 확인 (8, 6)


# <단계2> score, academy 칼럼만 추출하여 DataFrame 생성
new_df2 = new_df[['score', 'academy']]

new_df2.shape # 차원 확인 (8, 2)


# <단계3> new_df2 이용 score, academy의 평균 계산  
print('score =', new_df2.score.mean())
print('academy =',new_df2.academy.mean())
'''
score = 76.5
academy = 1.625
'''


