from urllib.request import urlopen,Request
import urllib

url = "http://blog.naver.com/pjt3591oo"

data = {"key1" : "value1" , "key2" : "value2"}
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')

print(data)

req_post = Request(url,data=data,headers={})
page = urlopen(req_post)

print(page)
print(page.url)

req_get = Request(url+'?key1=value1&key2=value2',None,headers={})
page = urlopen(req_get)

print(page)
print(page.url)