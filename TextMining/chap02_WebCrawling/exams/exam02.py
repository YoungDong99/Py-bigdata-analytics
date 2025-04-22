'''
 문2) urls 객체의 url을 대상으로 다음 조건에 맞게 웹 문서의 자료를 수집하시오.
    조건1> https://으로 시작하는 url만을 대상으로 한다.
    조건2> url에 해당하는 웹 문서를 대상으로 <a> 태그(tag) 내용만 출력한다.
    조건3> <a> 태그 내용이 없는(None) 경우는 출력하지 않는다.

    <출력 결과 예시>
    url : https://www.daum.net
    a 태그 전체 개수 : 1
     브라우저에서 자바스크립트를 활성화하는 방법
     
    url : https://www.naver.com
    a 태그 전체 개수 : 8
    상단영역 바로가기
    서비스 메뉴 바로가기
    새소식 블록 바로가기
    쇼핑 블록 바로가기
    관심사 블록 바로가기
    MY 영역 바로가기
    위젯 보드 바로가기
    보기 설정 바로가기
'''

from urllib.request import urlopen # 함수 : 원격 서버 url 요청 
from bs4 import BeautifulSoup # 클래스 : html 파싱
import re # 정규표현식

urls = ['https://www.daum.net', 'www.duam.net', 'https://www.naver.com']


# 단계1 : url 정제
url_pat = re.compile('^https://www')

# None이 아닌 url을 저장
new_urls = [url for url in urls if url_pat.match(url)]

# 단계2 : url에서 a 태그 내용 수집 & 출력
for url in new_urls :   
    # 1. url 요청
    print('url :', url)
    
    text_src = urlopen(url).read().decode()
    
    # 2. html 파싱 
    html = BeautifulSoup(text_src, 'html.parser')
    
    # 3. a 태그 찾기 & 내용 출력  
    links = html.find_all('a')
    
    print('a 태그 전체 개수 :', len(links))
    
    for a in links :
        print(a.string)
    
    print('================================')




# for문 -> 함수로 변경
def crawler(url) :
    print('url :', url)
    
    text_src = urlopen(url).read().decode()
    
    # 2. html 파싱 
    html = BeautifulSoup(text_src, 'html.parser')
    
    # 3. a 태그 찾기 & 내용 출력  
    links = html.find_all('a')
    
    print('a 태그 전체 개수 :', len(links))
    
    for a in links :
        print(a.string)
    
    print('================================')


# crawler 함수 호출
for url in new_urls :
    crawler(url)









