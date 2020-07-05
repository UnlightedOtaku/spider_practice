# # 尝试绘制图片
# # 2-11 的对应 1-9 然后 0
# import matplotlib.pyplot as plt
# import re
#
# str = """"
#      <contour>
#         <pt x="297" y="714" on="1"/>
#         <pt x="262" y="674" on="0"/>
#         <pt x="160" y="612" on="0"/>
#         <pt x="111" y="598" on="1"/>
#         <pt x="111" y="516" on="1"/>
#         <pt x="212" y="546" on="0"/>
#         <pt x="279" y="614" on="1"/>
#         <pt x="279" y="0" on="1"/>
#         <pt x="361" y="0" on="1"/>
#         <pt x="361" y="714" on="1"/>
#     </contour>
# """
#
#
# x = [int(i) for i in re.findall(r'<pt x="(.*?)" y=', str)]
# y = [int(i) for i in re.findall(r'y="(.*?)" on=', str)]
#
# print(x)
# print(y)
#
# plt.plot(x, y)
# plt.show()
code = '&#xF52C' + ';'
code = code.encode('utf-8')
print(code)
