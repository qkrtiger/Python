# 수동으로 크롬 버전을 확인하고, 그에 맞는 크롬 드라이버를 다운로드

import os
import requests
import zipfile
import winreg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def get_chrome_version():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon")
        version, type = winreg.QueryValueEx(key, "version")
        return version
    except WindowsError:
        return None

def download_chromedriver(version):
    base_url = "https://chromedriver.storage.googleapis.com"
    response = requests.get(f"{base_url}/LATEST_RELEASE_{version.split('.')[0]}")
    driver_version = response.text.strip()
    
    download_url = f"{base_url}/{driver_version}/chromedriver_win32.zip"
    response = requests.get(download_url)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    zip_path = os.path.join(script_dir, "chromedriver.zip")
    
    with open(zip_path, "wb") as f:
        f.write(response.content)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(script_dir)
    
    os.remove(zip_path)
    return os.path.join(script_dir, "chromedriver.exe")

def get_chrome_driver():
    chrome_version = get_chrome_version()
    if not chrome_version:
        raise Exception("Chrome is not installed or version could not be determined.")
    
    chrome_driver_path = download_chromedriver(chrome_version)
    
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option("detach", True)
    
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
