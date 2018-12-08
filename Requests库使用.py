import requests
import time
def getHT(url):
    try:
        response=requests.get(url,timeout=30)
        response.raise_for_status()
        response.encoding=response.apparent_encoding
        return response.text
    except:
        return "产生异常"


def a():
    url='https://www.baidu.com'
    start=time.perf_counter()
    for i in range(100):
         getHT(url)
    end=time.perf_counter()
    print(end-start)


a()

"""
import requests
import time


def getHtmlTxt(url):
    try:
        r = requests.get(url, timeout=300)
        r.raise_for_status()  # 正常返回200，异常产生HttpError
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "连接失败"


if __name__ == "__main__":
    url = 'https://www.baidu.com'
    start = time.time()
    for i in range(100):
        getHtmlTxt(url)
    end = time.time()
  """#  print("访问100次百度所用时间为%fs" % (end - start))