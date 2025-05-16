"""
 - 로지스틱회귀모델 & ROC 평가
 - 이항분류기(binary class classifier) 
"""

from sklearn.datasets import load_breast_cancer # dataset
from sklearn.linear_model import LogisticRegression # model 
from sklearn.model_selection import train_test_split # dataset split 
from sklearn.metrics import confusion_matrix, accuracy_score # model 평가 


################################
### 이항분류(binary class) 
################################

# 1. dataset loading 
X, y = load_breast_cancer(return_X_y=True)

print(X.shape) # (569, 30)
print(y) # 0(양성) or 1(악성)


# 2. train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.3, random_state=1)


# 3. model 생성 
lr = LogisticRegression(solver='lbfgs', max_iter=100, random_state=1) # 빈 모델  
'''
solver='lbfgs', : 최적화에 사용되는 기본 알고리즘(solver) 
max_iter=100,  : 반복학습횟수 
random_state=None, : 난수 seed값 지정 
'''

model = lr.fit(X=X_train, y=y_train) # 학습모델 


# 4. model 평가 
y_pred = model.predict(X = X_test) # class 예측치(0 or 1) 
y_true = y_test # 관측치 

# 1) 혼동행렬(confusion_matrix)
con_max = confusion_matrix(y_true, y_pred)
print(con_max)
'''
     0    1 
0 [[ 57   6]
1  [  6 102]]
'''

# 2) 분류정확도 
acc = accuracy_score(y_true, y_pred)
print('accuracy =',acc) # accuracy = 0.9298245614035088

# 민감도(Sensitivity) = TPR : 실제 양성(1)을 양성(1)으로 예측할 비율
# 특이도(Specificity) = TNR : 실제 음성(0)을 음성(0)으로 예측할 비율
# 위양성비율 = FPR : 실제 음성(0)을 양성(1)으로 잘못 예측한 비율 
 
TPR = 102 / (6 + 102) # 0.944444 : y축 
TNR = 57 / (57 + 6) # 0.90476  
FPR = 1 - TNR # 0.09523809523809523 : x축 

FPR = 6 / (57 + 6) # 0.09523809523809523




#############################
# ROC curve 시각화
#############################
dir(model)
'''
predict(X) : class 예측 
predict_proba(X) : 확률 예측
'''

# 1) 확률 예측치
y_pred_proba = model.predict_proba(X = X_test) # 확률 예측 
y_pred_proba = y_pred_proba[:, 1]  # y=1 확률  


# 2) ROC curve 
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt 

fpr, tpr, _ = roc_curve(y_true, y_pred_proba) # y정답, y=1 확률예측치 
# tpr : 민감도(y축) 
# fpr : 1-특이도(x축) 

plt.plot(fpr, tpr, color = 'red', label='ROC curve')
plt.plot([0, 1], [0, 1], color='green', linestyle='--', label='AUC')
plt.legend()
plt.show()

'''
ROC curve FPR vs TPR  

ROC curve x축 : FPR(False Positive Rate) - 실제 음성을 양성으로 잘못 예측할 비율  
ROC curve y축 : TPR(True Positive Rate) - 실제 양성을 양성으로 정상 예측할 비율  
'''


