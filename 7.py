# 从 Python 入门指南 教程列表页分别进入每一篇 python 教程，登录后抓取第十一课到第二十课教程的文章内容。
#
# 账号登录用户名为：qx，密码为：qx123。另外，也可以通过在命令行输入 python manage.py createsuperuser 新建用户后登陆。
# 法一 利用cookie登陆
# 法二 模拟登录发送请求,见7-2
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
# 首先用浏览器登录，得到cookie
cookie_str = 'order=id%20desc; memSize=1993; vcodesum=12; backup_path=/www/backup; serverType=apache; ' \
         'sites_path=/www/wwwroot; force=0; load_page=null; load_search=undefined; load_type=null; ' \
         'uploadSize=1073741824; rank=a; aceEditor=%7B%22fontSize%22%3A%2213px%22%2C%22theme%22%3A%22monokai%22%7D; ' \
         'BT_PANEL_6=77b28554-12e1-4634-8be1-188ed272593e.fI56BRSBk9pmrSZBqZxHC-WZvrs; ' \
         'request_token=rIHDgPGVu8H7nvng6c2qbmcOXIQ8zsQ4chB2jKH0ARqCUCFW; layers=7; ' \
         'Path=/www/wwwroot/pa/purple_mountain/mysite; ' \
         'csrftoken=1OH5gVIMkbxFn0Gq6F4Od0koZCm5IytO8NO9ZrABS1NJ1gVLLjWwrsmT7MwuCkoO; ' \
         'sessionid=5fipq2qnwyic5ofir0czhh4uli9adt8t '
# 把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

# 当前文件夹
cur_path = os.getcwd() + '/'
# 存储路径
pic_path = cur_path + '7results'
# 新建文件夹
if os.path.exists(pic_path):
    print('directory exist!')
else:
    os.mkdir(pic_path)
# 进入目录，开始下载
os.chdir(pic_path)

# print(cookies)
for i in range(12, 21):
    true_url = base_url + str(i)
    # 注意参数名是headers，因为实际上可以准备多个header，失效自动切换
    result = requests.get(true_url, headers=header, cookies=cookies)
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