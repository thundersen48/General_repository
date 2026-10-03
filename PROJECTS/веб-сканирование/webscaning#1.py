import requests


URL = ("https://yandex.ru/pogoda/moscow")
resp = requests.get(URL)
print(resp.status_code)
print(resp.text)