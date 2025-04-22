'''
 문4) step04_google_search.py에서 작성한 아래 내용을 다음 조건에 맞게 함수로 
     정의하고 정의된 함수를 호출하여 실행결과를 확인하시오. 
       
   <조건1> 함수명과 인수 : googleSearch(searchword)
   <조건2> 함수 반환 :  h3 태그의 내용을 리스트로 저장하여 반환  
   <조건3> 다음 검색어 목록의 각 검색어로 자료를 수집하여 중첩리스트에 저장 
           searchword_list = ['머신러닝','통게분석','SQL']    
'''

from selenium import webdriver # driver 
#from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자  
from selenium.webdriver.common.by import By # 요소 선택 
from selenium.webdriver.common.keys import Keys # 엔터키 역할
from selenium.webdriver.chrome.options import Options # driver options생 성 

import os
import time 


def googleSearch(searchword) :
    driver_path = ChromeDriverManager().install()
    correct_driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe")
    
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://www.google.com/")
     
    elem = driver.find_element(By.NAME, "q")

    elem.send_keys(searchword) # 검색어 입력 
    elem.send_keys(Keys.ENTER) # 엔터 키  
    time.sleep(3)
    
    heads = driver.find_elements(By.TAG_NAME, "h3")  
    print('수집 head 개수 =', len(heads))
    
    head_text = []
    for head in heads :        
        head_text.append(head.text)
    
    driver.close()
    
    return head_text


searchword_list = ['머신러닝','통게분석','SQL']  

result = [googleSearch(word) for word in searchword_list]

print(result)
