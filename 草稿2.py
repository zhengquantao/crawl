import os
import requests
import bs4
baseUrl="https://imgur.com"
dirName='image'
os.makedirs(dirName,exist_ok=True)
url=baseUrl+"/search/score?q="+"movie"
response=requests.get(url)
response.raise_for_status()
response.raise_for_status()
print(response.status_code)
soup=bs4.BeautifulSoup(response.text,'html.parser')
imageUrls=soup.select(".image-list-link img")
if not imageUrls:
   print("没有找到图片!")
else:
    for imageUrl in imageUrls:
        downloadUrl=imageUrl.get('src')
        split = downloadUrl.split('/')
        fileName=os.path.basename(split[len(split) - 1])
        filePath = os.path.join(dirName, fileName)
        print("filePath %s..." % filePath)
        if not os.path.exists(filePath):
            imageUrlPath=requests.get("http:"+downloadUrl)
            imageUrlPath.raise_for_status()
            imageFile=open(filePath,'wb')
            for python in imageUrlPath.iter_content(100):
                imageFile.write(python)