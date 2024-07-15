
## 인스타그램 태스별 게시물 수 조회

```python
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    # 인스타그램 데이터 스크래핑 로직
    url = f"https://www.instagram.com/explore/tags/{keyword}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # 해시태그 발행량 추출 로직 (예시)
    posts = soup.find('meta', {'property': 'og:description'}).get('content')
    return jsonify({'태그별 게시물 수': keyword, 'posts': posts})

if __name__ == '__main__':
    app.run(debug=True)
```

## 프로그램 실행 방법

1. 프로젝트 디렉터리 내에서 가상환경 생성
```bash
python -m venv venv
```

2. 가상 환경 활성화
```bash
source venv/bin/activate
```

3. 필요 패키지 설치
```bash
pip install Flask beautifulsoup4 requests
```

4. Flask 애플리케이션 실행
```bash
python main.py
```

5. 웹 브라우저에서 테스트

`http://127.0.0.1:5000/search?keyword=your_keyword`


## 관련 명령어

```
터미널에서 가상 환경 비활성화
deactivate

가상환경 완전히 삭제
rm -rf venv
```
