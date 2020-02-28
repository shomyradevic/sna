from requests import post, get, delete, put


class EntityRequest:

    def __init__(self, root):
        self.root = root

    def queryset(self):
        response = get(url=self.root)
        q = [instance for instance in eval(response.text)]
        return {'code': response.status_code, 'data': q}

    def get(self, id):
        response = get(url=self.root + str(id) + '/')
        return {'code': response.status_code, 'text': response.text}

    def delete(self, id):
        response = delete(url=self.root + str(id) + '/')
        if response.status_code == 204:
            return 'Deleted successfully.'
        return 'Not deleted.'

    def put(self, id, data: dict):
        response = put(url=self.root + str(id) + '/', data=data)
        return {'code': response.status_code, 'text': response.text}


class PostEntityRequest(EntityRequest):

    def create(self, author, content=None, image_path=None):
        if content:
            data = {'content': content, 'author': author}
            response = post(url=self.root, data=data)
        elif image_path:
            with open(image_path, 'rb') as descriptor:
                files = {'image': (image_path, descriptor, 'multipart/form-data')}
                data = {'author': eval(user.get(1)['text'])['url']}
                response = post(self.root, data=data, files=files)
                descriptor.close()
                return {'code': response.status_code, 'text': response.text}
        else:
            return 'You must provide either text-content or image to create a post!'
        return {'code': response.status_code, 'text': response.text}


class CustomUserEntityRequest(EntityRequest):

    def create(self, username, password, email):
        data = {'username': username, 'password': password, 'email': email}
        response = post(url=self.root, data=data)
        return {'code': response.status_code, 'text': response.text}


class ProfileEntityRequest(EntityRequest):

    def create(self, username, password, email):
        data = {'username': username, 'password': password, 'email': email}
        response = post(url=self.root, data=data)
        return {'code': response.status_code, 'text': response.text}


API_ROOT = 'http://localhost:8000/api/'
blog_post = PostEntityRequest(root=API_ROOT + 'blogposts/')
user = CustomUserEntityRequest(root=API_ROOT + 'users/')
print(user.delete(44))

"""
def roditeljska():
    niz = [3, 4, 3, 5, 8, 0, 2, 1]
    
    def vrati_najveci(arr):
        return max(arr)

    rez = vrati_najveci(niz)
    return rez


print(roditeljska())
"""
