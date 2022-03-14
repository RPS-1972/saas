


import requests


user =  "user"
pwd =  "rOgxCEVL6O"




ip = "af55a8117bffd4bc3bd6e87e366b680e-165648227.ap-southeast-1.elb.amazonaws.com"


url = f"http://{user}:{pwd}@{ip}/asynchPeople/api/xml?depth=1"



# https://<yourjenkins>/asynchPeople/api/xml?depth=1

# payload = 'json={}'
headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }



# response = requests.post(url, headers=headers, data=payload)

response = requests.get(url, headers=headers)






print("ACTUAL RESPONSE FROM API")
print("------------------------")
print(resp)