import requests

TOKEN = '///'

class YaUploader:
    
    base_host = 'https://cloud-api.yandex.net/'
    
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload(self, path_to_file: str):
        print(path_to_file)
        uri = 'v1/disk/resources/upload/'
        upload_url = self.base_host + uri
        params = {"path": "AnyFile.xlsx", "overwrite": True}
        resp = requests.get(upload_url, headers = self.get_headers(), params=params).json()
        upload_link = resp.get('href')
        print(upload_url)
        print(upload_link)
        response = requests.put(upload_link, data = open(path_to_file, 'rb'), headers=self.get_headers())
        print(response.status_code)
        if response.status_code == 201:
            print('Загрузка произведена успешно')


if __name__ == '__main__':
    path_to_file = 'AnyFile.xlsx'
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.get_upload(path_to_file)