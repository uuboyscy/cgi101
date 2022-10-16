import sys
sys.path = sys.path + ['', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload', '/Users/uuboy.scy/PycharmProjects/cgi101/venv/lib/python3.8/site-packages', '/Users/uuboy.scy/PycharmProjects/cgi101/venv/lib/python3.8/site-packages/setuptools-40.8.0-py3.8.egg', '/Users/uuboy.scy/PycharmProjects/cgi101/venv/lib/python3.8/site-packages/pip-19.0.3-py3.8.egg']

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time


service = Service("./chromedriver")
driver = Chrome(service=service)

url = 'https://www.ptt.cc/bbs/index.html'

driver.get(url)

driver.find_element(by=By.CLASS_NAME, value='board-name').click()
driver.find_element(by=By.CLASS_NAME, value='btn-big').click()

cookie = driver.get_cookies()

#[{'domain': 'www.ptt.cc', 'httpOnly': False, 'name': 'over18', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.ptt.cc', 'expiry': 1665907193, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.ptt.cc', 'expiry': 1665993534, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.600065558.1665907133'}, {'domain': '.ptt.cc', 'expiry': 1700467134, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2026779270.1665907133'}]
print(cookie)

ss = requests.session()

# 設定cookies
for c in cookie:
    ss.cookies.set(c['name'], c['value'])

res = ss.get('https://www.ptt.cc/bbs/Gossiping/index.html')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())
