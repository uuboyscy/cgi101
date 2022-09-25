import requests
import os
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/index.html"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "user-agent": user_agent
}

if not os.path.exists("pttmovie"):
    os.mkdir("pttmovie")

for i in range(0, 5):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    # print(soup)
    title_tag_list = soup.select('div[class="title"]')
    for title_tag_obj in title_tag_list:
        if title_tag_obj.select_one('a') == None:
            continue
        title_name = title_tag_obj.select_one('a').text
        article_url = "https://www.ptt.cc" + title_tag_obj.select_one('a')["href"]

        article_res = requests.get(article_url, headers=headers)
        article_soup = BeautifulSoup(article_res.text, "html.parser")
        article_tag_obj = article_soup.select_one('div[id="main-content"]')
        article_content = article_tag_obj.text.split("※ 發信站:")[0]

        word_list = ['/', '?']
        for w in word_list:
            if w in title_name:
                title_name = title_name.replace(w, '')
        try:
            with open("pttmovie/{}.txt".format(title_name), 'w', encoding='utf-8') as f:
                f.write(article_content)
        except FileNotFoundError as e:
            # print(e.args)
            # print("pttmovie/{}.txt".format(title_name.replace('/', '-')))
            with open("pttmovie/{}.txt".format(title_name.replace('/', '-')), 'w', encoding='utf-8') as f:
                f.write(article_content)
        except OSError:
            pass

        print(title_name)
        print(article_url)
        print("=========")

    new_url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]
    print(new_url)
    url = new_url