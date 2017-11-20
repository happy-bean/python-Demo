#!/usr/bin/python
# -*- coding: UTF-8 -*-


# Python 变量类型
#
# 变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间。
#
# 基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
#
# 因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。


# 变量赋值
#
# Python 中的变量赋值不需要类型声明。
#
# 每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
#
# 每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#
# 等号（=）用来给变量赋值。
#
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。


counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "python"  # 字符串


# 多个变量赋值
#
# Python允许你同时为多个变量赋值。
a = b = c = 1

# 以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
#
# 您也可以为多个对象指定多个变量。
a, b, c = 1, 2, "python"


# 标准数据类型
#
# 在内存中存储的数据可以有多种类型。
#
# 例如，一个人的年龄可以用数字来存储，他的名字可以用字符来存储。
#
# Python 定义了一些标准类型，用于存储各种类型的数据。
#
# Python有五个标准的数据类型：
#
#     Numbers（数字）
#     String（字符串）
#     List（列表）
#     Tuple（元组）
#     Dictionary（字典）

