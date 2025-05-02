'''
템플릿 페이지에서 GET 전송 자료 받기

<<작업순서>>
 1. index 페이지 : 가전제품 선택 
 2. choice 페이지 : 상품 이미지 출력 
'''

from flask import Flask, render_template, request  


app = Flask(__name__)


@app.route('/') # 시작 페이지
def index() :
    return render_template('/step03/index.html') # 시작페이지 


@app.route('/choice', methods=['GET']) # get방식 전송   
def choice() :
    img_file = request.args.get('image') # get방식 파라미터 받기  
    print(img_file)
    return render_template("/step03/choice.html", img_file = img_file)

if __name__ == '__main__':
    app.run(port=80)




