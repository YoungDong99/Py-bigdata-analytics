"""
- templates 이용한 url 요청과 응답
"""

from flask import Flask, render_template  

# 1. 애플리케이션(app) 생성 
app = Flask(__name__)  


# 3. 서버 요청 & 응답
@app.route("/")  
def index() :  
    return render_template('/step01/index.html')  


# 프로그램 시작점 
if __name__ == '__main__' :
    app.run(host = '127.0.0.1', port = 80) # 2. 애플리케이션(app) 실행
    '''
    host : 서버 url
    port : 서버 포트번호 
    '''  


