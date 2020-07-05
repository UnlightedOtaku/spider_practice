# 从 Python 入门指南 教程列表页分别进入每一篇 python 教程，登录后抓取第十一课到第二十课教程的文章内容。
#
# 账号登录用户名为：qx，密码为：qx123。另外，也可以通过在命令行输入 python manage.py createsuperuser 新建用户后登陆。
# 法一 利用cookie登陆，见7-1
# 法二 模拟登录发送请求
import requests
from bs4 import BeautifulSoup
import os
import time


base_url = 'http://47.104.29.136:8000/tasks/tutorial/'
login_url = 'http://47.104.29.136:8000/accounts/login/'
parser = 'html.parser'
# 设置报头，Http协议
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 '
                  'Safari/537.36'}
# 当前文件夹
cur_path = os.getcwd() + '/'
# 存储路径
pic_path = cur_path + '7-2results'
# 新建文件夹
if os.path.exists(pic_path):
    print('directory exist!')
else:
    os.mkdir(pic_path)
# 进入目录，开始下载
os.chdir(pic_path)

# 虽然我们不通过cookie登陆，但是django自带防止csrf攻击所以需要一个csrf的cookie，当然 可以先get一下 在获取这个cookie
cookie_str='Cookie: order=id%20desc; memSize=1993; vcodesum=12; backup_path=/www/backup; serverType=apache; ' \
           'sites_path=/www/wwwroot; force=0; load_page=null; load_search=undefined; load_type=null; ' \
           'uploadSize=1073741824; rank=a; aceEditor=%7B%22fontSize%22%3A%2213px%22%2C%22theme%22%3A%22monokai%22%7D; ' \
           'BT_PANEL_6=77b28554-12e1-4634-8be1-188ed272593e.fI56BRSBk9pmrSZBqZxHC-WZvrs; ' \
           'request_token=rIHDgPGVu8H7nvng6c2qbmcOXIQ8zsQ4chB2jKH0ARqCUCFW; layers=7; ' \
           'Path=/www/wwwroot/pa/purple_mountain/mysite; ' \
           'csrftoken=1OH5gVIMkbxFn0Gq6F4Od0koZCm5IytO8NO9ZrABS1NJ1gVLLjWwrsmT7MwuCkoO '
# 就是这玩意，不知道为什么，我感觉可能作者关掉django自带的csrf防护比较好
# 注意cookie最后少了sessionid
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
session = requests.session()
# 设置表单
form_data = {
    # 注意csrf，可以自己进入登录页 点一下 看f12 network 里面提交一个空表单可见form_data
    'csrfmiddlewaretoken': 'p8evSqoG8fgqpJ7LFCEC4PGxfEbJakInw7lzBWgvG5wu3Zm6kgwkihI2nOl846Dn',
    'username': 'qx',
    'password': 'qx123'
}
response = session.post(login_url, headers=header, data=form_data, cookies=cookies)
# 只演示了一个 其他循环即可
if response.status_code == 200:
    time.sleep(3)
    # 注意参数名是headers，因为实际上可以准备多个header，失效自动切换
    true_url = base_url + '14'
    result = session.get(true_url, headers=header)
    result.encoding = 'utf-8'
    print(result.text)
    # 解析html
    soup = BeautifulSoup(result.text, parser)
    f = open('14.html', 'w', encoding='utf-8')
    f.write("<head><meta charset='UTF-8'></head>")  # 一开始忘了加了。。。
    # 标题
    title = soup.find('h2').get_text()
    f.write(f'<h2>{title}</h2>')
    content = soup.find('div', attrs={'class': 'ppx-main-block'}).get_text()
    f.write(content)
    f.close()
else:
    print(response.text)
