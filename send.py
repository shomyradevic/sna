from requests import post, get, put, patch, delete, ConnectionError as RequestConnectionError
from datetime import datetime


refresh = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4MzY2MjEwOCwianRpIjoiMzE4OGZjMDg2YTllNDM1YzlmMmE2MmNhMjcwNzRhMDUiLCJ1c2VyX2lkIjo0NX0.i0FXlmo_DK9xaNwRMDzLld40L64Woad3qDnxMMnxgwQ'
access = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzNzUzMzE1LCJqdGkiOiIxM2E0ZTBmZTlhODE0ODg5OTlkMTZiOTA4Y2MwMjU1YiIsInVzZXJfaWQiOjQ1fQ.0X1Oz-QCEb0z5QsVEMZomhsB30mmNK-8n6lMQf9U5Pc'


def register_req():
    data = {
        'username': 'Delete',
        'email': 'Delete@gmail.com',
        'password': 'Deletepwd',
        'password2': 'Deletepwd'
    }
    url = 'http://localhost:8000/api/register/'
    response = post(url=url, data=data)
    print(response.status_code)
    print(response.text)


def login_req():
    url = 'http://localhost:8000/api/token/'
    data = {'username': 'TestUser', 'password': 'test1234'}
    response = post(url=url, data=data)
    print(response.status_code)
    print(response.text)


def after_req():
    global access
    try:
        r = get(url='http://localhost:8000/api/profiles/6/', headers={'Authorization': 'Bearer ' + access})
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


def refresh_req():
    global refresh
    try:
        r = post(url='http://localhost:8000/api/token/refresh/', data={'refresh': refresh})
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


def put_image_req():
    global access
    with open(file='C:\\Users\\Korisnik\\Desktop\\ai_programming.jpg', mode='rb') as descriptor:
        files = {'image': descriptor}
        try:
            r = put(
                url='http://localhost:8000/api/posts/129/',
                files=files,
                headers={'Authorization': 'Bearer ' + access}
            )
            descriptor.close()
            print(r.status_code)
            print(r.text)
        except RequestConnectionError as rce:
            print('ERROR', rce)


def create_image_post_req():
    global access
    image_path = 'C:\\Users\\Korisnik\\Desktop\\laptop.jpg'
    files = {'image': ''}
    with open(file=image_path, mode='rb') as descriptor:
        files['image'] = (image_path, descriptor, 'multipart/form-data')
        try:
            r = post(
                url='http://localhost:8000/api/posts/',
                files=files,
                headers={'Authorization': 'Bearer ' + access}
            )
            descriptor.close()
            print(r.status_code)
            print(r.text)
        except RequestConnectionError as rce:
            print('ERROR', rce)


def put_text_req():
    global access
    data = {'content': 'Put at ' + str(datetime.now())}#
    try:
        r = put(
            url='http://localhost:8000/api/posts/127/',
            data=data,
            headers={'Authorization': 'Bearer ' + access}
        )
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


def patch_req():
    global access
    data = {'username': 'JulesWinfield94', 'is_staff': True, 'email': 'JulesW@gmail.com'}
    try:
        r = patch(
            url='http://localhost:8000/api/users/10/',
            data=data,
            headers={'Authorization': 'Bearer ' + access}
        )
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


def patch_image_req():
    global access
    with open(file='C:\\Users\\Korisnik\\Desktop\\laptop.jpg', mode='rb') as descriptor:
        files = {'image': descriptor}
        try:
            r = patch(
                url='http://localhost:8000/api/posts/127/',
                files=files,
                headers={'Authorization': 'Bearer ' + access}
            )
            descriptor.close()
            print(r.status_code)
            print(r.text)
        except RequestConnectionError as rce:
            print('ERROR', rce)


def delete_post():
    global access
    try:
        r = delete(
            url='http://localhost:8000/api/posts/130/',
            headers={'Authorization': 'Bearer ' + access}
        )
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


def try_create_post():
    global access
    try:
        r = post(
            url='http://localhost:8000/api/posts/',
            data={
                'content': 'Post u ' + str(datetime.now())
            },
            headers={'Authorization': 'Bearer ' + access}
        )
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


def get_req():
    global access
    try:
        r = get(
            url='http://localhost:8000/api/profiles/45/'
        )
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


def delete_user():
    global access
    try:
        r = delete(
            url='http://localhost:8000/api/users/47/',
            headers={'Authorization': 'Bearer ' + access},
        )
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


def put_profile_req():
    global access
    url = 'http://localhost:8000/api/profiles/45/'
    with open(file='C:\\Users\\Milos\\Desktop\\download.png', mode='rb') as descriptor:
        files = {'image': descriptor}
        response = put(
            url=url,
            files=files,
            headers={'Authorization': 'Bearer ' + access}
        )
        descriptor.close()
        print(response.status_code)
        print(response.text)


def patch_profile_req():
    global access
    url = 'http://localhost:8000/api/profiles/45/'
    image_path = 'C:\\Users\\Milos\\Desktop\\download.png'
    with open(file=image_path, mode='rb') as image_desc:
        files = {'image': image_desc}
        r = patch(
            url=url,
            files=files,
            headers={'Authorization': 'Bearer ' + access}
        )
        image_desc.close()
        print(r.status_code)
        print(r.text)


def put_user_req():
    global access
    url = 'http://localhost:8000/api/users/10/'
    data = {
        'first_name': 'Jules',
        'last_name': 'Winfield',
        'username': 'JulesWinfield94',
        'email': 'JulesW@gmail.com'
    }
    try:
        r = put(
            url=url,
            data=data,
            headers={'Authorization': 'Bearer ' + access}
        )
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


#login_req()
#put_text_req()
#patch_req()
#register_req()
#try_create_post()
#get_req()
#delete_post()
#put_profile_req()
#patch_profile_req()
#refresh_req()
#put_image_req()
#create_image_post_req()
#patch_req()
#patch_image_req()
#put_user_req()
#delete_user()