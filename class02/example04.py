# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/17 14:26
@Author      : QSY
@Funtion    : if分支语句
"""
#
x = int(input("x:"))
y = int(input("y:"))

if x >= 0:
    if y >= 0:
        z = x + y
    else:
        z = x - y
else:
    if y >= 0:
        z = -x + y
    else:
        z = -x - y

print(z)
