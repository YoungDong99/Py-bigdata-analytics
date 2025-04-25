"""
- 이산형 : 셀수 있는 정수
- 이산형 변수 시각화 : 막대 그래프, 원 그래프 
"""
import matplotlib.pyplot as plt  

# 차트에서 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'
# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False


# 그래프 자료 생성 
data = [127, 90, 201, 150, 250] # 국가별 수출현황 
year = [2010, 2011, 2012, 2013, 2014] # 년도 


# 1. 세로막대 그래프 
plt.bar(x=year, height=data)   
plt.title('국가별 수출현황')
plt.xlabel('년도별')
plt.ylabel('수출현황(단위 : 달러)')
plt.show()


# 2. 가로막대 그래프
plt.barh(y= year, width = data, color='blue') # 색상적용  
plt.title('국가별 수출현황')
plt.xlabel('수출현황(단위 : 달러)')
plt.ylabel('년도별')
plt.show()


# 3. 누적형 세로막대 그래프
cate = ['A', 'B', 'C', 'D'] # 집단 
val1 = [15, 8, 12, 10]  # 첫 번째 데이터셋
val2 = [5, 12, 8, 15]  # 두 번째 데이터셋

plt.bar(cate, val1, label='데이터셋1', alpha=0.5)    # alpha : 투명도(0~1)
plt.bar(cate, val2, bottom=val1, label='데이터셋2', alpha=0.8)
plt.title('누적형 막대 그래프')
plt.xlabel('카테고리')
plt.ylabel('값')
plt.legend()  # 범례 추가
plt.show()



# 4. 원 그래프

# 1) 레이블 적용  
labels = ['싱가폴','태국','한국','일본','미국'] 

plt.pie(x = data, labels = labels)
plt.show()

# 2) 비율 적용 
data_ratio = [ round((d / sum(data))*100, 2) for d in data] # 비율 계산 

plt.pie(x = data, labels = data_ratio)
plt.show()


# 레이블 만들기 : 국가명 + 비율
new_labels = []

for i in range(len(data)):
    new_labels.append(labels[i] + '\n' + str(data_ratio[i]))

print(new_labels)



plt.pie(x = data, labels = new_labels)
plt.show()


