# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/17 12:12
@Author      : QSY
@Funtion    : 输入模块功能
"""

x = 1
y = 2
z = 3

print(x < y < z)

s1 = "abcd"
s2 = "bcd"

print(s1 > s2)
# 字符串相等不等
print(s1 == s2)
print(s1 != s2)
# 包含
print(s1.__contains__(s2))

# 字符串运算

s1 = "ab"
s2 = "cd"

print(s1 + s2)
print(s1 * 3)
