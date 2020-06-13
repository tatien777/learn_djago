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
        'content': 'new test'
    }
    r = requests.post(BASE_URL + ENDPOINT  ,json.dumps(new_data))
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
    r = requests.post(BASE_URL + ENDPOINT + "1/" ,data=new_data)
    # print(r.headers,r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

def do_obj_update():
    new_data = {
        "user": 3,
        'content': 'put test'
    }
    r = requests.put(BASE_URL + ENDPOINT + "15/" ,data= json.dumps(new_data) )  # json.dumps(new_data)
    # print(r.headers,r.status_code,r.json())
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

def do_obj_delete():
    new_data = {
        'id': 16
    }
    r = requests.delete(BASE_URL + ENDPOINT + "{}/".format(new_data.get('id')) )
    # print(r.headers,r.status_code,r.json())
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

def test():
    new_data = {
        'id': 14,
        'content': 'put test'
    }
    # print(BASE_URL + ENDPOINT +  "{0}/".format(new_data.id))

    print(new_data.get("id"))
    return new_data.get("id")

#### TEST 
# print()
# get_list()
# print(create_update()) # list view
# print(create_update_detail())
# print(do_obj_update()) ## put
print(do_obj_delete()) ## delete 