'''
템플릿 페이지에서 GET/POST 전송 자료 받기

<<작업순서>>
 1. 시작 페이지 : get방식 전송 or post 방식 전송   
 2. Flask 앱 : get방식 or post방식의 파라미터 받고 & 브라우저에 출력 
'''

from flask import Flask, render_template, request # request : 파라미터 받기 

app = Flask(__name__)


@app.route('/') # 시작 페이지
def index() :
    return render_template('/step03/post_method.html') # 시작 페이지

'''
1차 : post_method.html
2차 : get_method.html
'''

@app.route('/login', methods=['GET', 'POST'])    
def login() :    
    if request.method == 'GET' :
        uid = request.args.get('uid')
        return f'get 방식 -> 사용자 아이디 : {uid}'
        
    if request.method=='POST' : # post 방식 
        uid = request.form['uid']
        pwd = request.form['pwd']
        return f'post 방식 <br> 사용자 아이디 : {uid} <br> 사용자 비번 : {pwd}'

if __name__ == '__main__':
    app.run(port=80)







