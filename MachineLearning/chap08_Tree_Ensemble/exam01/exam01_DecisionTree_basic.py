'''
 문1) load_breast_cancer 데이터 셋을 이용하여 다음과 같이 Decision Tree 모델을 생성하시오.
  <조건1> 75:25비율 train/test 데이터 셋 구성 
  <조건2> x변수 : cancer.data, y변수 : cancer.target
  <조건3> tree 최대 깊이 : 5 
  <조건4> decision tree 시각화 & 중요변수 확인
'''

from sklearn import model_selection
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
# tree 시각화 
from sklearn.tree import plot_tree

# 데이터 셋 load 
cancer = load_breast_cancer()
dir(cancer)
'''
feature_names : X변수명 
target_names : y클래스명 
'''

X_names = cancer.feature_names
class_names = cancer.target_names

# <단계1> x변수 : cancer.data, y변수 : cancer.target
X = cancer.data 
X.shape # (569, 30)
y = cancer.target # 0 or 1

# <단계2> 75:25비율 train/test 데이터 셋 구성
X_train, X_test, y_train, y_test = model_selection.train_test_split(
    X, y, test_size=0.3, random_state=123)

# <단계3> tree 최대 깊이 : 5
model = DecisionTreeClassifier(max_depth=5, random_state=123).fit(X=X_train, y=y_train)

# model 평가 
model.score(X=X_test, y=y_test) # 0.9473684210526315

# <단계4> decision tree 시각화 & 중요변수 확인 
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plot_tree(model, 
          feature_names=X_names, 
          class_names=class_names, 
          filled=True)
plt.show()

#중요변수 확인 
print(model.feature_importances_)
'''
[0.         0.         0.         0.00740627 0.01234379 0.
 0.         0.03029839 0.         0.         0.0107817  0.00740627
 0.         0.         0.0096017  0.         0.         0.
 0.         0.         0.72298482 0.08647305 0.         0.01185004
 0.         0.         0.01101526 0.08983871 0.         0.        ]
'''

# 막대차트 : x축(변수명), y축(중요도)
plt.barh(y=X_names, width=model.feature_importances_)
#plt.barh(x=X_names, height=model.feature_importances_)
plt.show()
# worst_radius(종양 반지름) 클 수록 악성 확률이 높다. 


