"""
step03 관련 문제 

문1) 다음과 같은 조건으로 Flask 앱을 작성하시오.

   조건1> 템플릿(templates) 파일 작성 위치 : templates\exam03 폴더
   조건2> input 페이지에서 아이디와 비밀번호를 입력하여 post 방식으로 서버에 전송
   조건3> output 페이지에서 아이디와 비밀번호를 파라미터로 받아서 인증 여부 판단
          로그인 성공 : 아이디 : 'hong', 비번 : '1234'  
          로그인 실패 : 아이디 또는 비번이 다른 경우 
   
   기타 : 출력결과는 강의자료에서 확인     
"""


from flask import Flask, render_template, request  


app = Flask(__name__)


@app.route('/') # 시작 페이지
def input() :
    return render_template('/exam03/input.html') # 템플릿 파일


@app.route('/output', methods=['POST']) # get 방식 전송 
def output() :
    uid = request.form['uid']
    pwd = request.form['pwd']  
    
    if uid == 'hong' and pwd == '1234' :
        result = "로그인 성공!"
    else :
        result = "로그인 실패.."
        
    return render_template('/exam03/output.html', result = result)



if __name__ == '__main__':
    app.run(port=80)











