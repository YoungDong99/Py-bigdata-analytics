"""
Flask 앱(application) 샘플 

Flask 설치 필요 
 > pip install flask
"""

from flask import Flask 

# 1. 애플리케이션(app) 객체 생성 
app = Flask(__name__)  


# 3. 서버 요청 & 응답
@app.route("/") # 요청할 url 설정 : 시작주소 의미 (http://127.0.0.1:5000)
def hello() : # 응답 함수 정의
    return "Hello Flask ~~ 홍길동" # 브라우저로 응답할 내용  

 
# 프로그램 시작점 
if __name__ == '__main__' :
    app.run() # 2. 애플리케이션(app) 실행 (서버 실행)
    # 서버 주소(기본 url)













