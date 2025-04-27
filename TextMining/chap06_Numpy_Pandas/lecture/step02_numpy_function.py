"""
2. 유니버설 함수  
 - 다차원 배열의 원소를 대상으로 수학/통계 등의 연산을 수행하는 함수
"""

import numpy as np # 별칭 


# 1) numpy 제공 함수 
data = np.random.randn(5) # 1차원 난수 배열 (-3 ~ +3)

print(data)  # [ 0.01660729 -0.24513628  0.28321677  1.23916555 -2.36510931]

# 별칭.함수()
print(np.abs(data)) # 절대값
print(np.sqrt(data)) # 제곱근 > 음수는 nan
print(np.square(data)) # 제곱 
print(np.sign(data)) # 부호 
print(np.var(data)) # 분산
print(np.std(data)) # 표준편차
                

# 2) numpy 객체 메서드 
data2 = np.random.randint(1, 10, size=(3, 4)) # 2차원 난수 배열

print(data2)
'''
[[6 5 6 3]
 [6 8 4 6]
 [6 4 7 2]]
'''

# 객체.함수()
dir(data2)  # sqrt, square 지원X

print('합계=', data2.sum()) # 합계
print('평균=', data2.mean()) # 평균
print('표준편차=', data2.std()) # 표준편차
print('최댓값=', data2.max()) # 최댓값
print('최솟값=', data2.min()) # 최솟값


# 3. axis 속성 
print(data2.sum())  # 전체 원소 합계 : 63
print(data2.sum(axis=0)) # 행축 기준 : [18 17 17 11]
print(data2.sum(axis=1)) # 열축 기준 : [20 24 19]

# 축(axis) 이해
data2.shape # (3, 4) : 3행 4열
data2.sum(axis=0) # 행축 기준 : 0번째는 3(행)
data2.sum(axis=1) # 열축 기준 : 1번째는 4(열)




