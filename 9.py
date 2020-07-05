# 获取此文章的点赞数和评论数。
# 我们可以看到点赞和评论数，但在f12里面一看是方框
# 直接爬是&#xF52C;&#xF51D;&#xF369;&#xe072;
# 。。。仔细看有个class是num，应该是css的字体
# 查看他的css有个‘http://47.104.29.136:8000/static/tasks/css/svgtextcss/a0f3498f963cb4af89a535c674d63493.css
# @font-face
# {
# 	font-family: "PingFangSC-Regular-num";
# 	src:url("../../fonts/3526468f.eot");
# 	src:url("../../fonts/3526468f.eot?#iefix") format("embedded-opentype"),url("../../fonts/3526468f.woff");
# }
# .num
# {
# 	font-family: 'PingFangSC-Regular-num';
# }
# 意思就是加了个特殊的字体
# 找出对应的数字与编码的对应关系
# 有的网站比较复杂 每次对应关系不同 可能用别的工具 暂不介绍
# 给一个字体PingFangSC-Regular下载链接https://github.com/zongren/font/blob/master/PingFang-SC-Regular.ttf
import requests
from bs4 import BeautifulSoup
# 本来不想写正则，bs的text有问题 那个&#xF51D;会被解码为奇怪的汉字 造成无法匹配。。。
import re


# 大小写可能有问题。。。
num_dict = [{'code': 'F52C', 'no': 1}, {'code': 'e072', 'no': 2}, {'code': 'f2bd'.upper(), 'no': 3},
            {'code': 'f51d'.upper(), 'no': 4},
            {'code': 'f7d9'.upper(), 'no': 5}, {'code': 'e52c'.upper(), 'no': 6}, {'code': 'f783'.upper(), 'no': 7},
            {'code': 'e8b8'.upper(), 'no': 8}, {'code': 'eb7f'.upper(), 'no': 9}, {'code': 'f369'.upper(), 'no': 0}]
url = 'http://47.104.29.136:8000/tasks/tutorial/1/'
parser = 'html.parser'
# 设置报头，Http协议
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 '
                  'Safari/537.36'}
cookie_str = 'csrftoken=KoVAJsa72bQ4osEwm7Mebwn4hFVKhNgFjlN0j8WOVymm0EbQg7cvFqvPA8XL1yX4;sessionid' \
             '=gnrl6rquz0rrm0anarlsq20cait6t4yn '
# 把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
response = requests.get(url, cookies=cookies, headers=header)
response.encoding = 'utf-8'

# 寻找点赞数等
# soup = BeautifulSoup(response.text, parser)
# content = soup.find('h5').find_all('span')
# like_no = content[2].get_text()
# print(str(like_no))
# comments_no = content[3].get_text()
# print(comments_no)

like_no, comments_no = re.findall(r'<span class="num">(.*?)</span>', response.text)

for i in range(len(num_dict)):
    code = '&#x' + num_dict[i]['code'] + ';'
    print(code)
    if code in like_no:
        like_no = like_no.replace(code, str(num_dict[i]['no']))
for i in range(len(num_dict)):
    code = '&#x' + num_dict[i]['code'] + ';'
    if code in comments_no:
        comments_no = comments_no.replace(code, str(num_dict[i]['no']))
f = open('9result.txt', 'w')
f.write(like_no)
f.write(comments_no)
