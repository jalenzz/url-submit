import re
import urllib
import requests

site = 'https://blog.jalenchuh.cn'
sitemap = 'https://blog.jalenchuh.cn/sitemap.xml'

headers = {
  'User-Agent': 'curl/7.12.1',
  'Host': 'data.zz.baidu.com',
  'Content-Type': 'text/plain',
  'Content-Length': '83'
}
html = urllib.request.urlopen(sitemap).read().decode('utf-8')
result = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)
url = 'http://data.zz.baidu.com/urls?site=' + site + '&token=BAIDU_TOKEN'

for data in result:
  print(data + '\n' +
    requests.post(
      url = url,
      data = data,
      headers = headers
    ).text + '\n'
  )
