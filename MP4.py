import requests
from lxml import etree
import re
from urllib.request import urlretrieve
import os
root="D://python//video"
if not os.path.exists(root):
    os.mkdir(root)
else:
    print('已经存在')
def Li_html():
    url = 'http://www.pearvideo.com/category_59'
    html = requests.get(url).text
    html = etree.HTML(html)
    video_id = html.xpath('//div[@class="vervideo-bd"]/a/@href')
    for i in video_id:
        urls = 'http://www.pearvideo.com/'+i
        htmls = requests.get(urls).text
        mp_url = re.findall('srcUrl="(.*?)"',htmls)
        mp_name = re.findall('class="video-tt">(.*?)<',htmls)
        print("正在保存%s"%mp_name[0])
        urlretrieve(mp_url[0],'./video/%s.mp4'%mp_name[0])


Li_html()