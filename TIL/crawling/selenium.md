```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 웹 드라이버 설정 (Chrome 사용 예시)
driver = webdriver.Chrome('/path/to/chromedriver')

try:
    # 웹 페이지 열기
    driver.get("https://www.example.com")

    # 요소 찾기 및 상호작용
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    # 명시적 대기 - 특정 요소가 로드될 때까지 기다림
    wait = WebDriverWait(driver, 10)
    results = wait.until(EC.presence_of_element_located((By.ID, "results")))

    # 결과 출력
    print(results.text)

finally:
    # 브라우저 닫기
    driver.quit()
```
