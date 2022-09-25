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

# print(soup)
# logo_tag_list = soup.findAll('a', {'id': 'logo'})
# logo_tag_list = soup.findAll('a', class_='logo')
logo_tag_list = soup.findAll('a', id='logo')
print(logo_tag_list[0])  # Tag object
print(logo_tag_list[0].text)
print("https://www.ptt.cc" + logo_tag_list[0]["href"])

print("===================")

title_tag_list = soup.select('div[class="title"]')
print(title_tag_list)

'''
<div class="title">
<a href="/bbs/photo/M.1660991759.A.8F6.html">[作品] 生活在台南</a>
</div>
'''
print(title_tag_list[0])  # Tag object
# title_detail_tag = title_tag_list[0].select_one('a')
title_detail_tag = title_tag_list[0].find('a')
print(title_detail_tag)

print(type(title_tag_list[0]))
print(type(soup))

