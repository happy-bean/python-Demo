#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python数据类型转换

# 将x转换为一个整数
x = 10
y='1'
base = 10
# x -- 字符串或数字。base -- 可选，进制数，默认十进制。
int(y, base)
# 将x转换为一个长整数
long(x)
# 将x转换到一个浮点数
float(x)
# 创建一个复数 complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数
complex(1, 2)  # >>>(1 + 2j)

complex(1)  # 数字 >>>(1 + 0j)

complex("1")  # 当做字符串处理 >>>(1 + 0j)

# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
complex("1+2j")  # >>>(1 + 2j)

# 将对象x转换为字符串
str(x)
# 将对象x转换为表达式字符串
repr(x)

# 用来计算在字符串中的有效Python表达式, 并返回一个对象
eval( '3 * x' )

s = [1, 2, 3, 4]
# 将序列s转换为一个元组
tuple(s)
# 针对字典 会返回字典的key组成的tuple
tuple({1: 2, 3: 4})
# 元组会返回元组自身
tuple((1, 2, 3, 4))

# 将序列s转换为一个列表
s = (123, 'xyz', 'zara', 'abc')
list(s)

# 转换为可变集合
set(s)

# 创建一个字典。d必须是一个序列(key, value)元组。
dict()  # 创建空字典 >>>{}
dict(a='a', b='b', t='t')  # 传入关键字 >>>{'a': 'a', 'b': 'b', 't': 't'}
dict(zip(['one', 'two', 'three'], [1, 2, 3]))  # 映射函数方式来构造字典 >>>{'three': 3, 'two': 2, 'one': 1}
dict([('one', 1), ('two', 2), ('three', 3)])  # 可迭代对象方式来构造字典>>>{'three': 3, 'two': 2, 'one': 1}

# 转换为不可变集合
a = frozenset(range(10))  # 生成一个新的不可变集合>>>
print a
frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = frozenset('runoob')
print b
# frozenset(['b', 'r', 'u', 'o', 'n'])   # 创建不可变集合

# 将一个整数转换为一个字符
chr(x)

# 将一个整数转换为Unicode字符
unichr(x)

x = '2'
# 将一个字符转换为它的整数值
ord(x)

x = 1
# 将一个整数转换为一个十六进制字符串
hex(x)

# 将一个整数转换为一个八进制字符串
oct(x)
