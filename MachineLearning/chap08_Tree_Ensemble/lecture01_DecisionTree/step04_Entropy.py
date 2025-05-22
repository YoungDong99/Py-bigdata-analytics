"""
지니불순도(Gini-impurity), 엔트로피(Entropy)
  - Tree model에서 중요변수 선정 기준
 - 확률 변수 간의 불확실성을 나타내는 수치
 - 작을 수록 불확실성이 낮다.

  지니불순도와 엔트로피 수식  
 Gini-impurity = sum(p * (1-p))
 Entropy = -sum(p * log(p))

  지니계수와 정보이득  
  gini_index = base - Gini-impurity 
  info_gain = base - Entropy
"""

import numpy as np

# 1. 불확실성이 큰 경우(x:앞면, y:뒷면)
x, y = 0.5, 0.5 

gini = sum([x * (1-x), y * (1-y)])
print(gini) # 0.5

entropy = -sum([x * np.log2(x), y * np.log2(y)])
print(entropy) # 1.0


# 2. 불확실성이 작은 경우(x:앞면, y:뒷면)
x, y = 0.9, 0.1 

gini2 = sum([x * (1-x), y * (1-y)])
print(gini2) # 0.18

entropy2 = -sum([x * np.log2(x), y * np.log2(y)])
print(entropy2) # 0.4689955935892812

#지니계수와 정보이득
gini_index = 1 - gini # 0.5
gini_index = 1 - gini2 # 0.82

info_gain = abs(0.9 - entropy) # 0.099
info_gain = 0.9 - entropy2 # 0.4310
 
##########################
### dataset 적용 
##########################

from sklearn.tree import DecisionTreeClassifier # model 
from sklearn.metrics import confusion_matrix # 평가 
 
from sklearn.tree import plot_tree # 시각화 도구


# 1. data set 생성 함수
def createDataSet():
    #           x1  x2   y       
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    columns = ['dark_clouds','gust'] # X1,X2,label
    return dataSet, columns


# 함수 호출 
dataSet, columns = createDataSet()

# list -> numpy 
dataSet = np.array(dataSet)
dataSet.shape # (5, 3)
print(dataSet)
print(columns) # ['dark_clouds', 'gust']

# 변수 선택 
X = dataSet[:, :2]
y = dataSet[:, -1]

# 레이블 인코딩 : 'yes' = 1 or 'no' = 0
label = [1 if i == 'yes' else 0 for i in y] 


# model 생성 
obj = DecisionTreeClassifier(criterion='entropy')
model = obj.fit(X = X, y = label)

y_pred = model.predict(X)

# 혼동행렬 
con_mat = confusion_matrix(label, y_pred)
print(con_mat)

# 의사결정트리 시각화 : matplotlib 제공  
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plot_tree(model, 
          feature_names=columns, 
          class_names=['no', 'yes'], 
          filled=True)
plt.show()



