# 将woff文件转为xml文件
from fontTools.ttLib import TTFont
# 加载字体文件：
font = TTFont('D:\\3526468f.woff')

# 转为xml文件：
# 给我康康
font.saveXML('wtf.xml')
