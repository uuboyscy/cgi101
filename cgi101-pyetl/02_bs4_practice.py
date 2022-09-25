import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/photo/index.html"

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "user-agent": user_agent
}

res = requests.get(url, headers=headers)

# print(res.text)
soup = BeautifulSoup(res.text, "html.parser")

print(soup)
