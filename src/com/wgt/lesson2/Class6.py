#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python continue 语句
#
# Python continue 语句跳出本次循环，而break跳出整个循环。
#
# continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
#
# continue语句用在while和for循环中。

# 第一个实例
for letter in 'Python':
    if letter == 'h':
        continue
    print '当前字母 :', letter

# 第二个实例
var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print '当前变量值 :', var
print "Good bye!"

# Python pass 语句
#
# Python pass是空语句，是为了保持程序结构的完整性。
#
# pass 不做任何事情，一般用做占位语句。

for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter

print "Good bye!"