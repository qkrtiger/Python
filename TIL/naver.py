from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pdb


# 페이지가 자동으로 새로고침될 때마다 실행될 코드
def check_pw_value():
    pw_input = driver.find_element(By.ID, "pw")
    pw_value = pw_input.get_attribute("value")
    if pw_value == '':
        # 비밀번호 다시 전송
        pw_input.send_keys('my-tjgus0902')


# 크롬 웹 드라이버 초기화
driver = webdriver.Chrome()

# 네이버 로그인 페이지로 이동
driver.get("https://nid.naver.com/nidlogin.login")
pdb.set_trace()

input("로그인 후 엔터를 눌러주세요.")

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
        check_pw_value()
        
        input("보안문자를 입력 후 엔터를 눌러주세요.")

        # 로그인 후 메인 페이지로 이동되었는지 확인
        if "naver.com" in driver.current_url:
            print("로그인 성공!")
            time.sleep(10)
        else:
            print("로그인 실패!")
            
    except Exception as e:
        print("페이지 로드 또는 처리 중 에러 발생:", e)
