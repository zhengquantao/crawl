import requests
import re
import bs4
def getHtml(url,en):
    try:
        kv={"User-Agent":"Mozella/5.0"}
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding=en
        return r.text
    except:
        return "a"
def getNumber(lst,html):
    htmla=getHtml(html,"GB2312")
    soup=bs4.BeautifulSoup(htmla,'html.parser')
    a=soup.find_all("a")
    for i in a:
        try:
            href=i.attrs["href"]
            lst.append(re.findall(r"\d{6}",href)[0])
        except:
            continue

def getPrint(lst,html):
    count=0
    for stock in lst:
        url=html+stock
        htmls=getHtml(url,'utf-8')
        try:
            if htmls=="":
                continue
            info={}
            soup=bs4.BeautifulSoup(htmls,'html.parser')
            inlt=soup.find("div",attrs={'class':'stock-quote-wrap'})
            name=inlt.find_all(attrs={'class':'title'})[0]
            info.update({'股票名称':name.text.split()[0]})
            Lut=inlt.find_all('td')
            for i in range(len(Lut)):
                Lit=Lut[i].text
                info[Lit]=Lit
            with open("Gupiaos.txt","a+",encoding="utf-8") as f:
                f.writelines(info)
                f.close()
                count=count+1
                print("\r当前进度{:.2f}%".format(count*100/len(lst)),end="")
        except:
            continue


def main():
    firstUrl="http://quote.eastmoney.com/stocklist.html"
    secondUrl="https://www.laohu8.com/hq/s/"
    slist=[]
    getNumber(slist,firstUrl)
    getPrint(slist,secondUrl)
main()
