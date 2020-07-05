# 从 Python 入门指南 教程列表页分别进入每一篇 python 教程，抓取前十课 python 教程（截止到：10. 变量2）的文章内容（不包括阅读数、点赞数和评论数）。
#
# 注意：如果你在短时间抓取了很多篇 python 教程相关文章（频率大于 10 分钟 30 次的访问），那么你的 ip 地址会被封禁一段时间（10 分钟）

# 添加header ， 加上sleep即可
import requests
from bs4 import BeautifulSoup
import os
import time


base_url = 'http://47.104.29.136:8000/tasks/tutorial/'
parser = 'html.parser'
# 设置报头，Http协议
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 '
                  'Safari/537.36'}

# 当前文件夹
cur_path = os.getcwd() + '/'
# 存储路径
pic_path = cur_path + '6results'
# 新建文件夹
if os.path.exists(pic_path):
    print('directory exist!')
else:
    os.mkdir(pic_path)
# 进入目录，开始下载
os.chdir(pic_path)

# 虽然文章是0.但url是1开始。。。
for i in range(1, 12):
    true_url = base_url + str(i)
    # 注意参数名是headers，因为实际上可以准备多个header，失效自动切换
    result = requests.get(true_url, headers=header)
    result.encoding = 'utf-8'
    print(result.text)
    # 解析html
    soup = BeautifulSoup(result.text, parser)
    f = open(f'{i}.html', 'w', encoding='utf-8')
    f.write("<head><meta charset='UTF-8'></head>")  # 一开始忘了加了。。。
    # 标题
    title = soup.find('h2').get_text()
    f.write(f'<h2>{title}</h2>')
    content = soup.find('div', attrs={'class': 'ppx-main-block'}).get_text()
    f.write(content)
    f.close()
    # 暂停10min 30次 10*60/30 == 20
    time.sleep(20)
