'''import requests
import bs4
#from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup=bs4.BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])



def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    #print("{:^10}\t{:^10}\t{:^15}".format('排名','学校名称','总分'))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
        #print("{:^10}\t{:^10}\t{:^15}".format(u[0],u[1],u[2]))
        with open("t.txt", "w",encoding='utf-8') as f:
            f.writelines(u)
            f.seek(0)
            f.close()

def main():
    uinfo=[]
    url="http://www.zuihaodaxue.com/shengyuanzhiliangpaiming2018.html"
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,100)


main()'''
import requests
import bs4
def getHTMLText(url,en='UTF-8'):
    try:
        kv={'User-Agent':'Mozella/5.0'}
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding=en
        return r.text
    except:
        print("")


def getMessage(ilt,html):
    soup=bs4.BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr("td")
            ilt.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
def printList(ilt,num):
    rin="{0:^3}\t{1:{4}^15}\t{2:^5}\t{3:^6}"
    print(rin.format("排名","学校名称","地址","留学生占比",chr(12288)))
    for i in range(num):
        u=ilt[i]
        print(rin.format(u[0],u[1],u[2],u[3],chr(12288)))
def saveText(ilt):
    try:
        for i in range(100):
            with open("t.txt","a+",encoding="utf-8") as f:
                f.write(str(ilt[i])+'\n')
                f.close()
    except:
        print("文件已经存在")



def main():
    url='http://www.zuihaodaxue.com/xueshengguojihuapaiming2018.html'
    infoList=[]
    html=getHTMLText(url)
    getMessage(infoList,html)
    printList(infoList,100)
    saveText(infoList)
main()