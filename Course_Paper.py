from pprint import pprint
import json
import requests
import configparser

from tqdm import tqdm

from vk_user import vk_user
from yandex_disk import yandex_disk
from json_utils import save_to_json

class vk_user:
    def get_json(self, file_path):
        save_to_json(self.photo_dict, file_path)
       
##    def __init__(self):
##         self.token = config['DEFAULT']['VK_TOKEN']
##         self.vk_user_id = input('Введите свой ID пользователя VK : ')
##         self.id_album = input("Введите ID альбома: ")
##         self.count = input('Введите количество фотографий: ')
##         self.photo_dict = {}
##         
##         
##    def get_photo(self):
##         URL = 'https://api.vk.com/method/users.get'
##         params = {'access_token': self.token,
##                   'user_ids': self.vk_user_id,
##                   'v': 5.131}
##         user = requests.get(URL, params=params).json()
##         URL = 'https://api.vk.com/method/photos.get'
##         params = {'owner_id': user['response'][0]['id'], 
##                   'album_id': self.id_album,
##                   'count': self.count,
##                   'extended': 1,
##                   'access_token': self.token,
##                   'v': 5.131}
##         vk_sizes = {'s': 1, 'm': 2, 'o': 3, 'p': 4, 'q': 5, 'r': 6, 'x': 7, 'y': 8, 'z': 9, 'w': 10}
##    def res_get_photo_1(self):
##         res_get_photo = requests.get(URL, params=params).json()
##         if 'response'in res_get_photo:
##             for file in res_get_photo['response']['items']:
##                 file_url = max(file['sizes'], key=lambda x: vk_sizes[x['type']])
##                 names = file['likes']['count']
##                 if names in self.photo_dict.keys():
##                     self.photo_dict[f"{names}_{file['date']}"] =  file_url['url']
##                 else:
##                     self.photo_dict[names] =file_url['url']
##         else:
##             print("Отсутствует ключ 'response' в словаре res_get_photo.")
##         return
##    def res_get_photo_2(self):        
##         res_get_photo = requests.get(URL, params=params).json()
##         for file in res_get_photo['response']['items']:
##             file_url = max(file['sizes'], key=lambda x: vk_sizes[x['type']])
##             names = file['likes']['count']
##             if names in self.photo_dict.keys():
##                 self.photo_dict[f"{names}_{file['date']}"] =  file_url['url']
##                 self.photo_dict_1[f"{folder_name}"] = count(file_url['url'])
##             else:
##                 self.photo_dict[names] =  file_url['url']
##         return
    
##    def get_json(self, file):
##         with open('result_json.json', 'w') as f:
##             json.dump(file, f, ensure_ascii=False, indent=2)

   
            
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('settings.ini')
    poligon = config['DEFAULT']['POLIGON_YA']
    vk = vk_user()
    vk.get_photo()
    vk.res_get_photo_1()
    vk.res_get_photo_2()
    vk.get_json(vk.photo_dict)
    ya = yandex_disk(poligon=poligon)
    ya.create_get_folder(vk.photo_dict)
    ya.upload_url_1()
    
