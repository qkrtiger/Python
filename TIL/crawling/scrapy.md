
# 파이썬 크롤링 프레임워크 Scrapy


Scrapy는 웹 크롤링과 웹 스크래핑을 위한 강력하고 사용하기 쉬운 파이썬 프레임워크.

Scrapy는       주로 데이터를 수집하고 분석하는 데 사용되며, 빠르고 효율적인 크롤링 작업을 수행할 수 있도록 설계되았다.

### 주요 특징
1. 빠르고 효율적: Scrapy는 비동기 I/O를 사용하여 빠르고 효율적으로 웹 페이지를 크롤링한다.
2. 모듈화: 다양한 컴포넌트(스파이더, 아이템 파이프라인, 미들웨어 등)로 구성되어 있어 필요에 따라 확장하고 커스터마이징할 수 있다.
3. 간편한 데이터 추출: XPath 및 CSS 선택자를 사용하여 웹 페이지에서 쉽게 데이터를 추출할 수 있다.
4. 내장된 피드 익스포터: JSON, CSV, XML 등의 다양한 형식으로 데이터를 내보낼 수 있다.
5. 강력한 커뮤니티와 문서: 풍부한 문서와 예제, 강력한 커뮤니티를 지원한다.

### Scrapy의 기본 구조
1. 프로젝트(Project): Scrapy 작업의 기본 단위. 프로젝트 내에는 스파이더, 설정 파일, 파이프라인 등이 포함된다.
2. 스파이더(Spider): 특정 웹 사이트를 크롤링하고 데이터를 수집하는 데 사용되는 클래스. 각 스파이더는 크롤링할 도메인과 페이지를 정의하고, 데이터를 추출하는 방법을 구현한다.
3. 아이템(Item): 수집된 데이터를 구조화된 형식으로 저장하기 위한 클래스.
4. 파이프라인(Pipeline): 추출된 데이터를 처리하고 저장하는 데 사용된다. 예를 들어, 데이터를 클렌징하거나 데이터베이스에 저장하는 작업을 수행할 수 있다.
5. 미들웨어(Middleware): 요청과 응답을 처리하는 중간 단계에서 추가적인 작업을 수행할 수 있다. 예를 들어, 사용자 에이전트를 설정하거나 요청을 리다이렉트할 수 있다.

### Scrapy 사용 예제
1. Scrapy 설치
 ```sh
pip install scrapy
```

2. Scrapy 프로젝트 생성
   
```sh
scrapy startproject myproject
```

3. 스파이더 작성
  스파이더는 Scrapy의 핵심.
  myproject/spiders 디렉토리 아래에 새로운 스파이더 파일을 생성한다.
  예를 들어, quotes_spider.py 파일을 생성한다.

```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

```

5. 스파이더 실행
```sh
scrapy crawl quotes
```

7. 데이터 저장
json 포맷으로 데이터를 저장한다.

```sh
scrapy crawl quotes -o quotes.json
```
