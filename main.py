import requests
import json

response = requests.get('https://randomuser.me/api/')

if response.status_code == 200:
    content = response.content
    data = json.loads(content.decode())

    user = {
        "fullname": data['results'][0]['name']['first'] + " " + data['results'][0]['name']['last']
    }
    print(user)
