"""
step01 관련 문제 

문1) 다음과 같은 조건으로 Flask 앱을 작성하시오.

   조건1> 템플릿(templates) 파일 작성 위치 : templates\exam01 폴더
   조건2> 서버의 기본 url을 요청 시 index.html 페이지로 응답하여 
         'Flask Test'를 제목으로 출력하고, 바로 아래쪽에 test.png
          이미지를 브라우저에 보이도록 한다.
   조건3> 모든 내용은 페이지 가운데 정렬한다. 

      기타 : 출력결과는 강의자료에서 확인    
"""

from flask import Flask, render_template # 템플릿 페이지 요청 

# 1. app 객체 생성 
app = Flask(__name__)


# 2. 서버 요청 & 응답
@app.route("/")
def index() :
    return render_template('/exam01/index.html')  


# 프로그램 시작점 
if __name__ == '__main__' :    
    app.run(port=80)





