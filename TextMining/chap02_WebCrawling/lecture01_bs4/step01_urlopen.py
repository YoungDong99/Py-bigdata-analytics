"""
url 요청과 html 파싱
"""


from urllib.request import urlopen  # url요청, 읽기, 해독(한글)
from bs4 import BeautifulSoup  # html 문서 파싱(문자열 -> html 문서화)
## 파싱 : html 태그를 인식할 수 있도록 하는 작업


url = "http://www.naver.com/index.html"

# 1. 원격 서버 url 요청 
url_res = urlopen(url)  # 요청 & 응답
print(url_res)  # <http.client.HTTPResponse object at 0x00000227265F96F0>

byte_data = url_res.read()  ## byte 단위로 읽기
print(byte_data)  # 한글 16진수로 출력됨


# 2. html 파싱 
text_data = byte_data.decode("utf-8") # 디코딩  
print(text_data)  # 한글 정상 출력 확인(일반 텍스트)

## 태그 추출이 가능하도록 html 문서화
html = BeautifulSoup(text_data, 'html.parser') # html source 파싱
print(html)

dir(html)
'''
find('tag') : 1개 태그 찾기
find_all() : 모든 태그 찾기
get('속성')
string : 내용 수집
text : 내용
'''


# 3. a 태그 수집 : 태그 찾기 -> 내용 또는 속성 수집
a = html.find('a') # a 태그 찾기 

print('a 태그 : ', a)
print('a 태그 내용 : ', a.string)
print('a 태그 내용 : ', a.text)

# a 태그 속성 수집
url = a.get('href')
print(url)


### string vs text : 태그 내용 추출하는 속성
'''
string : 태그 내용에 텍스트만 포함된 경우 사용
text : 태그 내용에 또 다른 태그를 포함된 경우 
'''

scr = "<div>이순신 <p>홍길동</p> <a>문단</a> </div>"
html = BeautifulSoup(scr, 'html.parser')

print(html.string)  # None
print(html.text)  # 이순신 홍길동 문단 






