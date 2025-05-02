'''
템플릿 페이지에서 GET과 POST 동시에 전송되는 자료 받기
'''

from flask import Flask, render_template, request # request import

app = Flask(__name__)


@app.route('/') # 시작 페이지
def index() :
    return render_template('/step03/main.html') # 템플릿 파일


@app.route('/receive', methods=['POST', 'GET']) # post 방식 
def received() :    
    if request.method=='POST' : # post 방식 
        name = request.form['uname'] # 파라미터 받기  
        age = request.form['age']
        
        result = "[post 방식] 사용자 정보 : " + name + ', ' + age         
        return render_template('/step03/result.html', result=result)

    if request.method=='GET' : # get 방식 
        name = request.args.get('uname') # 파라미터 받기
        age = request.args.get('age') # 파라미터 받기
        result = "[get 방식] 사용자 정보 : " + name + ', ' + age 
        return render_template('/step03/result.html', result=result)
    
if __name__ == '__main__':
    app.run(port=80)







