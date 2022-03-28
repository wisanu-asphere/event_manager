# import requests
# import json

# GJ8mkOKFT_5ATg5UKGZ7wBgfQuh7MkXQe_2Wb6wdnU2La-TzC7XmntgaieJVs61w2-zaRufaEI951xVTr-5dhIkhVJLoGFN3v5_wtlySo1oeKDUH4KLL0HkXP7DFcyb9qzURSBRUGbbeC8tmM_QfRMPdYilDy-84uSWgBr9X5Q2t5mXYDXKU0D79rHMXJUu4y5gnNy-oJBzo7FtRI92b_w
#url = "https://ptt-dev.idboxrt.com/api/token"

url = "http://idbox-ineos-local/api/token"
import requests
import json
import time

url_token = "http://idbox-ineos-local/api/token"
payload_token = "grant_type=password&username=root&password=root!"
headers_token = {
    'cookie': "__cfduid=d5df7fa290f8aa8399f41406756ef21441605173952",
    'Content-Type': "application/x-www-form-urlencoded"
    }

while True:
    time.sleep(1)
    response = requests.request("GET", url_token, data=payload_token, headers=headers_token)
    while response.status_code != 200:
        print(' response is ',response.status_code)
        time.sleep(1)
    if response.status_code == 200:
        token_obj = response.json()
        token_txt = token_obj["access_token"]
        # print(token_txt)
        # print('\n')
        url = "http://idbox-ineos-local/api/v1/data/real-time/"
        tag_name = ['A01', 'A02', '05FC101-04', '05FC101-04.IVP']
        payload = ""
        headers = {
            'cookie': "__cfduid=d5df7fa290f8aa8399f41406756ef21441605173952",
            'Authorization': "Bearer " + token_txt,
            'Security-Group': "1"
            }
        for tag in tag_name:
            url_get = url+tag
            # print(url_get)
            response = requests.request("GET", url_get, data=payload, headers=headers)
            while response.status_code != 200:
                pass
            if response.status_code == 200:
                tag_obj = response.json()
                row_print = url_get + '    tag : ' + tag_obj['tag'] + '    value : ' + str(round(tag_obj['value'],2)) + '    timestamp : ' + tag_obj['timestamp']
                print(row_print)
    print('----------------------------------------------------------------------------------------------------------------------------------------------')



# url = "https://ptt-dev.idboxrt.com/api/v1/signals/signals/2"

# payload = ""
# headers = {
#     'cookie': "__cfduid=d5df7fa290f8aa8399f41406756ef21441605173952",
#     'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJyb290IiwibmJmIjoxNjA1NjcxODg4LCJleHAiOjE2MDU2NzM2ODgsImlhdCI6MTYwNTY3MTg4OCwiaXNzIjoiaHR0cHM6Ly9wdHQtZGV2LmlkYm94cnQuY29tL2xvZ2luIiwiYXVkIjoiSURib3hSVCJ9.9bOqi5DuosNbZ5RYoviMJBPhqOsqF9jdwJHKf3ECsE8",
#     'Security-Group': "1"
#     }

# tag_name = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10']

# for tag in tag_name:
#     print('\n tag : ', tag)



'''
response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)

if response.status_code == 200:
    tag_obj = response.json()
    print('\n id : ',     tag_obj["id"])
    print('\n minValue : ',       tag_obj["token_type"])
    print('\n minValue : ',       tag_obj["minValue"])
    print('\n maxValue : ',    tag_obj["maxValue"])

'''

# import requests
# import json

# url = "https://ptt-dev.idboxrt.com/api/token"

# payload = "grant_type=password&username=root&password=root!"
# headers = {
#     'cookie': "__cfduid=d5df7fa290f8aa8399f41406756ef21441605173952",
#     'Content-Type': "application/x-www-form-urlencoded"
#     }

# response = requests.request("POST", url, data=payload, headers=headers)

# print('response.status_code', response.status_code)

# print('response', response)

# if response.status_code == 200:
#     token_obj = response.json()
#     print('\n access_token : ',     token_obj["access_token"])
#     print('\n token_type : ',       token_obj["token_type"])
#     print('\n expires_in : ',       token_obj["expires_in"])
#     print('\n refresh_token : ',    token_obj["refresh_token"])

