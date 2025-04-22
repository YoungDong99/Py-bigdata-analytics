"""
로케이터(locator) : 요소(element) 찾기 기능 

<작업순서>
1. naver page 이동 
2. login 버튼 클릭 
3. 페이지 이동(뒤로, 앞으로) 
"""

from selenium import webdriver # driver 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자  
from selenium.webdriver.common.by import By # 로케이터
import os
import time # 화면 일시 정지


# 1. 크롬 driver 생성 
driver_path = ChromeDriverManager().install() # 드라이버 설치 경로 
correct_driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe") # 실행파일경로 
driver = webdriver.Chrome(service=Service(executable_path=correct_driver_path)) # 드라이버 생성 

dir(driver)
'''
find_element(By.로케이터, "이름") : 1개 태그 찾기
fine_elements(By.로케이터, "이름") : 여러 개 태그 찾기
back() : 뒤로 이동
forward() : 앞으로 이동
refresh() : F5키(새로고침)
'''

# 2. 대상 url 이동 
driver.get('https://www.naver.com/') # url 이동 

# 3. 로그인 버튼 태그(element) 가져오기 : class name으로 가져오기(ppt.11) 
'''
<a href="https://nid.naver.com/nidlogin.login?mode=form&amp;url=https://www.naver.com/" class="MyView-module__link_login___HpHMW"><i class="MyView-module__naver_logo____Y442"><span class="blind">NAVER</span></i>로그인</a>
'''
login_btn = driver.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
login_btn.click() # 로그인 버튼 클릭 -> 로그인 페이지 이동
time.sleep(2) # 2초 일시 중지

driver.back() # 현재페이지 -> 뒤로
time.sleep(2) # 2초 일시 중지
  
driver.forward() # 현재페이지 -> 앞으로
driver.refresh() # 페이지 새로고침(F5)
time.sleep(2) # 2초 일시 중지

driver.close() # 현재 창 닫기


