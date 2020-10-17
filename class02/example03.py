# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/17 13:51
@Author      : QSY
@Funtion    : 逻辑运算
"""
# bool值运算
# x = int(input("请输入值："))
# b1 = x > 0
# print(b1)
# b2 = x < 100
# print(b2)
# print(b1 and b2)
# print(b1 or b2)

# 逻辑运算优先级 not > and > or

b1 = True
b2 = True
b3 = False

print(b1 or b2 and b3)

# 短路原则
x = 1
y = 2
z = 2

print(x > y and y == z)
print(x < y or y < z)
