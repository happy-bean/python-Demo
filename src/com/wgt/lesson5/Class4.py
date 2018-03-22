#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 类属性与方法
# 类的私有属性
#
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
# 类的方法
#
# 在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
# 类的私有方法
#
# __private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount


counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter.__secretCount  # 报错，实例不能访问私有变量

# 单下划线、双下划线、头尾双下划线说明：
#
#     __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
#
#     _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
#
#     __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。


# 新式类和经典类的区别：

class A:
   def foo(self):
      print('called A.foo()')
class B(A):
   pass
class C(A):
   def foo(self):
      print('called C.foo()')
class D(B, C,object):
   pass

if __name__ == '__main__':
   d = D()
   d.foo()

# D 继承了 object 和不继承程序输出不一样，继承 object 会调用 C 类的 foo，否则会调用 Ａ 的。
#
# 使用 super 进行父类构造调用那么必须使用 object 继承的新式类，否则报错。