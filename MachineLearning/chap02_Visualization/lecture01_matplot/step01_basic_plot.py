"""
 - 기본 그래프 그리기 
"""

import matplotlib.pyplot as plt # 시각화 
import random # 난수 생성 


# 차트에서 한글과 음수 부호 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


# 1. 그래프 자료 생성 
data = range(-3, 7) # (start, stop-1)
print(data) # [-3, ... ,6]
len(data) # 10


# 2. 기본 그래프 
help(plt.plot)
'''
plot(x, y)        # plot x and y using default line style and color
plot(x, y, 'bo')  # plot x and y using blue circle markers
plot(y)           # plot y using x as index array 0..N-1
plot(y, 'r+')     # ditto, but with red plusses
'''

plt.plot(data) # 선색 : 파랑, 스타일 : 실선 
plt.title('선 색 : 파랑, 선 스타일 : 실선 ')
plt.show() # y축=data, x축=index


# 3. 색상 : 빨강, 선스타일(+)
plt.plot(data, 'r+') # y축=data, x축=index
plt.title('선 색 : 빨강, 선 스타일 : +')
plt.show()


# 4. x,y축 선스타일과 색상 & 마커(circle marker)  
data2 = [random.gauss(0, 1) for i in range(10)]  
plt.plot(data, data2, 'ro') # (x=data, y=data2)
plt.show()

'''
색상기호

b : blue
g : green
r : red
c : cyan ( 청록색 )
m : magenta ( 자홍색 )
y : yellow
k : black
w : white

스타일 기호

- 실선 ( 기본값 )
-- 이음선
-. 점 이음선
: 점선
. 점
, 픽셀
o 원
v 역삼각형
^ 정삼각형
< 좌삼각형
> 우삼각형
1 작은 역삼각형
2 작은 정삼각형
3 작은 좌삼각형
4 작은 우삼각형
s 사각형
p 오각형
* 별표
h 육각형
+ 더하기 표
D 다이아몬드 표
X 엑스 표
'''




