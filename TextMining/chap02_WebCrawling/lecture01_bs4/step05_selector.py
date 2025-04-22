"""
<선택자(selector) 이용 자료 수집>
 1. select_one('id선택자')함수 이용 
 2. select('class선택자')함수 이용    
"""

from bs4 import BeautifulSoup # html 파싱 

path = r'C:\ITWILL\3_TextMining\data' # 파일 경로 

# 1. html source 가져오기 
file = open(path + '/html03.html', mode='r', encoding='utf-8')
src = file.read()
print(src)
file.close()

# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)
dir(html)
'''
find() : 태그
find_all() : 태그
select() : 태그 or #id or .class : 여러 개 태그 list 반환
select_all() : 태그 or #id or .class : 1개 태그 반환
'''


# 3. 선택자 이용 태그 내용 가져오기 

# 1) id 선택자
print('>> table 선택자 <<') 
table = html.select_one('#tab') # 1개 tag 수집 
print(table)  
    

# 2) class 선택자 : class='odd'
trs = html.select(".odd")  # 여러개 tag 수집 
print(trs)


# 1행 반환
for tr in trs :
    tds = tr.find_all('td')
    for td in tds :
        print(td.string)





# 형식) select("태그[속성='속성값']") 
trs = html.select("tr[class='odd']") 
print(trs)


# 3) 계층적 선택자 
ths = html.select('#tab > tr > th') 
print(ths) # list

for th in ths :
    print(th.string)


