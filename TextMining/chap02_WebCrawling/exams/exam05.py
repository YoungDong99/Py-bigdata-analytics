"""
문5) 이미지 url 추출 & 파일 저장 
   
  중급수준 : 네이버 검색 페이지에서 검색어를 입력하면 검색 페이지로 이동된다. 
            이때 [이미지] 링크를 클릭하여 이미지 검색페이지로 이동한 후 
            첫번째 이미지를 기준으로 이미지 10개에 해당하는 이미지 url를
            반환하는 함수를 완성하시오.
          
  고급수준 : 수집한 이미지 url을 이용하여 특정 폴더에 파일로 저장하시오.      
"""

import urllib # quote
from selenium import webdriver # 드라이버 
from urllib.request import urlretrieve # image 파일 저장 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자
from selenium.webdriver.common.keys import Keys # 엔터키 역할 
from selenium.webdriver.common.by import By # 로케이터(locator) 

import os
import time # 화면 일시 정지


# 태그 수집 함수 
def image_collect(query) :
    
    # 1. driver 생성 
    driver_path = ChromeDriverManager().install() # 드라이버 설치 경로 
    correct_driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe") # 실행파일경로 
    driver = webdriver.Chrome(service=Service(executable_path=correct_driver_path)) # 드라이버 생성 
    
    
    # 2. new url 이동 : new_url = 기본 url + 검색어 
    url = "https://search.naver.com/search.naver?query=" # 기본 url 
    new_url = url + urllib.parse.quote(query) # 한글과 URL 결합
    
    driver.get(new_url)
    time.sleep(3)
    
    
    # 3. [이미지] 링크 클릭 -> 이미지 검색 페이지 이동  
    img_tab = driver.find_element(By.LINK_TEXT, '이미지')
    img_tab.send_keys(Keys.ENTER)
    time.sleep(3)
    
    
    # 4. 이미지 10개 수집         
    images = []
    for i in range(1, 11) :
        try :
            img = driver.find_element(By.XPATH, f'//*[@id="main_pack"]/section/div[1]/div/div/div[1]/div[{i}]/div/div/div/img')
            images.append(img)
        except :
            print('xpath 오류')
    
    print('수집 images 개수 =', len(images)) 
    
    # 5. image url 추출 
    img_urls = []
    for img in images :
        img_urls.append(img.get_attribute('src'))
    
    
    # 6. image 저장 폴더 생성 
    path = r'C:\ITWILL\3_TextMining\workspace\chap02_WebCrawling' # 저장 경로 
    os.mkdir(path + '/selenium_' + query) # 폴더 생성 : [sel_데이터분석]
    os.chdir(path + '/selenium_' + query) # 폴더 이동 
    
    
    # 7. image save
    for i in range(len(img_urls)) :
        file_name = "img" + str(i+1) + ".jpg"
        urlretrieve(img_urls[i], file_name)
        
    driver.close()
    
    return img_urls
    


# 함수 호출 
query = input('검색어 입력 : ') 
img_urls = image_collect(query)

print(img_urls)

img_urls[0] # 1번 이미지 url 
img_urls[-1] # 10번 이미지 url 








