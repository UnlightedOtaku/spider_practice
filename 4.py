# 从文章列表页分别进入每一篇文章的详细页面，获得每一篇文章的阅读数、点赞数和评论数并保存本地。
# 首先找到a标签指向的url，再在文章详情页找
import requests
from bs4 import BeautifulSoup


url = 'http://47.104.29.136:8000/tasks/article/list/'
base_url = 'http://47.104.29.136:8000'
parser = 'html.parser'
result = requests.get(url)

# 解析网页
soup = BeautifulSoup(result.text, parser)
# 找到文章详情页的url
a_tags = soup.find('main').find(name="div", attrs={"class": "container-fluid"}).find_all('a')
f = open('4result.txt', 'w')
for i in a_tags:
    # print(i.get('href'))
    # 获取文章链接
    article_url = base_url + i.get('href')
    article = requests.get(article_url)
    # 解析html
    soup = BeautifulSoup(article.text, parser)
    # 标题
    title = soup.find('h2').get_text()
    f.write(title+'\n')
    # 寻找点赞数等
    content = soup.find('h5').find_all('span')
    for j in content:
        f.write(j.get_text()+'\n')
    f.write('\n')
f.close()
