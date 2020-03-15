from requests import post, get, put, patch, delete, ConnectionError as RequestConnectionError
from datetime import datetime


refresh = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4NDM1NTQ3OSwianRpIjoiOWY1YTU4ZDEyMDdkNGEzMWFkYjg3NTk3YjUzZWE5NjMiLCJ1c2VyX2lkIjoxMH0.NQqa6YlWAIqTT4wwDRQ0RMsk82zG8KM_lHunqhiekjE'
access = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg0MzU1NjAxLCJqdGkiOiJmYzFkMzBhMzdhNjc0NzMwYTFhOGRlZWExZGMxNDY4ZiIsInVzZXJfaWQiOjI0fQ.sekBLbq9fQStGABTbk9vR_Q1U_Xqv0u1qWnSvvaTmhE'


def register_req():
    data = {
        'username': 'TestUser',
        'email': 'Test@gmail.com',
        'password': 'test1234',
        'password2': 'test1234'
    }
    url = 'http://snanetwork.rs/api/register/'
    response = post(url=url, data=data)
    print(response.status_code)
    print(response.text)


def login_req():
    url = 'http://snanetwork.rs/api/token/'
    data = {'username': 'MikeSNA', 'password': 'z20letopel'}
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
        r = post(url='http://snanetwork.rs/api/token/refresh/', data={'refresh': refresh})
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
    image_path = 'C:\\Users\\Korisnik\\Desktop\\pdzi.jpg'
    files = {'image': ''}
    with open(file=image_path, mode='rb') as descriptor:
        files['image'] = (image_path, descriptor, 'multipart/form-data')
        try:
            r = post(
                url='http://snanetwork.rs/api/posts/',
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
            url='http://snanetwork.rs/api/posts/137/',
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
            url='http://snanetwork.rs/api/posts/',
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
            url='http://snanetwork.rs/api/users/'
        )
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


def delete_user():
    global access
    try:
        r = delete(
            url='http://snanetwork.rs/api/users/49/',
            headers={'Authorization': 'Bearer ' + access},
        )
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


def put_profile_req():
    global access
    url = 'http://snanetwork.rs/api/profiles/48/'
    with open(file='C:\\Users\\Korisnik\\Desktop\\22.jpg', mode='rb') as descriptor:
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
    url = 'http://snanetwork.rs/api/profiles/48/'
    image_path = 'C:\\Users\\Korisnik\\Desktop\\pdzi.jpg'
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
    url = 'http://snanetwork.rs/api/users/10/'
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


def api_root_request():
    url = 'http://snanetwork.rs/api/'
    try:
        r = get(url=url)
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


def try_delete_profile():
    url = 'http://snanetwork.rs/api/profiles/49/'
    try:
        r = delete(
            url=url,
            headers={'Authorization': 'Bearer ' + access}
        )
        print(r.status_code)
        print(r.text)
    except RequestConnectionError as rce:
        print('ERROR', rce)


#login_req() #works
#put_text_req()
#patch_req()
#register_req() works
#try_create_post()
#get_req() works
#delete_post() #works
#put_profile_req() works
#patch_profile_req() works
#refresh_req()
#put_image_req() works
#create_image_post_req() works
#patch_req() works
#patch_image_req() works
#put_user_req()
#delete_user() #works
#api_root_request() works
#try_delete_profile()