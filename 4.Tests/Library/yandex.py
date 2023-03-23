import requests


class Yandex:

    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def folder(self, folder='test'):
        uri = 'v1/disk/resources/'
        url = self.host + uri
        params = {'path': f'{folder}', 'permanently': 'true'}
        response = requests.put(url, headers=self.get_headers(), params=params)
        return response.status_code

