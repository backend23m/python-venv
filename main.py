import requests
import json
from pprint import pprint
users={}
n=int(input())
gender = input()
lst=[]
info=0

while info != n:
    response = requests.get('https://randomuser.me/api/')
    user={}

    if response.status_code == 200:
        content = response.content
        data = json.loads(content.decode())['results'][0]
        if data['gender']==gender:
            user["fullname"]=f"Name: {data['name']['title']} {data['name']['first']} {data['name']['last']}"
            user["number"]=f"Number: {data['phone']}"
            user['email']=f"email: {data['email']}"
            lst.append(user)
            info+=1
f=open('users.json','w')
users['users']=lst
users['info']=info
f.write(json.dumps(users,indent=4))
f.close()