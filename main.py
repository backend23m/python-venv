import requests
import json

response = requests.get('https://randomuser.me/api/')

if response.status_code == 200:
    content = response.content
    data = json.loads(content.decode())

    randomuser = data['results'][0]

    user = {
        "fullname": randomuser['name']['first'] + " " + randomuser['name']['last'],
        "email": randomuser['email']
    }
    print(user)
