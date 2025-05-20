"""
 - 알려진 범주로 알려지지 않은 범주 분류 
 - 유클리드 거리계신식 이용 
"""

from sklearn.neighbors import KNeighborsClassifier # class

# 1.dataset 생성 : ppt.6 참고 
grape = [8, 5]   # 포도[단맛,아삭거림] - 과일(0)
fish = [2, 3]    # 생성[단맛,아삭거림] - 단백질(1)
carrot = [7, 10] # 당근[단맛,아삭거림] - 채소(2)
orange = [7, 3]  # 오랜지[단맛,아삭거림] - 과일(0)
celery = [3, 8]  # 셀러리[단맛,아삭거림] - 채소(2)
cheese = [1, 1]  # 치즈[단맛,아삭거림] - 단백질(1)

# x변수 : 알려진 그룹  
know = [grape,fish,carrot,orange,celery,cheese]  # 중첩 list

# y변수 : 알려진 그룹의 클래스
y_class = [0, 1, 2, 0, 2, 1]  #10진수 인코딩 

# 알려진 그룹의 클래스 이름(class name) 
class_label = ['과일', '단백질', '채소'] 
 

# 2. 분류기 
knn = KNeighborsClassifier(n_neighbors = 3) # k=3 : 홀수  
model = knn.fit(X = know, y = y_class) 

# 3. 분류기 평가 
x1 = 6 #4 # 단맛(1~10) 
X2 = 4 #8 # 아삭거림(1~10) 

# 분류대상 
unKnow = [[x1, X2]]  # 중첩 list

# class 예측 
y_pred = model.predict(X = unKnow)
print(y_pred) # [2]

print('분류결과 :', class_label[y_pred[0]]) # 1차 : 분류결과 : 채소
print('분류결과 :', class_label[y_pred[0]]) # 2차 : 분류결과 : 과일





