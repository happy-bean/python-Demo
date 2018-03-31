#!/usr/bin/python
# -*- coding: UTF-8 -*-



# Python JSON
#
# 本章节我们将为大家介绍如何使用 Python 语言来编码和解码 JSON 对象。
#
# JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。
# JSON 函数
#
# 使用 JSON 函数需要导入 json 库：import json。
# 函数	描述
# json.dumps 	将 Python 对象编码成 JSON 字符串
# json.loads	将已编码的 JSON 字符串解码为 Python 对象
# json.dumps
#
# json.dumps 用于将 Python 对象编码成 JSON 字符串。
# 语法
#
# json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)
#
# 实例
#
# 以下实例将数组编码为 JSON 格式数据：

import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = json.dumps(data)
print json

# 参考 http://www.runoob.com/python/python-json.html

#
# json.loads
#
# json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
# 语法
#
# json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print text


# 使用第三方库：Demjson
#
# Demjson 是 python 的第三方模块库，可用于编码和解码 JSON 数据，包含了 JSONLint 的格式化及校验功能。
#
# Github 地址：https://github.com/dmeranda/demjson
#
# 官方地址：http://deron.meranda.us/python/demjson/
# 环境配置
#
# 在使用 Demjson 编码或解码 JSON 数据前，我们需要先安装 Demjson 模块。本教程我们会下载 Demjson 并安装：
#
# $ tar -xvzf demjson-2.2.3.tar.gz
# $ cd demjson-2.2.3
# $ python setup.py install
#
# 更多安装介绍查看：http://deron.meranda.us/python/demjson/install


# JSON 函数
# 函数	描述
# encode 	将 Python 对象编码成 JSON 字符串
# decode	将已编码的 JSON 字符串解码为 Python 对象
# encode
#
# Python encode() 函数用于将 Python 对象编码成 JSON 字符串。
# 语法
#
# demjson.encode(self, obj, nest_level=0)


import demjson

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = demjson.encode(data)
print json


# decode
#
# Python 可以使用 demjson.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型。
# 语法
#
# demjson.decode(self, txt)
#
# 实例
#
# 以下实例展示了Python 如何解码 JSON 对象：



json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = demjson.decode(json)
print  text

