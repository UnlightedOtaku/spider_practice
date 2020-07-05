# 通过网站的 API 接口，批量下载文章对应题图到本地。
import requests
import os
import json


url = 'http://47.104.29.136:8000/tasks/api/'
base_url = 'http://47.104.29.136:8000'
# 请求
result = requests.get(url)

# 当前文件夹
cur_path = os.getcwd() + '/'
# 存储路径
pic_path = cur_path + '2results'
# 新建文件夹
if os.path.exists(pic_path):
    print('directory exist!')
else:
    os.mkdir(pic_path)
# 进入目录，开始下载
os.chdir(pic_path)

# 解析结果
# print(result.content) bytes
# print(result.text) unicode
# json解析字符串，当让也可以通过正则 或者肉眼观察图片的url
json_result = json.loads(result.text)
# print(json_result)
print(json_result['articles'])
for i in json_result['articles']:
    # print(i)
    # print(i['image'])
    # 文件名
    filename = i['image'].split('/')[-1]
    # 图片的url
    img_url = base_url + i['image']
    # 打开文件 ， 写入 ， 关闭
    f = open(filename, 'wb')
    f.write(requests.get(img_url).content)
    f.close()
