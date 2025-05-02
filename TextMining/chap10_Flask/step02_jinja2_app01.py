"""
jinja2 표현식 
 - 템플릿에서 python 객체 표현식 : {{객체}} or {% for or if %}
 - templates/step02 작성
"""

from flask import Flask, render_template 

# 1. app 객체 생성 
app = Flask(__name__) # 생성자 -> object 


# 2. 서버 요청 & 응답
@app.route("/") 
def index() : # 응답 함수 
    return render_template('/step02/test.html') 

@app.route("/view")
def view() :
    username = "홍길동"  
    scores = [85, 65, 95]  
    return render_template('/step02/view.html', name = username, scores = scores) 


# 프로그램 시작점 
if __name__ == '__main__' :
    app.run(host = '127.0.0.1', port = 80)
    