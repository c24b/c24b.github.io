#coding:utf-8
from bs4 import BeautifulSoup
import requests

def download(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
        
def extract_title(html):
    soup = BeautifulSoup(html)
    return soup.title

###ici l'exemple avec inclusion de la fonction précédente
mypage = "http://fr.wikipedia.org/wiki/Araignée"
html = download(mypage)
title = extract_title(html)
print(title)
