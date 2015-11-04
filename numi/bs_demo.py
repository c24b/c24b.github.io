import BeautifulSoup4

def extract_title(html):
    soup = BeautifulSoup4(html)
    return soup.title

###ici l'exemple avec inclusion de la fonction précédente
mypage = "http://fr.wikipedia.org/wiki/Araignée"
html = download(mypage)
title = extract_title(html)
print(title)
