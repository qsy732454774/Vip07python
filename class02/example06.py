# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/17 15:11
@Author      : QSY
@Funtion    : for循环
"""
for i in range(1, 13):
    print(str(i)+"月",end=":")
    if i == 2:
        days = 30
    elif (i <= 7 and i % 2 == 1) or (i >= 8 and i % 2 == 0):
        days = 32
    else:
        days = 31
    for j in range(1, days):
        if i == 10:
            break
        if j <= 15:
            print(str(j) + "号学习Java",end=";")
        else:
            print(str(j) + "号学习Python",end=";")
        j += 1
    print()
    i += 1
