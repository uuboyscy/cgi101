from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# url = "https://5278-13-231-145-110.ngrok.io/hello_get?name=Allen"
url = "https://www.ptt.cc/bbs/photo/index.html"

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "User-Agent": user_agent
}

req = request.Request(url=url, headers=headers)

# res = request.urlopen(url=url)
res = request.urlopen(req)

print(res.read().decode("utf-8"))