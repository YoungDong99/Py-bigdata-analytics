"""
CSS 선택자 이용 태그 수집  
"""

from selenium import webdriver # driver 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자  
from selenium.webdriver.common.by import By # 로케이터
import os 
import time # 화면 일시 정지 


# 태그 수집 함수 
def keyword_search(keyword) :
    # 1. driver 생성 
    driver_path = ChromeDriverManager().install() # 드라이버 설치 경로 
    correct_driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe") # 실행파일경로 
    driver = webdriver.Chrome(service=Service(executable_path=correct_driver_path)) # 드라이버 생성 
    
    
    # 2. url 이동 : naver news 검색 페이지 이동
    # new_url = 기본 url + 검색어
    url = f'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={keyword}'
    driver.get(url) 
    time.sleep(3)
    
    
    # 3. 선택자 지정 
    '''
    <span class="sds-comps-text sds-comps-text-ellipsis-1 sds-comps-text-type-headline1">프로<mark>야구</mark>, 18일부터 더블헤더 시행…순위싸움 변수 될까</span>
    클래스 여러개(공백) 중 하나 선택 -> sds-comps-text
    '''
    links = driver.find_elements(By.CSS_SELECTOR, 'a.sds-comps-text')  # a 태그, class 이름.
    print('수집 a_tags 개수 =', len(links))
    
    # 4. urls 추출 
    urls = []
    for a in links :        
        urls.append(a.get_attribute('href')) 
        '''
        a.text : 내용 추출
        a.get_attribute('속성') : 속성 추출
        '''
    
    driver.close() # 창 닫기 
    
    return urls


# 함수 호출 
keyword = input('검색어 입력 : ') # 파이썬, 크롤링  
urls = keyword_search(keyword)
print('-'*50)

for url in urls :
    print(url)

