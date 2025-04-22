"""
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

# 1. driver 생성 
driver_path = ChromeDriverManager().install() # 드라이버 설치 경로 
correct_driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe") # 실행파일경로 
driver = webdriver.Chrome(service=Service(executable_path=correct_driver_path)) # 드라이버 생성 



# 2. 대상 url 이동 
driver.get('https://www.naver.com/') # url 이동 


# 3. 로그인 버튼 태그(element) 가져오기 : xpath로 가져오기
'''
//*[@id="account"]/div/a
'''
login_btn = driver.find_element(By.XPATH, '//*[@id="account"]/div/a') 

# 3-1. LINK_TEXT로 element 가져오기
#login_btn = driver.find_element(By.LINK_TEXT, 'NAVER 로그인') 


login_btn.click() # 버튼 클릭 
time.sleep(2) # 2초 일시 중지

driver.back() # 현재페이지 -> 이전으로
time.sleep(2) # 2초 일시 중지 
  
driver.forward() # 이전 -> 앞으로 
driver.refresh() # 페이지 새로고침(F5)

time.sleep(2) # 2초 일시 중지 
driver.close() # 현재 창 닫기  