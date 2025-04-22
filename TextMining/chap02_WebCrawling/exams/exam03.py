'''
 문3) css_example.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오.

   <조건1> class="odd" 선택자를 이용하여 3행과 5행의 <td> 전체 내용 출력 

   <출력 결과>     
    201602 
    이순신 
    해양학과 
    lee@naver.com 
    201604 
    유관순 
    유아교육 
    you@naver.com
    
    <조건2> id="tab" 선택자를 이용하여 하위 태그 전체를 가져온 후 <th> 전체 내용 출력
    
   <출력 결과>
    학번 
    이름 
    학과 
    이메일
'''

from bs4 import BeautifulSoup

path = r'C:\ITWILL\3_TextMining\data'

# 1. 파일 읽기 
file = open(path + "/css_example.html", mode='r', encoding='utf-8')
source = file.read()
file.close()


# 2. html 파싱
html = BeautifulSoup(source, 'html.parser')


# 3. 선택자 이용 태그 내용 가져오기 


## 조건 1
tds = html.select(".odd > td")

# td 전체 내용 출력 
for data in tds :
    print(data.string)



## 조건 2

trs = html.select("#tab > tr") # 계층적으로 접근 : 열 제목

print('\nth 내용')

for tr in trs :
    ths = tr.find_all('th') # 요소 추출
    for th in ths :
        print(th.string) # 내용 추출 


## 조건 2 다른 풀이
ths = html.select("#tab > tr > th")
for th in ths :
    print(th.string)



