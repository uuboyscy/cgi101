import requests

request_body = {
    "username": "Allen"
}

res = requests.post(
    "http://localhost:5001/hello_post",
    data=request_body
)

print(res.text)