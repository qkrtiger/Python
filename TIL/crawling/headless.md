
#### Selenium을 사용하여 숨김 모드로 Chrome 브라우저를 실행한다. 

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def search_instagram_hashtags(keyword):
    # Chrome 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 브라우저를 숨김 모드로 실행
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # ChromeDriver 경로 설정
    driver_path = '/path/to/chromedriver'  # ChromeDriver 경로를 설정합니다.
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    try:
        # 인스타그램 로그인 페이지로 이동
        driver.get('https://www.instagram.com/accounts/login/')

        # 로그인 (여기에 인스타그램 로그인 정보를 입력하세요)
        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        username.send_keys('your_username')
        password.send_keys('your_password')
        password.send_keys(Keys.RETURN)

        # 로그인 완료 대기
        time.sleep(5)

        # 검색창으로 이동
        search_url = f'https://www.instagram.com/explore/tags/{keyword}/'
        driver.get(search_url)

        # 데이터 로딩 대기
        time.sleep(5)

        # 게시물 수 추출
        posts_count = driver.find_element(By.XPATH, '//span[contains(text(), "posts")]')
        print(f"해시태그 '{keyword}'에 대한 게시물 수: {posts_count.text}")

    except Exception as e:
        print(f"오류 발생: {e}")

    finally:
        # 드라이버 종료
        driver.quit()

# 프로그램 실행
if __name__ == "__main__":
    keyword = input("검색할 해시태그를 입력하세요: ")
    search_instagram_hashtags(keyword)

```
