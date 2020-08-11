import urllib.request
import json

client_id = "cuJXF_cnDNtSyla0xcVr"
client_secret = "ogSFGAZwBK"

enc_text = urllib.parse.quote("로지텍")
url = "https://openapi.naver.com/v1/search/news.json?query={}".format(enc_text)

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

print(rescode)

if(rescode == 200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    json_rt = response_body.decode('utf-8')
    py_rt = json.loads(json_rt)

    news_list = py_rt['items']

    for news in news_list:
        news['title']
        print("title : {title} @ {pubDate}".format_map(news))
else:
    print("Error Code %d"%(rescode))
