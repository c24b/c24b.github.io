#coding : utf-8
import requests
def download(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

###ici l'exemple
mypage = "http://fr.wikipedia.org/wiki/Araignée"
html = download(mypage)
print(html)
