"""
2) 동적페이지 방식 : NAVER 카페 > 인기글 수집

NEVER 카페 홈 : https://section.cafe.naver.com/ca-fe/home
인기글 : https://section.cafe.naver.com/ca-fe/home/cafe-hots 
"""

from selenium import webdriver # 드라이버 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자 
from selenium.webdriver.common.by import By
import os 
import time # 화면 일시 정지

# 1. driver 생성 
driver_path = ChromeDriverManager().install() # 드라이버 설치 경로 
correct_driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe") # 실행파일경로 
driver = webdriver.Chrome(service=Service(executable_path=correct_driver_path)) # 드라이버 생성 

# 2. 대상 url 이동 : NAVER 카페 홈   
driver.get('https://section.cafe.naver.com/ca-fe/home')
url = driver.current_url
print('접속한 url =', url)

driver.implicitly_wait(2) # 2초 대기(자원 loading)


# 3. NAVER 카페 > [인기글] 링크 클릭
element = driver.find_element(By.XPATH, '//*[@id="gnbMenu"]/a[4]')
element.click()

driver.implicitly_wait(2) # 2초 대기(자원 loading)


# ------------ 화면 스크롤바 내림 -------------------------------------------------
last_height = driver.execute_script("return document.body.scrollHeight") #현재 스크롤 높이 계산

while True: # 무한반복
    # 브라우저 끝까지 스크롤바 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    
    time.sleep(2) # 2초 대기 - 화면 스크롤 확인

    # 화면 갱신된 화면의 스크롤 높이 계산
    new_height = driver.execute_script("return document.body.scrollHeight")

    # 새로 계산한 스크롤 높이와 같으면 stop
    if new_height == last_height: 
        break
    last_height = new_height # 새로 계산한 스크롤 높이로 대체 
# -------------------------------------------------------------------------------




# 4. 인기글 요소(Element) 수집  
'''
//*[@id="mainContainer"]/div[2]/div/div[2]/div[2]/div/a/div[1]/strong : 1번 인기글 
//*[@id="mainContainer"]/div[2]/div/div[2]/div[3]/div/a/div[1]/strong : 2번 인기글 
   : 
//*[@id="mainContainer"]/div[2]/div/div[2]/div[11]/div/a/div[1]/strong : 10번 인기글 

i = 2 ~ 101 : 100개 인기글 
f'//*[@id="mainContainer"]/div[2]/div/div[2]/div[{i}]/div/a/div[1]/strong'    
'''      


strongs = []   
                
for i in range(2, 102) : # 인기글 50개 수집 -> 100개 수집  
    try :  
        strong = driver.find_element(By.XPATH, f'//*[@id="mainContainer"]/div[2]/div/div[2]/div[{i}]/div/a/div[1]/strong')
        strongs.append(strong) 
    except :
          print('xpath 오류')
       

print('수집 element 개수 =', len(strongs)) # 수집 element 개수 = 50 -> 100개  

print('---', strongs)

# 5. strong 태그 내용 수집 
strong_text = [strong.text for strong in strongs]

print(strong_text) # 인기글  
len(strong_text) # 100개 

 

driver.close() # 창 닫기










