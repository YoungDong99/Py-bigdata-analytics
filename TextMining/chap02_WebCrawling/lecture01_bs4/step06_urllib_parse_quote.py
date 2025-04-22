"""
여러개의 검색어로 naver 검색 결과 출력하기 : ppt.12 참고 
"""

import urllib
from urllib.request import urlopen  
from bs4 import BeautifulSoup 


# 기본 url 
url = "https://search.naver.com/search.naver?query="

# 검색어 
query_list = ['파이썬', '웹 크롤링', '빅데이터', 'python']

'''
web_data = []

for query in query_list :
    print('query :', query)
    new_url = url + urllib.parse.quote(query) # 한글과 URL 결합 
    
    url_res = urlopen(new_url)
    byte_data = url_res.read()
    text_data = byte_data.decode() # 'utf-8' 기본값 생략 
        
    html = BeautifulSoup(text_data, 'html.parser')  # html 파싱     
    links = html.find_all("a")  # a 태그 모두 가져오기 
    
    result = []
    for a in links :
        print(a.text) # a태그 내용 출력 
        result.append(a.text)
    
    web_data.append(result)
'''

# for문 -> 함수 정의
def crawler_link(query) :
    print('query :', query)
    
    # urllib 패키지 안의 parse 모듈 -> 그 나의 quote 함수
    new_url = url + urllib.parse.quote(query) # 한글(비ASCII)과 URL 결합
    
    url_res = urlopen(new_url)  # url 요청 & 응답
    byte_data = url_res.read()  # byte 읽기
    text_data = byte_data.decode() # 'utf-8' 기본값 생략 
    
    
    html = BeautifulSoup(text_data, 'html.parser')  # html 파싱     
    links = html.find_all("a")  # a 태그 모두 가져오기 
    
    result = []  # 1개 키워드 검색 결과 저장 
    for a in links :
        print(a.text)  # a태그 내용 출력 
        result.append(a.text)  # 리스트 저장
    
    return result

# 함수 호출
web_data = [crawler_link(query) for query in query_list]


# 수집 자료 확인
len(web_data)

web_data[0]

web_data[1]









    
    
    
    
 



