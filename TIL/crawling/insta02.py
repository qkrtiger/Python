import requests
from bs4 import BeautifulSoup
import json

keyword = input("Enter a keyword: ")
# 인스타그램 URL
url = f"https://www.instagram.com/explore/tags/{keyword}/"

# 요청 헤더 설정 (인스타그램이 봇을 차단하지 않도록 사용자 에이전트를 설정)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# 인스타그램 페이지 요청
response = requests.get(url, headers=headers)

# 요청 성공 확인
if response.status_code == 200:
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    parent_element = soup.find('span', class_='_ac2a')
    
    if parent_element:
        # 부모 요소 내의 자식 span 요소 찾기
        child_element = parent_element.find('span')
        
        if child_element:
            # 자식 span 요소의 텍스트 추출
            post_count = child_element.text
            print(f"Number of posts for #{keyword}: {post_count}")
        else:
            print("Could not find the child span element.")
    else:
        print("Could not find the necessary script tag.")
else:
    print("Failed to retrieve the page")
