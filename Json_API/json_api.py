import requests
import json
#to get the data and load the edited data (params) into the same location using json.loads
# param={"page":2,"count":4}
# r=requests.get("http://httpbin.org/get",params=param)
# print(r.status_code)
# print(r.text,type(r.text))
# print(json.loads(r.text))
# print(r.json())

# post will be made changes in forms.
# param={"username":"corey","password":"testing"}
# r=requests.post("http://httpbin.org/post",data=param)
# print(r.status_code)
# print(r.text)

# Authorization for the http(types are auth)
parm={"username":"corey","password":"testing"}
r=requests.get("http://httpbin.org/basic-auth/abcd/124",auth=('abcd','124'))
print(r.status_code)
print(r.text)