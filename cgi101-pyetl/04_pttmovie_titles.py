import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/index.html"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "user-agent": user_agent
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

# print(soup)
title_tag_list = soup.select('div[class="title"]')
for title_tag_obj in title_tag_list:
    if title_tag_obj.select_one('a') == None:
        continue
    title_name = title_tag_obj.select_one('a').text
    article_url = "https://www.ptt.cc" + title_tag_obj.select_one('a')["href"]
    print(title_name)
    print(article_url)
    print("=========")
