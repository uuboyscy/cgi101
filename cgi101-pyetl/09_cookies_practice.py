import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "user-agent": user_agent
}

cookies = {
    "over18": "1"
}
res = requests.get(url, headers=headers, cookies=cookies)

print(res.text)