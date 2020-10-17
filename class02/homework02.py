# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/17 16:32
@Author      : QSY
@Funtion    : 乘法表
"""
# 乘法表整体
for i in range(1, 10):
    for j in range(1, 10):
        print(str(i) + "*" + str(j) + "=" + str(i * j), end=" ")
        j += 1
    print()
    i += 1

#  半个乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(str(i) + "*" + str(j) + "=" + str(i * j), end=" ")
        j += 1
        if j > i:
            break
    print()
    i += 1

#  半个乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(str(i) + "*" + str(j) + "=" + str(i * j), end=" ")
#         j += 1
#         if j > i:
#             break
#     print()
#     i += 1

# 去除对角线
for i in range(1, 10):
    for j in range(1, 10):

        if i == j or i+j ==10:
            print(end="      ")
            continue

        print(str(i) + "*" + str(j) + "=" + str(i * j), end=" ")
        j += 1

    print()
    i += 1