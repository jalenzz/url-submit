import re
import json
import urllib
import requests

site = 'https://blog.jalenchuh.cn'
sitemap = 'https://blog.jalenchuh.cn/sitemap.xml'

listUrl = []
bingData = {}

html = urllib.request.urlopen(sitemap).read().decode('utf-8')
result = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)

with open('urls.txt', 'w') as file:
  for data in result:
    print(data, file=file)
    listUrl.append(data)
file.close()

bingData["siteUrl"] = site
bingData["urlList"] = listUrl
with open("bing.json", "w") as f:
  json.dump(bingData,f)
file.close()
