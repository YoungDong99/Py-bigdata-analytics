"""
- 템플릿 페이지 불러오기 
"""

from flask import Flask, render_template # 템플릿 페이지 요청 

# 1. app 객체 생성 
app = Flask(__name__) 


# 3. 서버 요청 & 응답 
@app.route("/") 
def index() : # 응답 함수 
    return render_template('/step01/main.html')  


@app.route('/cont') 
def info() : # 응답 함수
    return render_template('/step01/cont.html') 

@app.route('/info') 
def test() : # 응답 함수
    return render_template('/step01/info.html') 

# 프로그램 시작점 
if __name__ == '__main__' :    
    app.run(host = '127.0.0.1', port = 80) # 2. 애플리케이션(app) 실행  





