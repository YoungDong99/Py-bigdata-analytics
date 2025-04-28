"""
5.nltk.classify: 텍스트 데이터를 기반으로 분류기 생성 및 평가 그리고 새로운 텍스트 분류
"""


'''
단계1. 필요한 라이브러리 가져오기
  - NLTK의 필요한 모듈 가져오기 
''' 
from nltk.classify import NaiveBayesClassifier  # 분류기
from nltk.classify.util import accuracy  # 정확도
from nltk.tokenize import word_tokenize # 토큰 생성기  


'''
단계2. 데이터셋 준비
 - 간단한 긍정과 부정 문장 데이터 준비
'''
dataset = [  # 정답 포함 : 지도학습
    ("I love this movie, it’s fantastic!", 'positive'),
    ("This- product is excellent, I would buy it again!", 'positive'),
    ("I hated this movie, it was terrible.", 'negative'),
    ("This is the worst product I have ever bought.", 'negative'),
    ("Amazing experience, very satisfied!", 'positive'),
    ("Not happy with the service at all.", 'negative')
]



'''
단계3. 특징(features) 추출 함수 정의
 - 문장에서 단어(features)를 추출하고 존재 여부를 확인하는 함수 
'''

def extract_features(sentence):
    words = word_tokenize(sentence)  # 문장 -> 단어 token
    return {word: True for word in words} # {'단어' : True} : 단어 존재 여부  



'''
단계4. 데이터셋 준비 : 훈련셋과 평가셋 
 - 특성 추출 함수를 사용하여 분류기에 적용할 데이터셋 준비
'''

# 데이터셋을 특성화
feature_data = [(extract_features(sentence), label) for (sentence, label) in dataset]
len(feature_data) # 6
print(feature_data)
'''
  (특징:{'단어1':True, '단어2':True, 정답:긍정 or 부정})
'''


# 훈련셋과 평가셋 나누기
train_data = feature_data[:4] # 4 : 긍정(2)+부정(2)) : 훈련셋
test_data = feature_data[4:] # 2 : 긍정(1) + 부정(1) : 평가셋


'''
단계5. 분류기 학습 및 테스트
 - NaiveBayesClassifier를 사용하여 모델을 학습하고, 테스트 데이터를 통해 정확도 평가
'''

# 분류기 학습 : 훈련셋 이용   
classifier = NaiveBayesClassifier.train(train_data)
# 객체 생성이 아니라 학습을 완료한 모델을 반환하는 코드
'''
type(classifier) : NaiveBayesClassifier 객체 (분류기)
train : 훈련셋 데이터를 이용해 기계한테 학습시키는 메서드
classifier 안에는 학습 내용 저장 : 어떤 단어들이 긍정,부정에 얼마나 자주 나오는지에 대한 정보
'''
print(classifier) # 객체의 메모리 주소와 타입 출력


# 분류기 평가(성능 평가) : 평가셋 이용   
print("Accuracy:", accuracy(classifier, test_data)) # model <- 평가셋 
# Accuracy: 1.0


# 분류기 정보 출력 : 학습된 분류기에서 가장 정보량이 높은 특성(feature) 출력  
classifier.show_most_informative_features() # (n=10)

'''
Most Informative Features
                       , = True           positi : negati =      1.7 : 1.0
                   again = None           negati : positi =      1.7 : 1.0
                  bought = None           positi : negati =      1.7 : 1.0
                     buy = None           negati : positi =      1.7 : 1.0
                    ever = None           positi : negati =      1.7 : 1.0
               excellent = None           negati : positi =      1.7 : 1.0
               fantastic = None           negati : positi =      1.7 : 1.0
                   hated = None           positi : negati =      1.7 : 1.0
                    have = None           positi : negati =      1.7 : 1.0
                      it = True           positi : negati =      1.7 : 1.0
                      
                '단어'=True : 해당 단어가 문장에 포함된 경우
                '단어'=None : 해당 단어가 문장에 포함된 않은 경우
                예) excellent = None : 단어가 문장에 포함 안되는 경우 부정 확률 높음 
'''


'''
단계6. 새로운 문장 분류
 - 새로운 문장을 분류기에 넣고 긍정/부정을 예측한다.
'''

new_sentence = "The service was absolutely wonderful!" # 긍정문 
features = extract_features(new_sentence) # 특정 추출 

# classify 메서드 : 긍정, 부정에 대한 최종 판단을 내려줌
print("Classification:", classifier.classify(features)) # 분류기 적용 












