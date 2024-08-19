#https://api.result -api-dev/objects

import requests


headers={'content-type':'application/Json'}
response=requests.get('https://api-github.com')
print(response)

con_var=rsponse.content
print(con_var)
data=response.Json()
print(data)
#print(type(response.content))

for key,value in data.items():
    #print(key,data['issue_url'])
    print(key,'*******',value)




