import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/index.html"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "user-agent": user_agent
}

article_url = "https://www.ptt.cc/bbs/movie/M.1664022409.A.D11.html"

article_res = requests.get(article_url, headers=headers)
article_soup = BeautifulSoup(article_res.text, "html.parser")
article_tag_obj = article_soup.select_one('div[id="main-content"]')
article_content = article_tag_obj.text.split("※ 發信站:")[0]
# print(article_tag_obj.text.split("※ 發信站:")[0])
