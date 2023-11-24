import requests
import json
users={}
info=10
payload={
    "results":info,
    "gender":"female",
    "nat":"US"     
}
response = requests.get("https://randomuser.me/api/",params=payload)
data = response.json()
f=open('users.json','w')
users['users']=data
users['info']=info
f.write(json.dumps(users,indent=4))
f.close()