import requests
import json
def get_user():
    response=requests.get("https://randomuser.me/api/")
    if response.status_code==200:
        content=response.content
        data=json.loads(content.decode())
        randomuser=data["results"][0]
        return randomuser
def get_users(gender,n):
    a=[]
   
    while len(a)<n:
        user=get_user()
        if user["gender"]==gender:
            a.append(user)
    users={
        "users":a,
        "info":{"count":n}
    }
    return users
def write_data(dic):
    with open ("users.json", "w") as s:
        data=json.dumps(dic, indent=4)
        s.write(data)

data=get_users("male", 20)
write_data(data)
