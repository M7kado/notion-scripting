import requests
from secrets import auth_token

from client import Client

# url = "https://api.notion.com/v1/pages/791923b871ad415c9454bdd385edb727"

# headers = {
#     "accept": "application/json",
#     "Notion-Version": "2022-06-28",
#     "Authorization": f'Bearer {auth_token}'
# }

# body = {
#     "properties" : {
#     'title': {'title': [{'text': {'content': 'test !'}}]}}
# }

# print(headers)

# #response = requests.get(url, headers=headers)
# response = requests.patch(url, headers=headers, json=body)

# outputjson = response.json()

# print(response.text)

client = Client(auth_token)

page = client.get_page("791923b871ad415c9454bdd385edb727")

print("old title: ", page.title)
print("changing title...")
page.title = "Updated title !"
print("new title: ", page.title)

pass