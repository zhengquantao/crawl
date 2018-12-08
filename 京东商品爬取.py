'''import requests
url="https://item.jd.com/676676.html"
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print("失败")

''''''import requests
response=requests.get("https://item.jd.com/676676.html")
response.status_code
response.encoding=response.apparent_encoding
print(response.text[:1000])''''''
import requests
url="https://detail.tmall.com/item.htm?spm=a220m"
try:
    response=requests.get(url)
    response.raise_for_status()
    response.encoding=response.apparent_encoding
    print(response.text[:1000])
except:
    print("失败")'''
import requests
import re
import os
import csv
def getHTMLText(url,en='utf-8'):
    try:
        kv={"User-Agent":"Mozella/5.0"}
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding=en
        return r.text
    except:
        print("")

def getMessage(ilt,html):
    #try:
        ptl=re.findall(r'\"color\"\:\".*?\"',html)
        tlt=re.findall(r'\"name\"\:\".*?\"',html)
        tts=tlt[:-15]
        for i in range(len(ptl)):
            colors=eval(ptl[i].split(':')[1])
            names=eval(tts[i].split(':')[1])
            ilt.append([colors,names])
    #except:
        print("s")

def printList(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","颜色","名字"))
    count=0
    for i in ilt:
        count=count+1
        print(tplt.format(count,i[0],i[1]))
def writeList(ilt):
    try:
        root = "D://python//"
        if not os.path.exists(root):
            os.mkdir(root)
        else:
            for i in ilt:
                with open("dj.csv","a+",newline="") as f:
                    cs=csv.writer(f,dialect='excel')
                    cs.writerow(i)
                    f.close()

    except:
        print("")
def main():
    info=[]
    url='https://list.jd.com/list.html?cat=9987,653,655'
    html=getHTMLText(url)
    getMessage(info,html)
    printList(info)
    writeList(info)
main()