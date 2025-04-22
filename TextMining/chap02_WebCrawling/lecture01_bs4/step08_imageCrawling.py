"""
이미지 수집 & 저장하기  
"""

import urllib
from urllib.request import urlopen, urlretrieve # url 요청, 저장  
from bs4 import BeautifulSoup # 클래스 : html 파싱 
import os # 폴더 생성 및 이동

url = "https://search.naver.com/search.naver?query="

# crawler 함수 
def image_collect(query) :  # '파이썬', '데이터분석'
    # 1. url 요청 & 파싱  
    new_url = url + urllib.parse.quote(query) # new url 
    
    url_res = urlopen(new_url) # url 요청 
    byte_data = url_res.read() # byte date 
    text_data = byte_data.decode() # 디코딩 : 'utf-8' 기본값 생략 
    
    html = BeautifulSoup(text_data, 'html.parser') # html 파싱 
    
    # 2. img 태그 & 속성 가져오기 
    
    imgs = html.find_all("img", class_="img_thumb") # a 태그 모두 가져오기 
    #imgs = html.select("img[class='img_thumb']")
    # <img scr="url">
    
    
    # img url 수집 
    img_url = [] 
    for img in imgs :
        img_url.append(img.get('src'))  # imgae url 추출     
    
    
    # 3. image 저장 폴더 생성 
    path = r'C:\ITWILL\3_TextMining\workspace\chap02_WebCrawling' # 저장 경로 
    os.mkdir(path + '/' + query) # 폴더 생성 : [파이썬], [데이터분석]
    os.chdir(path + '/' + query) # 폴더 이동
        
    # 4. image save
    for i in range(len(img_url)) :
        filename = "img" + str(i+1) + ".jpg"
        # image file save
        urlretrieve(img_url[i], filename)
        
    # urlretrieve(이미지_주소, 저장_파일이름) : 해당 URL에서 이미지 다운로드, 로컬 파일에 저장

image_collect('파이썬')
image_collect('데이터분석')

