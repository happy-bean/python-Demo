#!/usr/bin/python
# -*- coding: UTF-8 -*-

# for循环的语法格式如下：
#
# for iterating_var in sequence:
#    statements(s)

for letter in 'Python':  # 第一个实例
    print '当前字母 :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print '当前水果 :', fruit


# 通过序列索引迭代
#
# 另外一种执行循环的遍历方式是通过索引，如下实例：

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print '当前水果 :', fruits[index]

