"""
<패키지 설치> 
(base) pip install selenium
(base) pip install webdriver_manager
"""

from selenium import webdriver # 드라이버 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자  
import os # file 경로 
import time # 화면 일시 정지


# 1. 크롬 driver 생성 
driver_path = ChromeDriverManager().install() # 드라이버 설치 경로 
correct_driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe") # 실행파일경로 
driver = webdriver.Chrome(service=Service(executable_path=correct_driver_path)) # 드라이버 생성 
# 크롬 드라이버 객체 생성 > 객체를 인수로 경로 생성 > 드라이버 제어 객체 생성


dir(driver)
'''
get('url')

'''




# 2. 대상 url 이동 
driver.get('https://www.naver.com/') # url 이동 


# 3. 일시 중지 & driver 종료 
time.sleep(3) # 3초 일시 중지 
driver.close() # 현재 창 닫기  


















