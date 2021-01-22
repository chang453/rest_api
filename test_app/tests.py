from django.test import TestCase
import requests

data_create = {
    'title' : 'new1',
    'contents' : 'new1',
}
data_update = {
    'title' : 'new2',
    'contents' : 'new2',
}

data = requests.get('http://127.0.0.1:8000/api_list/1')
print(data)
print(data.text)

data = requests.post('http://127.0.0.1:8000/api_list/create', data = data_create)
print(data)

data = requests.put('http://127.0.0.1:8000/api_list/2/update', data = data_update)
print(data)

data = requests.delete('http://127.0.0.1:8000/api_list/4/delete')
print(data)







# rest_key = '5b11c1507025858e59f3381bdad95f45'

# import json
# import requests

# headers = {
#     'Authorization': 'KakaoAK {}'.format(rest_key)
# }
# url = 'https://dapi.kakao.com/v2/search/web?query={}&size=50'.format('데이터누리')

# t = requests.get(url, headers = headers)
# raw = json.loads(t.text)
# signs = []
# signs.extend(raw['documents'])
# for k in range(0, 50):
#     data = requests.post('http://127.0.0.1:8000/api_list/create', signs[k])
#     print(data)



