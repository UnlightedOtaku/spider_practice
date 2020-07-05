# 获取 Django girl 教程中的全部教程内容并保存为本地的 HTML 文件。
# ajax即异步的js和xml
# 这种是动态网页
# 通常对于用了ajax的网页，两种方法，找到真实的url,使用浏览器如无头浏览器和webdriver操控chrome
# 这里我选择找到真实的url
import os
import requests

original_url = 'http://47.104.29.136:8000/static/tasks/djangogirl/djangogirl.html'
base_url = 'http://47.104.29.136:8000/static/tasks/djangogirl/'
parser = 'html.parser'

# 当前文件夹
cur_path = os.getcwd() + '/'
# 存储路径
pic_path = cur_path + '5results'
# 新建文件夹
if os.path.exists(pic_path):
    print('directory exist!')
else:
    os.mkdir(pic_path)
# 进入目录，开始下载
os.chdir(pic_path)

# 保存原始网页
result = requests.get(original_url)
result.encoding = 'utf-8'
# 保存网页为html
f = open('djangogirl.html', 'w', encoding='utf-8')
f.write(result.text)
f.close()

# 保存加载的内容网页
for i in range(18):
    # 使用f-string来拼接字符串
    true_url = base_url + f'content{i}.html'
    result = requests.get(true_url)
    result.encoding = 'utf-8'
    # 保存网页为html
    f = open(f'content{i}.html', 'w', encoding='utf-8')
    f.write(result.text)
    f.close()
    print(result.text)
