from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

def save_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    # 인스타그램 데이터 스크래핑 로직 (Selenium 사용)
    url = f"https://www.instagram.com/explore/tags/{keyword}/"
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless 모드로 실행
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get(url)
    
    # 페이지 로드 완료 대기 (필요시 적절한 대기 조건 추가)
    driver.implicitly_wait(10)  # 최대 10초 대기
    
    print('접속은 함')

    # 페이지 소스를 BeautifulSoup으로 파싱
    # soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # driver.quit()
    post_cnt_element = driver.find_element(By.XPATH, '//span[@class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs"]')
    post_cnt = post_cnt_element.text if post_cnt_element else 'No data'
    # soup_content = str(soup)
    # save_to_file(soup_content, 'soup_content.txt')
    
    # 해시태그 발행량 추출 로직 (예시)
    # post_cnt = soup.find('span', class_='html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs')
    
    # posts = soup.find('meta', {'property': 'og:description'}).get('content')
    return jsonify({'keyword': keyword, 'posts': post_cnt})

if __name__ == '__main__':
    app.run(debug=True)
