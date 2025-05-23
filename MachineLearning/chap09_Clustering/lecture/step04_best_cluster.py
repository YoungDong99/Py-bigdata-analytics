'''
Best Cluster 찾는 방법 
'''

from sklearn.cluster import KMeans # model 
from sklearn.datasets import load_iris # dataset 
import matplotlib.pyplot as plt # 시각화 

# 1. dataset load 
X, y = load_iris(return_X_y=True)
print(X.shape) # (150, 4)
print(X)


# 2. Best Cluster 
size = range(1, 11) # k값 범위(1 ~ 10)
inertia = [] # 응집도 : 거리제곱합(작을 수록 응집도는 좋다) 

for k in size : 
    obj = KMeans(n_clusters = k) 
    model = obj.fit(X)
    inertia.append(model.inertia_)  

print(inertia)
'''
[681.3706, 152.3479517603579, 78.8556658259773, 57.25600931571815, 49.84981451052335, 43.31158141025641, 40.30131168831169, 34.05396825396825, 29.24664005439006, 28.617375125939702]
'''

# 3. best cluster 찾기 : 3 ~ 4
plt.plot(size, inertia, '-o')
plt.xticks(size)
plt.show()


