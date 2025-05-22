'''
의사결정트리 주요 Hyper parameter 
'''

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
# tree 시각화
from sklearn.tree import plot_tree


iris = load_iris()
x_names = iris.feature_names # x변수 이름 
labels = iris.target_names # ['setosa', 'versicolor', 'virginica']

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)


############################
### Hyper parameter 
############################
'''
criterion='gini' : 중요변수 선정 기준, 
 -> criterion : {"gini", "entropy"}, default="gini"
splitter='best' : 각 노드에서 분할을 선택하는 데 사용되는 전략, 
max_depth=None : tree 최대 깊이, 
 -> max_depth : int, default=None
 -> max_depth=None : min_samples_split의 샘플 수 보다 적을 때 까지 tree 깊이 생성 
 -> 과적합 제어 역할 : 값이 클 수록 과대적합, 적을 수록 과소적합 
min_samples_split=2 : 내부 노드를 분할하는 데 필요한 최소 샘플 수(기본 2개)
 -> int or float, default=2    
 -> 과적합 제어 역할 : 값이 클 수록 과소적합, 적을 수록 과대적합 
'''

# model : default parameter
model = DecisionTreeClassifier(criterion='gini',
                               random_state=123, 
                               max_depth=None,
                               min_samples_split=2)
# min_samples_split=2 : 샘플 수 2이하가 될때까지 트리 깊이 만듬 
dir(model)
'''
feature_importances_ : 중요변수 확인
get_depth() : 트리 깊이 
'''
model.fit(X=X_train, y=y_train) # model 학습 

model.feature_importances_
# [0.01364196, 0.01435996, 0.5461181 , 0.42587999]
model.get_depth() # 5 



# model 평가 : 과적합(overfitting) 유무 확인  
model.score(X=X_train, y=y_train) # 1.0
model.score(X=X_test, y=y_test) # 0.9555555555555

# tree model 시각화 
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plot_tree(model, 
          feature_names=x_names, 
          class_names=labels, 
          filled=True)
plt.show()



