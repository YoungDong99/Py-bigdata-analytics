# -*- coding: utf-8 -*-

# 태그 수집 코드

import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.naver.com/index.html')

soup = BeautifulSoup(res.content,'html.parser') 

titles = soup.find_all('a') 

for title in titles: 
    print(title.get_text())
