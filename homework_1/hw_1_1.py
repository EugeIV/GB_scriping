import json
import requests
import os
# from dotenv import load_dotenv
# load_dotenv()

url = 'https://api.github.com'
user = 'EugeIV'
# user = os.getenv('USER', None)


def repo_list(ur, us):
    lst = []
    r = requests.get(f'{url}/users/{user}/repos')

    with open('data.json', 'w') as f:
        json.dump(r.json(), f)

    for i in r.json():
        lst.append(i['name'])

    return lst


print(repo_list(ur=url, us=user))
