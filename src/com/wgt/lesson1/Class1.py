#!/usr/bin/python
# -*- coding: UTF-8 -*-

 #python 中文编码

 #Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

 #解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了

 #注意：Python3.X 源码文件默认使用utf-8编码，所以可以正常解析中文，无需指定 UTF-8 编码。

 #注意：如果你使用编辑器，同时需要设置 py 文件存储的格式为 UTF-8，否则会出现类似以下错误信息：

print "Hello, World!";

print "你好，世界！"