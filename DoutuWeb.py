import requests
import re
import pymysql
db=pymysql.connect(host='127.0.0.1',port=3306,db='pysql',user='root',passwd='12345678',charset='utf8')
cursor=db.cursor()
cursor.execute("select*from images")
# print(cursor.fetchall())
def getHtml():
    try:
        for n in range(125, 151):
            url = 'http://www.doutula.com/photo/list/?page='+str(n)
            r=requests.get(url)
            html=r.text
            # re=r'data-original="(.*?)".*?alt="(.*?)"'
            # reg=re.compile(re,re.S)
            # lists=re.findall(reg,html)
            geturl=re.findall(r'data-original="(.*?)"',html)
            getname=re.findall(r'alt="(.*?)"',html)
            # print(len(getname))
            for i in range(len(geturl)):
                geturls=geturl[i]
                getnames=getname[i]
                # print(geturls)
                # cursor.execute("insert into images(~name~,~imageUrl~) values('{}','{}'".format(getnames,geturls))
                cursor.execute("insert into images(name,imageUrl) values(%s,%s)",[getnames,geturls])
                # print("正在保存%s"%getnames)
                print("{:.2f}%".format(i/68*100))
                # 提交更新
                db.commit()
    except:
        return "a"
getHtml()
