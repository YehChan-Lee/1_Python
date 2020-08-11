from urllib.request import Request,urlopen
from bs4 import BeautifulSoup

req = urlopen('http://media.daum.net')
print(req.getcode())

if req.getcode() == 200:
    html = req.read()
    print(html)

    html = html.decode("utf-8")
    print(html)
else:
    print('BTTP ERROR')

soup = BeautifulSoup(html,"html.parser")
print(soup.title)
print(soup.title.text)