# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/17 15:55
@Author      : QSY
@Funtion    : 2000-2099年，判断闰年，打印出每年/每月/每日 做什么
"""
for y in range(2000, 2100):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print(str(y) + "年是闰年")
    else:
        print(str(y) + "年是平年")
    for m in range(1, 13):
        if m <= 7 and m % 2 == 1 or m >= 8 and m % 2 == 0:
            days = 31
        elif m == 2:
            if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
                days =29
            else:
                days =28

        else:
            days = 30
        for i in range(1, days + 1):
            if days <= 15:
                print(str(y) + "-" + str(m) + "-" + str(i) + "号学习Java", end=";")
            else:
                print(str(y) + "-" + str(m) + "-" + str(i) + "号学习Python", end=";")
            i += 1
        print()
        m += 1

    y += 1
