# -*- coding: utf-8 -*-
"""
step02 관련 문제 

문2) 다음과 같은 조건으로 Flask 앱을 작성하시오.

   조건1> 템플릿(templates) 파일 작성 위치 : templates\exam02 폴더
   조건2> 다음 영화 자료를 대상으로 긍정 리뷰(review) 상위 20개를 선정하여 
         영화 제목과 영화 리뷰(review)를 템플릿 페이지로 출력하시오.
   
   기타 : 출력결과는 강의자료에서 확인     
"""


from flask import Flask, render_template # 템플릿 페이지 요청 
import pandas as pd

path = r"C:\ITWILL\3_TextMining\data"

movie_data = pd.read_csv(path + '/movie_reviews.csv')


print(movie_data.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1492 entries, 0 to 1491
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   reviews  1492 non-null   object
 1   title    1492 non-null   object
 2   label    1492 non-null   int64 # 1(긍정) or 0(부정)
'''

# 단계1 : 자료 생성 

# 1) 긍정 리뷰만 추출 
df = movie_data[movie_data.label == 1]
df.shape # (755, 3)


# 2) df에서 reviews와 title 칼럼을 대상으로 상위 20개 추출  
reviews = None
title = None

# 단계2 : Flask 서비스  
 
# 1. app 객체 생성 
app = Flask(__name__) # 생성자 -> object 


# 2. 서버 요청 & 응답
@app.route("/") # 기본 url 요청 
def index() : # 응답 함수     
    return render_template('/exam02/index.html') # index 페이지 요청  


@app.route('/review') #  기본 url/review 요청
def review() : # 호출 함수
    return render_template('/exam02/result.html') # result 페이지 요청   

# 프로그램 시작점 
if __name__ == '__main__' :    
    app.run(host = '127.0.0.1', port = 80) # app 실행
    
    
    
    
    
    