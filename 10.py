# 获取此文章的的阅读数。
# js加密
# 其实就是用python实现一次js处理的过程。。。
# 控制台可看 join_str = "0.26800046209008066"
# 其实js里写了
# readcount = '250.26800046209008066310.2680004620900806670.26800046209008066610.2680004620900806643';
# join_str = '0.26800046209008066';
# num_list = '6541237089';
# 可以看js文件
# var _0x345e = ["\x73\x70\x6C\x69\x74", "\x67\x65\x74\x46\x75\x6C\x6C\x59\x65\x61\x72", "\x67\x65\x74\x4D\x6F\x6E\x74\x68", "\x67\x65\x74\x44\x61\x74\x65", "", "\x6C\x65\x6E\x67\x74\x68"];
# // 上述代码可以解码 或者直接alert
# if (readcount) {
#     var datacomponents = readcount[_0x345e[0]](join_str);
#     var date = new Date();
#     var year = date[_0x345e[1]]();
#     var month = date[_0x345e[2]]() + 1;
#     var day = date[_0x345e[3]]();
#     var orginalMessage = _0x345e[4];
#     for (var index = 0; index < datacomponents[_0x345e[5]]; index++) {
#         var datacomponent = datacomponents[index];
#         if (!isNaN(datacomponent)) {
#             var currentNumber = parseInt(datacomponent);
#             orginalMessage += (currentNumber - month) / day
#         }
#     }
#     ;var str_end = _0x345e[4];
#     for (var i = 0; i < orginalMessage[_0x345e[5]]; i++) {
#         str_end += num_list[orginalMessage[i]]
#     }
# }

import requests
from bs4 import BeautifulSoup
import re
import datetime

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
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select("head  script")
thescript = result[4].__repr__()
# 获取变量
p = re.compile(r"var readcount = '(.*?)';")
m = p.search(thescript)
readcount = m.groups()[0]
p = re.compile(r"var join_str = '(.*?)';")
m = p.search(thescript)
join_str = m.groups()[0]
p = re.compile(r"var num_list = '(.*?)';")
m = p.search(thescript)
num_list = m.groups()[0]

datacomponents = readcount.split(join_str)
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
orginalMessage = []
for i in range(len(datacomponents)):
    if datacomponents[i]:
        currentNumber = int(datacomponents[i])
        orginalMessage.append(int((currentNumber - month) / day))
str_end = ''
for i in range(len(orginalMessage)):
    str_end += num_list[orginalMessage[i]]
print(str_end)
# 12697
