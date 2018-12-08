'''import requests
import bs4
import traceback
import re
def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent.encoding
        return r.text
    except:
        return ""
def getStockList(lst,stockURL):
    html=getHTMLText(stockURL)
    soup=bs4.BeautifulSoup(html,'html.parser')
    a=soup.find_all('a')
    for i in a:
        try:
            href=i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue
def getStockInfo(lst,stockURL,fpath):
    for stock in lst:
        url=stockURL+stock+".html"
        html=getHTMLText(url)
        try:
            if html=='':
                continue
            infoDict={}
            soup=bs4.BeautifulSoup(html,'html.parser')
            stockInfo=soup.find('div',attrs={'class':'stock-bets'})
            name=stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})
            keyList=stockInfo.find_all('dt')
            valueList=stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key=keyList[i].text
                val=valueList[i].text
                infoDict[key]=val
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
        except:
            traceback.print_exc()
            continue
def main():
    stock_list_url='http://quote.eastmoney.com/sz000001.html'
    stock_info_url='http://quote.eastmoney.com/sz300059.html'
    output_file='D://python//BaiduStockInfo.txt'
    slist=[]
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)
main()
'''
import requests
from bs4 import BeautifulSoup
import traceback
import re


def getHTMLText(url,en='utf-8'):
    try:
        kv={'User-Agent':'Mozella/5.0'}
        r = requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding = en
        return r.text
    except:
        return "a"


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL,'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][z]\d{6}", href)[0])
        except:
            continue


def getStockInfo(lst, stockURL):
    count=0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})
            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open("gupiao.txt", 'a+', encoding='utf-8') as f:
                f.write(str(infoDict)+"\n")
                f.close()
                count=count+1
                print("\r当前进度:{:.2f}%".format(count*100/len(lst)),end="")
        except:
            continue


def main():
    url = 'http://quote.eastmoney.com/stocklist.html'
    url2 = 'https://gupiao.baidu.com/stock/'
   # output_file = 'D://python//StockInfo.txt'
    slist = []
    getStockList(slist, url)
    getStockInfo(slist, url2)


main()

