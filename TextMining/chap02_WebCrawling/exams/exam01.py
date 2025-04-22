'''
 문1) css_example.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오. 
    <조건> 제목열을 지정하는 <th> 태그의 모든 내용 출력
    
   <출력 결과>
    학번
    이름
    학과
    이메일 
'''

from bs4 import BeautifulSoup


path = r'C:\ITWILL\3_TextMining\data'


# 1. 파일 읽기 
file = open(path + "/css_example.html", mode='r', encoding='utf-8')
source = file.read()
file.close()

print(source)

# 2. html 파싱
html = BeautifulSoup(source, 'html.parser')
print(html)

dir(html)
'''
find('tag')
find_all('tag')
get('속성')
string
text
'''

# 3. 태그 찾기 
ths = html.find_all('th')
print(ths)

# 4. 태그 내용 출력 
for th in ths :
    print(th.string)






