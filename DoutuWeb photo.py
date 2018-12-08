import requests
import re
import os
def get_url():
    for i in range(51):
        url = "http://www.doutula.com/photo/list/?page=" + str(i)
        r=requests.get(url)
        # print(r)
        html=r.text
        url_jpg=re.findall('original="(.*?)"',html)
        # print(url_jpg)
        # url_gif=re.findall('src="(.*?)"',html)
        url_alt=re.findall('alt="(.*?)"',html)
        root="D://python/image//"
        try:
             if not os.path.exists(root):
                os.mkdir(root)
             for i in range(len(url_alt)):
                path=root+url_alt[i].split('/')[-1]
                if not os.path.exists(path):
                    response=requests.get(url_jpg[i])
                    # print(response.content)
                    f=open(path,"wb")
                    f.write(response.content)
                    print("正在保存%s"%url_alt[i])
                    f.close()
             else:
                 continue
        except:
            return "a"
get_url()