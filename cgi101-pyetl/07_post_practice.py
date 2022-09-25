import requests

url = "https://5278-13-231-145-110.ngrok.io/hello_post"

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "user-agent": user_agent
}

data = {
    "username": "sdfgtfdgcvb uyufgh"
}

res = requests.post(url, headers=headers, data=data)

print(res.text)