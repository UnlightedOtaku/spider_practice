# 进入文章列表页面，获得每一篇文章的题目和摘要并保存在本地。
# 容易发现标题是h3，摘要是p
import requests
from bs4 import BeautifulSoup


url = 'http://47.104.29.136:8000/tasks/article/list/'
parser = 'html.parser'
result = requests.get(url)

# 解析网页
soup = BeautifulSoup(result.text, parser)
# 找到标题 摘要
titles = soup.find_all('h3')
abs = soup.find_all('p')
# 可能有编码问题，介意的请自行调整
f = open('3result.txt', 'w')
for i in range(len(titles)):
    f.write('title:'+titles[i].get_text()+'\nabs:'+abs[i].get_text()+'\n\n')
f.close()
