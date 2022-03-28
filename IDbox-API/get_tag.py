import requests
import json

#url = "https://ptt-dev.idboxrt.com/api/token"
url = "http://idbox-ineos-local/api/token"

payload = "grant_type=password&username=root&password=root!"
headers = {
    'cookie': "__cfduid=d5df7fa290f8aa8399f41406756ef21441605173952",
    'Content-Type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print('response.status_code', response.status_code)

print('response', response)

if response.status_code == 200:
    token_obj = response.json()
    print('\n access_token : ',     token_obj["access_token"])
    print('\n token_type : ',       token_obj["token_type"])
    print('\n expires_in : ',       token_obj["expires_in"])
    print('\n refresh_token : ',    token_obj["refresh_token"])

