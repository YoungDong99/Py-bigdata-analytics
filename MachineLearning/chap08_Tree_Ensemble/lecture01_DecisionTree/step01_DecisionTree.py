'''
Decision Tree 모델 & 시각화 
"""

'''
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier # 의사결정트리 모델  
from sklearn.metrics import accuracy_score # model 평가 
# tree 시각화 
from sklearn.tree import plot_tree # 의사결정트리 

# 1. dataset load 
path = r'c:\ITWILL\5_Python_ML\data'
dataset = pd.read_csv(path + "/tree_data.csv")
print(dataset.info())
'''
iq         6 non-null int64 - iq수치
age        6 non-null int64 - 나이
income     6 non-null int64 - 수입
owner      6 non-null int64 - 사업가 유무
unidegree  6 non-null int64 - 학위 유무
smoking    6 non-null int64 - 흡연 유무 - y변수 
'''

# 2. 변수 선택 
cols = list(dataset.columns)
X = dataset[cols[:-1]]
y = dataset[cols[-1]]

# 3. model & 평가 
model = DecisionTreeClassifier(random_state=123).fit(X, y)

y_pred = model.predict(X)

acc = accuracy_score(y, y_pred)
print(acc) # 1.0


# 4. tree 시각화 
feature_names = cols[:-1]  # x변수 이름 

# y변수 class 이름 
class_names = ['No', 'Yes'] 


# 의사결정트리 시각화 : 선명도 떨어짐
import matplotlib.pyplot as plt
''' 
plot_tree(model, 
          feature_names = feature_names,
          class_names=class_names)  
plt.show()
'''

# 의사결정트리 시각화 : matplotlib 이용   
plt.figure(figsize=(20, 10))
plot_tree(model, 
          feature_names=feature_names, 
          class_names=class_names, 
          rounded=True,
          filled=True)
plt.show()
# 흡연자 : 수입과 지능지수 높음 


