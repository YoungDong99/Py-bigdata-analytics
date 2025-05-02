"""
step02 관련 문제 

문1) 다음과 같은 조건으로 Flask 앱을 작성하시오.

   조건1> 템플릿(templates) 파일 작성 위치 : templates\exam02 폴더
   조건2> fruit_list.html 페이지에서 과일명을 클릭하면 fruit_info.html 페이지에서
         클릭한 과일명과 과일 이미지가 출력되도록 fruit_info.html 페이지를 
         완성하시오. 
   
   기타 : 출력결과는 강의자료에서 확인     
"""


from flask import Flask, render_template # 템플릿 페이지 요청 


# 1. app 객체 생성 
app = Flask(__name__) # 생성자 -> object 


# 2. 서버 요청 & 응답
@app.route("/") # 기본 url 요청 
def flist() : # 응답 함수     
    return render_template('/exam02/fruit_list.html') # 과일 목록 페이지  


@app.route('/finfo/<name>') # /<name> : 외부 파라미터 받음
def finfo(name) : 
    return render_template('/exam02/fruit_info.html', name=name) # 과일 정보 페이지  
    

# 프로그램 시작점 
if __name__ == '__main__' :    
    app.run(host = '127.0.0.1', port = 80) # app 실행
    
    
    
    
    
    