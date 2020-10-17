# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/17 20:00
@Author      : QSY
@Funtion    : while循环
"""

# 一半乘法表
x = 1
while x <= 9:
    print()
    y = 1
    while y <= 9:
        if x <y:
            break
        print(str(x)+"*"+str(y)+"="+str(x*y),end="     ")

        y+=1

    x += 1

# 去除对角线
x = 1
while x <= 9:
    print()
    y = 1
    while y <= 9:
        if x == y or x+y ==10:
            print(end="      ")
        else:
            print(str(x) + "*" + str(y) + "=" + str(x * y), end=" ")
        y += 1
    x += 1
