import requests
import json
import csv

# url = ['http://www.iwencai.com/stockpick/find-information?\
# stockList=000538%2C603527%2C603199%2C600814%2C300119%2C300297%2C002443%2C002036%2C601126%2C603010', 'http://www.iwencai.com/stockpick/find-information?stockList=000810%2C600563%2C600419%2C600887%2C600248%2C000981%2C002627',
#        'http://www.iwencai.com/stockpick/find-information?stockList=000538%2C603527%2C603199%2C600814%2C300119%2C300297%2C002443%2C002036%2C601126%2C603010']
# header = {
# 'Accept': 'application/json, text/javascript, */*; q=0.01',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Cache-Control': 'no-cache',
# 'Connection': 'keep-alive',
# 'Cookie': 'vvvv=1; PHPSESSID=3a5787a3f1e1a8aa18db7af772e1dc92; cid=3a5787a3f1e1a8aa18db7af772e1dc921541027381; ComputerID=3a5787a3f1e1a8aa18db7af772e1dc921541027381; v=AiJkNEkxjac6MpF7qmQfpo6wc6OHcyaN2HcasWy7ThVAP8wVVAN2nagHasU_',
# 'hexin-v': 'AiJkNEkxjac6MpF7qmQfpo6wc6OHcyaN2HcasWy7ThVAP8wVVAN2nagHasU_',
# 'Host': 'www.iwencai.com',
# 'Pragma': 'no-cache',
# 'Referer': 'http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=result_rewrite&selfsectsn=&querytype=stock&searchfilter=&tid=stockpick&w=PE%20%3D%2020&queryarea=',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
# 'X-Requested-With': 'XMLHttpRequest',
# }
# for i in url:
#     r = requests.get(i, headers=header)
#     html = r.text
#     html_json = json.loads(html)
#     with open('iwencai.txt', 'w', encoding='utf-8') as f:
#         f.write(str(html_json))
#     print(html_json)

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection':'keep-alive',
    'Cookie':'id=3a5787a3f1e1a8aa18db7af772e1dc921541027381; ComputerID=3a5787a3f1e1a8aa18db7af772e1dc921541027381; PHPSESSID=9ed49f8f75eea6a29ac416b68dc3c60a; v=As6IOD1tGeNM1a3HsTcL4kLUH6-TT5IcpBNGLvgXOlGMW2AZYN_iWXSjljrL',
    'hexin-v': 'As6IOD1tGeNM1a3HsTcL4kLUH6-TT5IcpBNGLvgXOlGMW2AZYN_iWXSjljrL',
    'Host': 'www.iwencai.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=result_rewrite&selfsectsn=&querytype=stock&searchfilter=&tid=stockpick&w=PE%20%3D%2020&queryarea=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
for i in range(1, 3):
    # format(n, y)  # n是token，y是页码
    url = 'http://www.iwencai.com/stockpick/cache?token={}&p={}&perpage=10&showType=[%22%22,%22%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onList%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22]'.format('511e51b2ea8df8384a13214e2ba3d008', i)
    r = requests.get(url, headers=header)
    html = r.text
    # 反序列化成python字典  解密
    html_text = json.loads(html)
    mess = html_text['title']
    mess2 = html_text['result']
    with open("iwencai.csv", 'a+', newline='', encoding='utf-8') as f:
        ls = csv.writer(f, dialect='excel')
        ls.writerow(mess)
    for s in mess2:
        with open("iwencai.csv", 'a+', newline='', encoding='utf-8') as f:
            ls = csv.writer(f, dialect='excel')
            ls.writerow(s)
