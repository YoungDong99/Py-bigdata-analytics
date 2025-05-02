'''
템플릿 페이지에서 GET/POST 전송 자료 받기

<<작업순서>>
 1. 시작 페이지 : 사용자 정보 입력 & get 방식 전송   
 2. Flask 앱 : get 방식의 파라미터 받기  
'''

from flask import Flask, render_template, request 

app = Flask(__name__)


@app.route('/') # 시작 페이지
def index() :
    return render_template('/step03/get_method.html') # 시작 페이지 


@app.route('/login', methods=['GET']) # 전송방식 
def login() :
    uid = request.args.get('uid')
    print(uid)  # 콘솔 출력
    return "uid = " + uid  # 브라우저 출력
        
    

if __name__ == '__main__':
    app.run(port=80)







