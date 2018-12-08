import requests
import os
url="http://ww3.sinaimg.cn/bmiddle/9150e4e5ly1fryaw710l9j20u00ttab5.jpg"
root="D://python//"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        response=requests.get(url)
        # print(response.content)
        with open(path,"wb") as f:
            f.write(response.content)#以二进制格式
            f.close()
    else:
        print("文件已经存在")
except:
    print("爬取失败")
'''import requests
python="D:/abc.jpg"
url="http://f2.topitme.com/2/6a/bc/113109954583dbc6a2o.jpg"
response=requests.get(url)
response.status_code
with open(python,'wb') as f:
    f.write(response.content)
    f.close()
print(response.status_code)
'''