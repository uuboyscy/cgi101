import requests
from bs4 import BeautifulSoup

url = "https://testselect.uuboyscy.repl.co/"

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
headers = {
    "user-agent": user_agent
}

data = dict()

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

intput_tag_list = soup.select('input[type="hidden"]')

print(intput_tag_list)  # [<input name="_hid_0" type="hidden" value="564328"/>, <input name="_hid_1" type="hidden" value="352167"/>, <input name="_hid_2" type="hidden" value="57483"/>]
for tag in intput_tag_list:
    # tag must be  <input name="_hid_0" type="hidden" value="564328"/>
    data[tag['name']] = tag['value']

print(data)
data['2A'] = 'dog'

print(
    requests.post(
        "https://www.w3schools.com/action_page.php",
        headers=headers,
        data=data
    ).text
)