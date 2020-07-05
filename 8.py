# 在 Python 入门指南 的列表页面上，有一个新增文章的选项，允许登录后的用户发布教程文章。请模拟 post 请求实现自动发文的功能。
# 在之前7的法一的基础上继续
import requests


add_url = 'http://47.104.29.136:8000/tasks/tutorial/new/'
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
# 设置表单
form_data = {
    # 注意csrf，可以自己进入登录页 点一下 看f12 network 里面提交一个空表单可见form_data
    'csrfmiddlewaretoken': 'SR8TkLHCnaaARvBLxchwBPLbAfOrwaMBrO0jUrtjgxGStH85rcHN5JTWTIQsgVt0',
    'title': 'post请求测试',
    'index': 100,
    'content': '一个用python添加的'
}
requests.post(add_url, headers=header, cookies=cookies, data=form_data)
# 可能网站的作者没有写response，不过可以去页面查看 已经增加成功
# response = requests.post(add_url, headers=header, cookies=cookies, data=form_data)
# print(response)
