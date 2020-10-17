# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/17 14:34
@Author      : QSY
@Funtion    : while循环
"""
# x = 1
# while x <= 31:
#     if x <= 15:
#         print(str(x) + "号学习Java")
#     else:
#         print(str(x) + "号学习Python")
#     x += 1

#
# m = 1
#
# while m <= 12:
#     x = 1
#     if m == 2:
#         while x <= 29:
#             if x <= 15:
#                 print(str(x) + "号学习Java")
#             else:
#                 print(str(x) + "号学习Python")
#             x += 1
#     elif (m <= 7 and m % 2 == 1) or (m >= 8 and m % 2 == 0):
#         while x <= 31:
#             if x <= 15:
#                 print(str(x) + "号学习Java")
#             else:
#                 print(str(x) + "号学习Python")
#             x += 1
#     else:
#         while x <= 30:
#             if x <= 15:
#                 print(str(x) + "号学习Java", end=";")
#             else:
#                 print(str(x) + "号学习Python", end=":")
#             x += 1
#     m += 1

x = 1

while x <= 12:
    if x == 2:
        days = 29
    elif (x <= 7 and x % 2 == 1) or (x >= 8 and x % 2 == 0):
        days = 31
    else:
        days = 30
    print(str(x) + "月", end=":")
    print()
    y = 1
    while y <= days:
        if days <= 15:
            print(str(y) + "号学习Java", end=";")
        else:
            print(str(y) + "号学习Python", end=";")
        y += 1

    print()
    x += 1
