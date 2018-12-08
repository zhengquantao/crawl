import requests
import os
url="http://dl.stream.qqmusic.qq.com/C400001Pkt5A2buDRX.m4a"
root="D://python//"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        response=requests.get(url)
        with open(path,"wb") as f:
            f.write(response.content)#以二进制格式
            f.close()
    else:
        print("文件已经存在")
except:
    print("爬取失败")