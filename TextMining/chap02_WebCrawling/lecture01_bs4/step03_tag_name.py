'''
 <태그 이용 자료 수집>
1. tag 계층구조 이용  
2. find('태그') 함수 이용  
3. find_all('태그') 함수 이용  
'''

from bs4 import BeautifulSoup  # html 파싱

path = r'C:\ITWILL\3_TextMining\data' # 파일 경로 

# 1. 로컬 파일 읽기 
file = open(path + '/html01.html', mode='r', encoding='utf-8')
text_data = file.read()  # 처음부터 끝까지 문자열로 반환
print(text_data)
file.close()

# 2. html 파싱
html = BeautifulSoup(text_data, 'html.parser')
print(html)


# 3. 태그 내용 수집 

# 1) tag 계층구조 찾기
h1 = html.html.body.h1 # DOM 구조 node 접근  : 1) tag
print('h1 : ', h1.string) # h1 :   시멘틱 태그 ?  : 2) 내용

# 2) find()함수 : 태그 찾기 
h2 = html.find('h2')
print('h2 : ', h2.string) # h2 :   주요 시멘틱 태그
type(h2)  # bs4.element.Tag

# 3) find_all('태그')
lis = html.find_all('li')  # list로 반환 
print(lis)
len(lis)

'''
conts = []
for li in lis :
    cont = li.string  # tag의 내용 수집
    conts.append(cont)
'''

# 리스트 내포
conts = [li.string for li in lis]
print(conts)


