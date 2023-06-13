import requests

r = requests.get('http://www.google.co.kr/ttt')
print(r.status_code)