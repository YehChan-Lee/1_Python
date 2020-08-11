from bs4 import BeautifulSoup
import re

html = """<html><head><title>test title</title></head><body><p class='d'>test</p><p class='d'>test2</p><p class='d' id='i'>test3</p><a 
href="/emample/test01">test4</a></html> """

soup = BeautifulSoup(html,'lxml')

print(soup.find_all(class_=re.compile('d')))
print(soup.find_all(id=re.compile('i')))
print(soup.find_all(re.compile('t')))
print(soup.find_all(re.compile('^t')))
print(soup.find_all(href=re.compile('/')))