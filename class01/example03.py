# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/15 23:11
@Author      : QSY
@Funtion    : 数据类型要点
"""

# 转义  \
s = "\""
print(s)
# 把无特殊含义的符号转义为有特殊含义的字符
print("a\tn\na")

# 类型的互斥

i = 1
f = 1.1
s = "aaaa"

b = True
n = None

print(i + f)
print(i + b)
# 强转
print(str(i) + s)
