# send request to API
import requests
url = 'http://127.0.0.1:8000/movie/' 
headers = {'Authorization': 'Token 1a394b8c7486d94321cdd89992ae11e749b9f9cd'}
r = requests.get(url, headers=headers)
print(r.text)