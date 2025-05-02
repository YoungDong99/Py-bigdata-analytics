"""
csv file 자료 & Flask 웹 표현     
"""

from flask import Flask, render_template # 템플릿 페이지 요청 
import pandas as pd # csv file read


# 단계1 : csv fiel 자료 준비  
path = r"C:\ITWILL\3_TextMining\data"
news = pd.read_csv(path + '/daum_news.csv')
print(news.info()) 


# 칼럼 추출 
title = news['title']
news = news['news']



# 단계2 : Flask 서비스 

# 1. app 객체 생성  
app = Flask(__name__)  


# 2. 서버 요청 & 응답
@app.route("/") # 기본 url 요청 
def index() : # 응답 함수   

    return render_template('/step02/news.html',
                       title = title, news = news, zip = zip) # movies 페이지 요청 
    
 
# 프로그램 시작점 
if __name__ == '__main__' :    
    app.run(host = '127.0.0.1', port = 80) # app 실행
    
    
    
    
    
    