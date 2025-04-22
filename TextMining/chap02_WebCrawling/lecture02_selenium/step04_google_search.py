"""
 검색어 입력 및 검색 페이지 이동
"""

from selenium import webdriver # driver 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자  
from selenium.webdriver.common.by import By # 요소 선택 
from selenium.webdriver.common.keys import Keys # 엔터키 역할
from selenium.webdriver.chrome.options import Options # driver options생 성 

import os
import time 
 
# 1. driver 생성 
driver_path = ChromeDriverManager().install() # 드라이버 설치 경로 
correct_driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe") # 실행파일경로 
#driver = webdriver.Chrome(service=Service(executable_path=correct_driver_path)) # 드라이버 생성 


# '로봇이 아닙니다' 라는 메시지가 나오는 경우

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)


# 2. url 이동 : 구글 페이지 이동 
driver.get("https://www.google.com/") # 구글 페이지 이동


# 3. 입력상자 가져오기 : <textarea name='q'>  </textarea>
elem = driver.find_element(By.NAME, "q") # 입력상자 element 수집


# 4. 검색어 입력 -> 엔터 
elem.send_keys("셀레리움 크롤링") # 검색어 입력 
time.sleep(3) # 3초 일시 중지 
elem.send_keys(Keys.ENTER) # 엔터 키 -> 검색 페이지 이동  
time.sleep(3) # 3초 일시 중지 


# 5. class 이름으로 요소 선택  
'''
<h3 class="LC20lb MBeuO DKV0Md">초보자를 위한 웹 크롤링: Selenium과 Scrapy로 시작하기</h3>
'''
# 클래스 이름에 공백 의미 -> or

heads = driver.find_elements(By.CLASS_NAME, "LC20lb")  
print('수집 head 개수 =', len(heads)) 
print(heads)

# 6. head 텍스트 출력  
head_text = [head.text for head in heads]     
print(head_text)

time.sleep(3)
driver.close() # 창 닫기 














