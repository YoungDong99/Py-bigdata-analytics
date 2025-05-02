"""
step03 관련 문제 

문2) 사원목록에서 '부서번호'를 클릭하면 해당 부서 정보가 출력되도록 하시오. 

   조건1> 템플릿(templates) 파일 작성 위치 : templates\exam03 폴더
   조건2> 사원목록을 나타내는 페이지 : emp_list.html
   조건3> 부서 정보가 출력되는 페이지 : dept_info.html 
   조건4> 전송 방식 : get 방식 
   조건5> 부서 정보(부서번호, 부서명, 부서위치) 
          10, '기획실', '서울시'   
          20, '연구실', '대전시'
          30, '영업부', '싱가폴'
        
   
   기타 : 출력결과는 강의자료에서 확인     
"""


from flask import Flask, render_template, request  


app = Flask(__name__)


@app.route('/') # 시작 페이지
def input() :
    return render_template('/exam03/emp_list.html') # 사원목록 

# 오타 수정 : methods = '[GET]' -> methods = ['GET']
@app.route('/deptInfo', methods = ['GET']) # get 방식 전송 
def deptInfo() :   
    dno = request.args.get('dno') # 부서번호 받기 
    
    if dno == '10' :
        dname = '기획실'
        loc = '서울시'
    elif dno == '20' :
        dname = '연구실'
        loc = '대전시'
    else :
        dname = '영업부'
        loc = '싱가폴'
        

    # 템플릿에 부서번호 넘기기 
    return render_template('/exam03/dept_info.html', 
                           dno = dno, dname = dname, loc = loc) # 부서정보  

if __name__ == '__main__':
    app.run(port=80)
    
    
    
    
    
    
    
    
    
    
    