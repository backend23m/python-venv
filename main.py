import requests
import json
from pprint import pprint


def get_randomuser() -> dict:
    response = requests.get('https://randomuser.me/api/')
    
    if response.status_code == 200:
        content = response.content
        data = json.loads(content.decode())
    
        randomuser = data['results'][0]
    
        user = {
            "fullname": randomuser['name']['first'] + " " + randomuser['name']['last'],
            "email": randomuser['email'],
            "phone": randomuser['phone']
        }
    
    return user

def get_randomusers(n: int) -> list:
    users = []
    for i in range(n):
        user = get_randomuser()
        users.append(user)

    result = {
        "users": users,
        "info": {"count": n}
    }
    return result

def write_data(result: dict):
    with open('users.json', 'w') as f:
        data = json.dumps(result, indent=4)
        f.write(data)

result = get_randomusers(30)
write_data(result)