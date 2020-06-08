import requests # https request 
import json 

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"

def get_list():
    r =requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    print(type(json.dumps(data)))
    for obj in data:
        if obj['id'] ==1:
            r2 =  requests.get(BASE_URL+ ENDPOINT + str(obj['id']))
            print(r2.json())
    return data

def create_update():
    new_data = {
        'user': 3,
        'content': 'new test',
        'image':''
    }
    r = requests.post(BASE_URL + ENDPOINT  ,new_data)
    # print(r.headers,r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

def create_update_detail():
    new_data = {
        'user': 3,
        'content': 'detail test',
        'image':''
    }
    r = requests.post(BASE_URL + ENDPOINT + "1/" ,new_data)
    # print(r.headers,r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text
# print()
# get_list()
# print(create_update())
print(create_update_detail())