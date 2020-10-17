# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/17 21:05
@Author      : QSY
@Funtion    : 判断用户名密码是都合法
"""

user = input(str("请输入账号："))
pwd = input(str("请输入密码："))

x = len(user)
y = len(pwd)

if x < 6 or x > 16:
    print("用户名不合法")
elif y < 6 or y > 16:
    print("密码不合法")
else:
    print("登录成功")
