'''
문1) 그리프 자료를 이용하여 다음 조건에 맞게 각 그래프를 그리시오.
    <조건1> 막대 그리프 그리기 : categories, values, colors 변수 이용 
    <조건2> 원 그래프 그리기 : values, colors 변수 이용 
    <조건3> 누적형 가로막대 그래프 그리기 : categories, values, values2, colors 변수 이용
    
    <시각화 결과> exam01.pdf 참고  
'''

import matplotlib.pyplot as plt

# 그래프 자료 
categories = ['A', 'B', 'C', 'D']
values = [15, 8, 12, 9]
values2 = [4, 12, 5, 7]
colors = ['blue', 'green', 'red', 'purple']  # 막대의 색상 리스트

# <조건1> 막대 그래프 그리기 
plt.bar(x = categories, height = values, color = colors)
plt.title('막대그래프')
plt.xlabel('카테고리')
plt.ylabel('값')
plt.show()

# <조건2> 원 그래프 그리기 
plt.pie(x = values, labels = colors, colors = colors)
plt.title('원 그래프')
plt.show()

# <조건3> 누적형 가로막대 그래프 그리기 
plt.bar(categories, values, label='데이터셋1',color = 'red', alpha=0.3)
plt.bar(categories, values2, bottom=values, label='데이터셋2', alpha=0.8)
plt.title('누적형 막대 그래프')
plt.xlabel('카테고리')
plt.ylabel('값')
plt.legend()
plt.show()


