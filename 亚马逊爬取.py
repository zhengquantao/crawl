import requests
url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
kv={"User-Agent":"Mozella/5.0"}
try:
    response=requests.get(url,headers=kv)
    response.raise_for_status()
    response.encoding=response.apparent_encoding
    print(response.request.headers,response.text[:1000])
except:
    print("失败")
"""import requests
url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
kv={'user':'Mozella/5.0'}
response=requests.get(url,headers=kv)
response.status_code
response.encoding=response.apparent_encoding
print(response.status_code,response.request.headers,response.text[:1000])
"""