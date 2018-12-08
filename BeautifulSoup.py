import requests
from bs4 import BeautifulSoup
try:
    url="http://python123.io/ws/demo.html"
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
  #  print(r.text)
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    tag=soup.find_all("a")
    tas=soup("a")
   # print(soup.title)
    #print(tag.attrs)
 #   print(soup.prettify())
    print(tas)

except:
    print("获取失败")