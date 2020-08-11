from urllib.request import Request,urlopen
from bs4 import BeautifulSoup

request = Request("http://movie.naver.com/movie/running/current.nhn")
response = urlopen(request)
html = response.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")

# currents = bs.find("ul", attrs={"class": "lst_detail_t1"})
# for child in currents:
#     try:
#         titles = child.find("dt", attrs={"class": "tit"})
#         for title in titles:
#             try:
#                 if title.name == "a":
#                     print(title.text, title['href'])
#             except:
#                 pass
#     except:
#         pass

current_movies = bs.select(".lst_detail_t1 > li")

for movie in current_movies:
    titles = movie.select(".lst_dsc > .tit > a")

    for title in titles:
        print(title.text, title['href'])

