from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time
from ptpython.repl import embed
import re

def close_popup(driver, wait_time=10, class_name="_da-close"):
    """
    팝업창이 있을 경우 닫기 버튼을 클릭하는 함수.
    
    Parameters:
    driver (webdriver): Selenium WebDriver 인스턴스
    wait_time (int): 닫기 버튼을 기다릴 최대 시간 (초)
    class_name (str): 닫기 버튼의 클래스 이름

    Returns:
    bool: 닫기 버튼이 나타나고 클릭이 성공하면 True, 아니면 False
    """
    try:
        # 지정된 클래스 이름으로 닫기 버튼을 기다리고 클릭
        close_button = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
        close_button.click()
        print("팝업창 닫기 성공")
        return True
    except Exception as e:
        # print(f"팝업창이 나타나지 않음 또는 클릭 실패: {e}")
        print(f"팝업창이 나타나지 않음 또는 클릭 실패:")
        return True

# Chrome 설정 옵션
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu") # 그래픽 가속 비활성화
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-images")  # 이미지 로드 방지
# chrome_options.add_argument("--disable-javascript") # 자바스크립트 로드 방지
# chrome_options.add_argument("--headless")  # Headless 모드로 실행하고 싶으면 추가

# ChromeDriver 자동 설치 및 설정
service = Service(ChromeDriverManager().install())

# ChromeDriver와 옵션으로 WebDriver 객체 생성
driver = webdriver.Chrome(service=service, options=chrome_options)

# 네이버 로그인 페이지로 이동
driver.get("https://nid.naver.com/nidlogin.login")

input("로그인 후 엔터를 눌러주세요.")

try:
    # 검색창이 로드될 때까지 기다림
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "query"))
    )
    
    email_div = driver.find_element(By.CLASS_NAME, "MyView-module__desc_email___JwAKa")
    email_text = email_div.text
    
    match = re.match(r"(.+)@naver\.com", email_text)
    user_id = match.group(1) if match else None

    print("user_id", user_id)
    
except Exception as e:
    print("검색창이 나타나지 않음:", e)

link_arr = []
if user_id:
    driver.get(f"https://m.blog.naver.com/{user_id}")
    
    # embed(globals(), locals())
    # 팝업창이 있을 경우 닫기 버튼 클릭
    res = close_popup(driver)

    # 카테고리 버튼 클릭(<button class="link__dkflP" data-clickcode="pgn.blogname"><i class="icon__MiNWr">카테고리 이동</i></button>)
    # cate_btn = driver.find_element(By.CLASS_NAME, "link__dkflP")
    if res:
        cate_btn = driver.find_element(By.XPATH, "//button[.//span[text()='카테고리']]")
        cate_btn.click()
    
    try:
        # span 요소 중 '록'이라는 텍스트가 포함된 요소를 찾음
        # span_el = driver.find_element(By.XPATH, "//span[contains(text(), '점')]")
        # # 해당 span 요소의 상위 a 태그 찾기
        # a_tag = span_el.find_element(By.XPATH, "./ancestor::a")
        # # a 태그의 href 속성을 가져옴
        # link = a_tag.get_attribute("href")
        # link_arr.append(link)
        # span 요소들 중 텍스트를 하나씩 확인
        
        time.sleep(2)
        # li_els = driver.find_elements(By.XPATH, "//li[@class='item__axzBh']")
        li_els = driver.find_elements(By.XPATH, "//div[contains(@class, 'category_list__VviwZ')]//li[@class='item__axzBh']")        
        
        for li_el in li_els:
            full_html = li_el.get_attribute('outerHTML')
            # li_el 내부에 있는 class가 'text__j6LKZ ell'인 span 태그를 찾기
            span_el = li_el.find_element(By.XPATH, ".//span[@class='text__j6LKZ ell']//span")
            soup = BeautifulSoup(full_html, 'html.parser')
            
            # span의 텍스트 가져오기
            text = span_el.text.strip()
            if text.endswith("점"):
                print("텍스트:", text)
                a_tag = soup.find('a', {'class': 'link__dkflP'})
                if a_tag:
                    link = a_tag['href']
                    print("링크:", link)
                    link_arr.append(link)
                
                # a_tag = full_html.find_element(By.XPATH, "./ancestor::a")
                # link = a_tag.get_attribute("href")
                
        print("링크 주소:", link_arr)
        
        # embed(globals(), locals())
        # url_arr = []
        for link in link_arr:
            
            url = f"https://m.blog.naver.com{link}"
            driver.get(url)
            
            close_popup(driver)        
            
            # response = requests.get(url)
            # soup = BeautifulSoup(response.text, 'html.parser')
            li_els = driver.find_elements(By.XPATH, "//div[contains(@class, 'list__A6ta5')]//li[@class='item__axzBh']")
            
            for li_el in li_els:
                
                full_html = li_el.get_attribute('outerHTML')
                soup = BeautifulSoup(full_html, 'html.parser')
                
                a_tag = soup.find('a', {'class': 'link__dkflP'})
                if a_tag:
                    link = a_tag['href']
                    print("링크:", link)
                    driver.get(link)
                    try:
                        # '통계' 버튼이 나타날 때까지 최대 10초 대기
                        stat_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'btn_stat')]"))
                        )
                        
                        # 포스팅 제목 가져오기
                        element = driver.find_element(By.ID, "_floating_menu_property")
                        title = element.get_attribute("posttitle")
                        
                        # '통계' 버튼의 href 속성값 추출
                        stat_url = stat_button.get_attribute('href')
                        # print(f"'통계' 버튼 URL: {stat_url}")
                        # stat_button.click()
                        driver.get(stat_url)
                        monthly_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='월간']/parent::a")))
                        monthly_link.click()
                        
                        view = driver.find_element(By.XPATH, "//span[text()='조회수']/following-sibling::div//strong").text
                        
                        # embed(globals(), locals())
                        
                        with open('view_review.txt', 'w', encoding='utf-8') as out:
                            out.write(f"{link}\t{title}\t{view}\n")
                        

                    except Exception as e:
                        print(f"요소를 찾는 중 문제가 발생했습니다: {e}")
                    # url_arr.append(link)
                
            # list_container = soup.find('li', class_='item__PxpH8')
            # 그 안에 있는 'item__axzBh' 클래스를 가진 모든 요소를 리스트화
            # items = list_container.find_all('li', class_='item__axzBh')
            
            
        
    except Exception as e:
        print("오류 발생:", e)
    
# # 검색창 찾기, 검색어 입력 및 검색
# search_box = driver.find_element("name", "q")
# search_box.send_keys("M1 Mac Selenium automatic ChromeDriver update")
# search_box.submit()

# # 결과 출력
# print(driver.title)

# # 브라우저 종료
# driver.quit()
