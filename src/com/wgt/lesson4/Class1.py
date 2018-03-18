#!/usr/bin/python
# -*- coding: UTF-8 -*-


# Python 函数
# 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
#
# 函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。
#
# 定义一个函数
# 你可以定义一个由自己想要功能的函数，以下是简单的规则：
#
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
# 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
# 语法
# def functionname( parameters ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]

def printme( str ):
   "打印传入的字符串到标准显示设备上"
   print str
   return

# 函数调用
# 定义一个函数只给了函数一个名称，指定了函数里包含的参数，和代码块结构。
#
# 这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从Python提示符执行。
#
# 如下实例调用了printme（）函数：

# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");

# python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

# python 传不可变对象实例



def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print b
# 结果是 2
# 实例中有 int 对象 2，指向它的变量是b，在传递给ChangeInt函数时，按传值的方式复制了变量
# b，a 和 b都指向了同一个Int 对象，在a = 10 时，则新生成一个】int值对象10，并让a指向它。


# 传可变对象实例

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist

# 参数
# 以下是调用函数时可使用的正式参数类型：
#
# 必备参数
# 关键字参数
# 默认参数
# 不定长参数
# 必备参数
# 必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
#
# 调用printme()函数，你必须传入一个参数，不然会出现语法错误：

# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
#
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
#
# 以下实例在函数 printme() 调用时使用参数名

printme( str = "My string");


#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name;
   print "Age ", age;
   return;

#调用printinfo函数
printinfo( age=50, name="miki" );

# 缺省参数
# 调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：

# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;


# 调用printinfo函数
printinfo(age=50, name="miki");
printinfo(name="miki")

# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：

# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return;


# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);

# 匿名函数
# python 使用 lambda 来创建匿名函数。
#
# lambda只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。


# 语法
# lambda函数的语法只包含一个语句，如下：
#
# lambda [arg1 [,arg2,.....argn]]:expression

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print "相加后的值为 : ", sum(10, 20)
print "相加后的值为 : ", sum(20, 20)

# return 语句
# return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，下例便告诉你怎么做：

# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print "函数内 : ", total
    return total;


# 调用sum函数
total = sum(10, 20);


# 变量作用域
# 一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。
#
# 变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：
# 全局变量
# 局部变量

# 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
#
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。如下实例：

total = 0;  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print "函数内是局部变量 : ", total
    return total;


# 调用sum函数
sum(10, 20);
print "函数外是全局变量 : ", total
#
# import 语句
# 模块的引入
# 模块定义好后，我们可以使用 import 语句来引入模块，语法如下：
#
# import module1[, module2[,... moduleN]
# 比如要引用模块 math，就可以在文件最开始的地方用 import math 来引入。在调用 math 模块中的函数时，必须这样引用：
#
# 模块名.函数名

# 当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
#
# 搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块 support.py，需要把命令放在脚本的顶端：

# # 导入模块
# import support
#
# # 现在可以调用模块里包含的函数了
# support.print_func("Runoob")


# from…import 语句
# Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
#
# from modname import name1[, name2[, ... nameN]]
# 例如，要导入模块 fib 的 fibonacci 函数，使用如下语句：
#
# from fib import fibonacci
# 这个声明不会把整个 fib 模块导入到当前的命名空间中，它只会将 fib 里的 fibonacci 单个引入到执行这个声明的模块的全局符号表。


# from…import* 语句
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
#
# from modname import *
# 这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。
#
# 例如我们想一次性引入 math 模块中所有的东西，语句如下：
#
# from math import *


# 搜索路径
# 当你导入一个模块，Python 解析器对模块位置的搜索顺序是：
#
# 1、当前目录
# 2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
# 3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
# 模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。
#
#
# PYTHONPATH 变量
# 作为环境变量，PYTHONPATH 由装在一个列表里的许多目录组成。PYTHONPATH 的语法和 shell 变量 PATH 的一样。
#
# 在 Windows 系统，典型的 PYTHONPATH 如下：
#
# set PYTHONPATH=c:\python27\lib;
# 在 UNIX 系统，典型的 PYTHONPATH 如下：
#
# set PYTHONPATH=/usr/local/lib/python

# dir() 函数
# dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
#
# 返回的列表容纳了在一个模块里定义的所有模块，变量和函数。如下一个简单的实例：


# 导入内置math模块
import math

content = dir(math)

print content;