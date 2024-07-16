
## 인스타그램 태스별 게시물 수 조회

```python
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)

def extract_post_count(content):
    match = re.search(r'([\d,]+)\s*posts', content)
    if match:
        return match.group(1)
    return "N/A"

def extract_related_tags(soup):
    # 이 부분은 실제 인스타그램 페이지 구조에 따라 조정이 필요할 수 있습니다
    related_tags = soup.find_all('a', {'class': 'related_tag_class'})
    return [tag.text for tag in related_tags][:5]  # 상위 5개만 반환

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    url = f"https://www.instagram.com/explore/tags/{keyword}/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 메타 데이터에서 게시물 수 추출
        meta_content = soup.find('meta', {'property': 'og:description'})
        posts_count = extract_post_count(meta_content['content']) if meta_content else "N/A"
        
        # 연관 태그 추출 (이 부분은 실제 페이지 구조에 따라 수정이 필요합니다)
        related_tags = extract_related_tags(soup)
        
        return jsonify({
            '키워드': keyword,
            '태그별 게시물 수': posts_count,
            '연관 키워드': related_tags
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
