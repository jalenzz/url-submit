import re
import urllib
import requests

sitemap = 'https://blog.jalenchuh.cn/sitemap.xml'

html = urllib.request.urlopen(sitemap).read().decode('utf-8')
result = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)

for data in result:
  with open('urls.txt', 'a') as file:
    print( data + ',', file=file)
