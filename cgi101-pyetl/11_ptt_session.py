import requests

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "user-agent": user_agent
}

url_landing_page = "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"
url_ask_over18 = "https://www.ptt.cc/ask/over18"
url_index = "https://www.ptt.cc/bbs/Gossiping/index.html"

ss = requests.session()

print(ss.cookies)

ss.get(url_landing_page, headers=headers)

print(ss.cookies)

data = {
    "from": "/bbs/Gossiping/index.html",
    "yes": "yes"
}

ss.post(url_ask_over18, headers=headers, data=data)

print(ss.cookies)

print(
    ss.get(url_index, headers=headers).text
)





