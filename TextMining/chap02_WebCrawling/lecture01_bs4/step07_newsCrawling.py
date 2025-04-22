import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup

url = "http://media.daum.net" # 다음 뉴스제공 사이트 

# 1. url 요청 
res = req.urlopen(url)
data = res.read() # 한글 깨짐 


# 2. 한글 디코딩 & html 파싱
src = data.decode('utf-8')
html = BeautifulSoup(src, 'html.parser')

# 3. news 관련 url 수집  

# 1) news url 수집  
links = html.select('a[class="item_newsheadline2"]') # a 태그 수집 

print(len(links))
print(links)  # list 반환 : <a href="url"> 내용 </a>
print(type(links))
'''
<class 'bs4.element.ResultSet'>
BeautifulSoup의 특수한 리스트 타입
-> "HTML 요소들이 들어 있는 리스트"
'''

# 2) url 추출   
urls = [] 

for link in links :
    url = link.get('href')  # get('속성') -> 값
    urls.append(url)    # 주소만 추출해서 리스트 담기
print(urls)
len(urls)
'''
'https://v.daum.net/v/20250415153308136',
,
'https://v.daum.net/v/20250415142759373'
'''


# 4. crawler 함수 정의
def crawler_fn(url): # 페이지 고정
    print('url :', url)
    try :
        # 1. url 요청 
        res = req.urlopen(url)
        data = res.read()
        
        # 2. html 파싱
        src = data.decode('utf-8') 
        html = BeautifulSoup(src, 'html.parser')        
        
        # 3. 제목 수집  : <h3 class="tit_view"> 내용 </h3>
        title = str(html.select_one('h3[class="tit_view"]').text).strip()
        # str로 감싸는 이유 : 예외 상황에서 확실하게(에러없이) 문자열로 바꾸기 위해
        
        # 4. 내용 수집 : list 반환
        article = html.select('div.news_view > div.article_view > section > p')
        
        # 여러개 문단(p) -> 한 개의 변수로 텍스트 누적 
        conts = ""
        for p in article :
            text = str(p.text).strip()
            conts += text + "\n" # 텍스트 누적
    except Exception as e:  
        print('예외 발생 :', e) 
        
    return title, conts 


# 함수 호출
titles = []
news = []

for url in urls :
    title, conts = crawler_fn(url)  # 함수 호출
    titles.append(title)  # 제목 저장
    news.append(conts)  # 뉴스 내용
    
len(titles)
len(news)

print(news[4])


# 5. file csv save
import pandas as pd

# 제목과 본문 리스트를 한 줄씩 짝지어 표 형태의 데이터프레임으로 만들기
daum_news = pd.DataFrame({'title' : titles, 'news' : news})



daum_news.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 21 entries, 0 to 20
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   title   21 non-null     object
 1   news    21 non-null     object
dtypes: object(2)
memory usage: 468.0+ bytes
'''

# 앞부분 데이터 상위 5개 행 미리보기
daum_news.head()


path = r'C:\ITWILL\3_TextMining\data'

# 데이터프레임을 CSV 파일로 저장하기
daum_news.to_csv(path + '/daum_news.csv', index = None)  # 행 번호 생략







