'''
태그 속성값 가져오기

태그 = 요소(element) : <시작태그 속성="값"> 내용 </종료태그>
    예) <a href="http://www.naevr.com"> 네이버 </a>
'''

from bs4 import BeautifulSoup

path = r'C:\ITWILL\3_TextMining\data' # 파일 경로 

# 1. 로컬 파일 불러오기 or 원격서버 url 요청  
file = open(path + '/html02.html', mode='r', encoding='utf-8')
src = file.read()


# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)


# 3. a태그 가져오기 
links = html.find_all('a') # list
print(links)

type(links[0])  # bs4.element.Tag


# 4. href 속성값 가져오기 

for a in links :
    print(a.get('href')) # url 수집 

# 리스트에 담기
urls = [a.get('href') for a in links]
print(urls)

# 5. 정규표현식으로 url 중에서 'http://' 시작하는 url만 추출   
import re

url_pat = re.compile('^http://')

dir(url_pat)
'''
findall
match
search
'''

new_urls = []  # 정상 url

for url in urls :
    result = url_pat.match(url)
    #print(result)  # None : 해당변수 값이 없음(null)
    
    if result :
        new_urls.append(url)

print(new_urls)

# 중복 url 제외
new_urls = list(set(new_urls))
print(new_urls)





        
        
        
        
        
        
