'''import time
import json
import requests
import random
import re
import csv
def getHtml():
    info=[]
    url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    kv={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
         'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
         'Accept-Encoding': 'gzip, deflate, br',
         'Referer': 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=',
         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
         'X-Requested-With': 'XMLHttpRequest', 'X-Anit-Forge-Token': 'None',
         'X-Anit-Forge-Code': '0',
         'Content-Length': '26',
         'Cookie': 'user_trace_token=20171103191801-9206e24f-9ca2-40ab-95a3-23947c0b972a; _ga=GA1.2.545192972.1509707889; LGUID=20171103191805-a9838dac-c088-11e7-9704-5254005c3644; JSESSIONID=ABAAABAACDBABJB2EE72'
                   '0304E451B2CEFA1723CE83F19CC; _gat=1; LGSID=20171228225143-9edb51dd-ebde-11e7-b670-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DKkJPgBHAnny1nUKaLpx2oDfUXv9ItIF3kBAWM2-fDNu%26ck%3D3065.1.126.376.140.374.139.129%26shh%3Dwww.baidu.com%26sht%3Dmonline_3_dg%26wd%3D%26eqid%3Db'
                   '0ec59d100013c7f000000055a4504f6; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20171228225224-b6cc7abd-ebde-11e7-9f67-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; SEARCH_ID=3ec21cea985a4a5fa2ab279d868560c8',
        'Connection': 'keep-alive',
         'Pragma': 'no-cache',
         'Cache-Control': 'no-cache'}
    for i in range(31):
        time.sleep(random.randint(3, 5))
        fo={'first': 'False',
               'pn': i,
               'kd': 'Python'}
        r=requests.post(url,data=fo,headers=kv)
        html=r.text
        #print(html)
        text0=re.findall('"positionName":"(.*?)"',html)
        text1=re.findall('"firstType":"(.*?)"',html)
        text2=re.findall('"companyFullName":"(.*?)"',html)
        text3=re.findall('"city":"(.*?)"',html)
        text4=re.findall('"salary":"(.*?)"',html)
        text5=re.findall('"workYear":"(.*?)"',html)
        for n in range(len(text1)):
            info.append([text0[15:][n],text1[n],text2[n],text3[n],text4[n],text5[n]])
            print("正在保存%s"%info[n])
            with open("Laogou.csv",'a+',newline="",encoding='utf-8') as f:
                ls=csv.writer(f,dialect='excel')
                ls.writerow(info[n])
                f.close()
getHtml()
'''
import requests
import re
import time
import random
# import pymysql
import csv

def getHtml():
    try:
        # db = pymysql.connect(host='127.0.0.1', port=3306, db='pysql', user='root', passwd='12345678', charset='utf8')
        # cursor = db.cursor()
        # cursor.execute("select*from work")
        # print(cursor.fetchall())
        info=[]
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        kv={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest', 'X-Anit-Forge-Token': 'None',
            'X-Anit-Forge-Code': '0',
            'Content-Length': '26',
            'Cookie': 'user_trace_token=20171103191801-9206e24f-9ca2-40ab-95a3-23947c0b972a; _ga=GA1.2.545192972.1509707889; LGUID=20171103191805-a9838dac-c088-11e7-9704-5254005c3644; JSESSIONID=ABAAABAACDBABJB2EE72'
            '0304E451B2CEFA1723CE83F19CC; _gat=1; LGSID=20171228225143-9edb51dd-ebde-11e7-b670-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DKkJPgBHAnny1nUKaLpx2oDfUXv9ItIF3kBAWM2-fDNu%26ck%3D3065.1.126.376.140.374.139.129%26shh%3Dwww.baidu.com%26sht%3Dmonline_3_dg%26wd%3D%26eqid%3Db'
            '0ec59d100013c7f000000055a4504f6; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20171228225224-b6cc7abd-ebde-11e7-9f67-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; SEARCH_ID=3ec21cea985a4a5fa2ab279d868560c8',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'}
        for i in range(31):
            time.sleep(random.randint(3,5))
            ks = {'first': 'true',
                  'pn': i,
                  'kd': 'java'}
            r=requests.post(url,data=ks,headers=kv)
            html=r.text
            #print(html)
            names=re.findall('"positionName":"(.*?)"',html)
            comy=re.findall('"companyFullName":"(.*?)"',html)
            work=re.findall('"firstType":"(.*?)"',html)
            salary=re.findall('"salary":"(.*?)"',html)
            adress=re.findall('"workYear":"(.*?)"',html)
            name=names[15:]
            for n in range(len(name)):
                info.append([name[n],comy[n],work[n],salary[n],adress[n]])
                with open("Java.csv","a+",newline="",encoding="utf-8") as f:
                     ls=csv.writer(f,dialect='excel')
                     ls.writerow(info[n])
                     f.close()
                     print("正在保存%s" % info[n])
    except:
        return ""

getHtml()

'''for n in range(15):
                text=r.json()['content']['positionResult']['result'][n]
                name=re.findall(r'\'positionName\'\:\'.*\'',text)
                year=re.findall(r'\'woekYear\'\:\'.*?\'',text)
                company=re.findall(r'\'companyFullName\'\:\'.*\'',text)
                money=re.findall(r'\'salary\'\:\'.*?\'',text)
                work=re.findall(r'\'secondType\'\:\'.*\'',text)
                getPrint(info,name):
                nao="{0:^10}\t{1:{5}^15}\t{2:^10}\t{3:^6}\t{4:^5}"
                print(nao.format("java","公司名称","工作","工资","地址"))
                for i in range(len(name)):
                u=info[i]
                print(nao,format(u[0],u[1],u[2],u[3],u[4]))
                print(r.json()['content']['positionResult']['result'][m]['companyFullName'])'''
