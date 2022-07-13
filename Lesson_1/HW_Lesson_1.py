import requests
from pprint import pprint
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
url = "https://api.github.com/users/PaninaNastya/repos"

response = requests.get(url, headers=headers)
j_data = response.json()

print(list((object['name'] for object in j_data)))

with open('data.txt', 'w') as outfile:
    json.dump(j_data, outfile)