import requests
from bs4 import BeautifulSoup

loginurl = ('https://the-internet.herokuapp.com/authenticate')
secure_url = ('https://the-internet.herokuapp.com/secure')

payload = {
    'username': 'tomsmith',
    'password': 'SuperSecretPassword!'
}

with requests.session() as s:
    s.post(loginurl, data=payload)
    r = s.get(secure_url)
    soup =BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())