import re
import json
import urllib
import requests

site = 'https://blog.jalenchuh.cn'
sitemap = 'https://blog.jalenchuh.cn/sitemap.xml'

listUrl = []
bingData = {}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
req = urllib.request.Request(url=sitemap, headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8')
result = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)

with open('urls.txt', 'w') as file:
  for data in result:
    print(data, file=file)
    listUrl.append(data)

bingData["siteUrl"] = site
bingData["urlList"] = listUrl
with open("bing.json", "w") as f:
  json.dump(bingData,f)
