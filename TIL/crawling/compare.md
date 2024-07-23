## BeautifulSoup / Scrapy / Selenium 비교

| 라이브러리   | 주요 특징                                     | 장점                                                | 단점                                          |
|--------------|----------------------------------------------|-----------------------------------------------------|-----------------------------------------------|
| BeautifulSoup| HTML 및 XML 파싱                             | 사용하기 쉽고 직관적, 간단한 프로젝트에 적합         | 동적 콘텐츠 처리 불가                           |
| Scrapy       | 고성능 웹 크롤링 프레임워크                    | 대규모 크롤링에 적합, 비동기 요청 처리, 데이터 처리 파이프라인 제공 | 초기 설정이 복잡, 간단한 작업에는 다소 과할 수 있음 |
| Selenium     | 웹 브라우저 자동화 도구                        | 동적 콘텐츠 처리 가능, 실제 브라우저와 상호작용        | 속도가 느림, 리소스 소비 많음                    |

### BeautifulSoup

#### 작동방식
- HTML 가져오기: requests 라이브러리와 함께 사용하여 HTML을 가져온다.
- HTML 파싱: BeautifulSoup을 사용하여 HTML을 파싱한다.
- 데이터 추출: 파싱된 HTML에서 필요한 데이터를 탐색하고 추출

```python
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.title.text
print(title)
```

### Scrapy

#### 작동방식
- 스파이더(Spider) 정의: 크롤링 작업을 수행할 스파이더 클래스를 정의한다.
- 비동기 요청: 비동기적으로 HTTP 요청을 보내고 응답을 처리
- 데이터 파이프라인: 데이터 추출, 처리, 저장을 위한 파이프라인을 설정한다.

```python
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://example.com']

    def parse(self, response):
        title = response.xpath('//title/text()').get()
        print(title)

# Scrapy 실행 명령: scrapy runspider example_spider.py

```

### Selenium

#### 작동방식
- 브라우저 드라이버 설정: 사용할 브라우저의 드라이버를 설정한다.
- 브라우저 제어: Selenium을 사용하여 브라우저를 제어하고, 웹 페이지를 탐색한다.
- 데이터 추출: BeautifulSoup과 함께 사용하여 HTML을 파싱하고 데이터를 추출할 수 있다.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 브라우저 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless") # 창 숨기기

# 브라우저 드라이버 설정
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://example.com')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

title = soup.title.text
print(title)

driver.quit()

```
