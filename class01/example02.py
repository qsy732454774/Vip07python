# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/15 23:02
@Author      : QSY
@Funtion    : 数据类型
"""

# 整数 小数
x = 1
y = 1.1
print(type(x), type(y))

# 字符串

s = "123字符串"
print(s)

# 布尔类型
b = False
print(type(b))

# 使用一个变量或者对象之前，需要先判断是否为空
x = None
if x:
    print(x + 1)
else:
    print("x值是None")
