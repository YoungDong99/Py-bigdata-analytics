'''
문4) 강의자료(PTT.63)의 인공신경망 모델에서 히든 노드(hidden node)를 구성하는 두 개의 노드를 
     다음과 같은 단계로 계산하시오. 
     
       
    <단계1> 가중치(weight)행렬 만들기 : 표준정규분포 난수 자료 이용   
    <단계2> 입력(X) 행렬 만들기 : 1.5,0.5,1.2 자료 이용      
    <단계3> 두 행렬 연산 : 행렬곱 연산   
           계산식 : hidden(2,1) = weight(2,3) @ X(3,1)   
           
    <출력 예시> 
    node1 =  2.251738398297871
    node2 =  0.2997682638949022       
'''

import numpy as np 
 

print('단계1 : 가중치(weight)행렬 만들기') # 힌트) np.random.randn() 함수 
weight = np.random.randn(2, 3) # 2행3열  
print(weight)
weight.shape # (2, 3)


print('단계2 : 입력(X) 행렬 만들기') # 힌트) numpy 다차원 배열
X = np.array([1.5,0.5,1.2]).reshape(3, 1) # 3행1열 
print(X)
X.shape # (3, 1)


print('단계3 : hidden node 계산') # 힌트) 행렬곱 연산 
hidden_node = weight.dot(X) # weight @ X
hidden_node.shape # (2, 1)

print('node1 = ', hidden_node[0,0])
print('node2 = ', hidden_node[1,0])







