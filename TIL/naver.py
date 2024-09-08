from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pdb
from ptpython.repl import embed
import re


# 페이지가 자동으로 새로고침될 때마다 실행될 코드
# def check_pw_value():
#     pw_input = driver.find_element(By.ID, "pw")
#     pw_value = pw_input.get_attribute("value")
#     if pw_value == '':
#         # 비밀번호 다시 전송
#         pw_input.send_keys('my-tjgus0902')


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
        print(f"팝업창이 나타나지 않음 또는 클릭 실패: {e}")
        return False

# 크롬 웹 드라이버 초기화
driver = webdriver.Chrome()

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
    
    # 팝업창이 있을 경우 닫기 버튼 클릭
    res = close_popup(driver)

    # embed(globals(), locals())
    # 카테고리 버튼 클릭(<button class="link__dkflP" data-clickcode="pgn.blogname"><i class="icon__MiNWr">카테고리 이동</i></button>)
    # cate_btn = driver.find_element(By.CLASS_NAME, "link__dkflP")
    cate_btn = driver.find_element(By.XPATH, "//button[.//span[text()='카테고리']]")
    cate_btn.click()
    
    try:
        # span 요소 중 '록'이라는 텍스트가 포함된 요소를 찾음
        span_el = driver.find_element(By.XPATH, "//span[contains(text(), '록')]")

        # 해당 span 요소의 상위 a 태그 찾기
        a_tag = span_el.find_element(By.XPATH, "./ancestor::a")

        # a 태그의 href 속성을 가져옴
        link = a_tag.get_attribute("href")
        link_arr.append(link)
        
        print("링크 주소:", link)

    except Exception as e:
        print("오류 발생:", e)
    
    # ~점이 들어간 카테고리 목록 가져오기(text__j6LKZ ell)
    # https://blog.stat.naver.com/m/blog/article/223570578441/cv
    # https://m.blog.naver.com/hi_0314/223570578441?referrerCode=1
    

# 아이디와 비밀번호 입력
id_input = driver.find_element(By.ID, 'id')
id_input.send_keys('aaaa')

pw_input = driver.find_element(By.ID, 'pw')
pw_input.send_keys('nnnn')

# 로그인 버튼 클릭
login_button = driver.find_element(By.CSS_SELECTOR, '#log\.login, .btn_global')
login_button.click()

# 페이지가 로드될 때마다 실행되도록 설정
while True:
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pw")))
        # check_pw_value()
        
        input("보안문자를 입력 후 엔터를 눌러주세요.")

        # 로그인 후 메인 페이지로 이동되었는지 확인
        if "naver.com" in driver.current_url:
            print("로그인 성공!")
            time.sleep(10)
        else:
            print("로그인 실패!")
            
    except Exception as e:
        print("페이지 로드 또는 처리 중 에러 발생:", e)
