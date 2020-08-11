from bs4 import BeautifulSoup

html = """<html><head></head><body><p class='d'>test</p><p class='d'>test2</p><p class='d' id='i'>test3</p><a>test4</a></html>"""

soup = BeautifulSoup(html, 'lxml')
print(soup.find('p', class_="d"))
print(soup.find('p', class_="d"))
print(soup.find('p',id='i'))

print(soup.select('body p'))
print(soup.select('body .d'))
print(soup.select('body #i'))

for tag in soup.find_all(['p','a']):
    print(tag.extract())

print('제거완료')
print(soup)