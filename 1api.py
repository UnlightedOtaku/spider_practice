# 通过网站的 API 接口，抓取 JSON 格式的文章数据到本地并保存。
import requests


# 这是我自己部署的网址，自用请换为自己的url
url = 'http://47.104.29.136:8000/tasks/api/'

result = requests.get(url)
# print(result.content) bytes
# print(result.text) unicode
# 打开文件 ， 写入 ， 关闭
f = open('1apiresult.txt', 'wb')
f.write(result.content)
f.close()
