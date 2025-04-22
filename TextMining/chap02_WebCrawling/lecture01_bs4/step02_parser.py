"""
웹문서 파싱(parsing)
 - HTML의 웹문서에서 태그나 속성 등을 추출하고 처리할 수 있도록 DOM구조로 변환하는 과정
"""

from bs4 import BeautifulSoup


path = r'C:\ITWILL\3_TextMining\data' # 파일 경로 


# 1. HTML 문서 파싱 

# 1) 로컬 파일 읽기 
file = open(path + '/html_sample.html', mode='r', encoding='utf-8')
html_doc = file.read() 
file.close()

'''
디코딩 과정 생략 
'''

# 2) html 파싱
html = BeautifulSoup(html_doc, 'html.parser')  # html 문서 파싱
print(html)

# a 태그 전체 찾기 
a_tags = html.find_all('a')
print(a_tags) # list

for a in a_tags : 
    print(a.string)

    
# 2. XML(Extensible Markup Language) 문서 파싱     
file = open(path + '/xml_sample.xml', mode='r', encoding='utf-8')
xml_doc = file.read() 
file.close()
print(xml_doc)    
    

# XML 파싱
xml = BeautifulSoup(xml_doc, 'xml')

items = xml.find_all('item')  # list 반환

print(items)
## 출력결과 : [<item id="1">Item 1</item>, <item id="2">Item 2</item>, <item id="3">Item 3</item>]

print(xml.text)
## 출력결과 :
# Item1
# Item2
# Item3

