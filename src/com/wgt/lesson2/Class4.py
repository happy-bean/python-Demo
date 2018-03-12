#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python 循环嵌套
#
# Python 语言允许在一个循环体里面嵌入另一个循环


# Python for 循环嵌套语法：
# for iterating_var in sequence:
#    for iterating_var in sequence:
#       statements(s)
#    statements(s)
#
# Python while 循环嵌套语法：
# while expression:
#    while expression:
#       statement(s)
#    statement(s)

num=[];
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)

i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print i, " 是素数"
    i = i + 1

print "Good bye!"