import requests

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params})
       return response.json()


access_token = 'vk1.a.Sibj4g5CcjmRtWM3TLapJqWvmdcMQ9o36tKeAh-9zJmO7IPuC5bCuDGQi2LzktIjX248vTgRjd0ptol-6xPSrW2y13yC_SadHCUpgIzz2ePM8dP_1x-wFi-mx3CJXY4CfqR-zWPmQW6dOj8URciNkdsFGye0KxtT876_bn-Yqvh20zcjSdN-l2iMglKtgFLCJltJNIJV2m9f-3p8nylYxA'
user_id = '14483137'
vk = VK(access_token, user_id)
print(vk.users_info())
