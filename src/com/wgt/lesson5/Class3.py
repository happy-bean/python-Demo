#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 类的继承
#
# 面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。继承完全可以理解成类之间的类型和子类型关系。
#
# 需要注意的地方：继承语法 class 派生类名（基类名）：//... 基类名写在括号里，基本类是在类定义的时候，在元组之中指明的。
#
# 在python中继承中的一些特点：
#
#     1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
#     2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别在于类中调用普通函数时并不需要带上self参数
#     3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
#
# 如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
#
# 语法：
#
# 派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：
#
# class SubClassName (ParentClass1[, ParentClass2, ...]):
#    'Optional class documentation string'
#    class_suite


class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr


class Child(Parent):  # 定义子类
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print '调用子类方法'


c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值


# 你可以继承多个类
#
# class A:        # 定义类 A
# .....
#
# class B:         # 定义类 B
# .....
#
# class C(A, B):   # 继承类 A 和 B
# .....
#
# 你可以使用issubclass()或者isinstance()方法来检测。
#
#     issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
#     isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。


# 方法重写
#
# 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：

class Parent:  # 定义父类
    def myMethod(self):
        print '调用父类方法'


class Child(Parent):  # 定义子类
    def myMethod(self):
        print '调用子类方法'


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法


# 基础重载方法
#
# 下表列出了一些通用的功能，你可以在自己的类重写：
# 序号	方法, 描述 & 简单的调用
# 1	__init__ ( self [,args...] )
# 构造函数
# 简单的调用方法: obj = className(args)
# 2	__del__( self )
# 析构方法, 删除一个对象
# 简单的调用方法 : del obj
# 3	__repr__( self )
# 转化为供解释器读取的形式
# 简单的调用方法 : repr(obj)
# 4	__str__( self )
# 用于将值转化为适于人阅读的形式
# 简单的调用方法 : str(obj)
# 5	__cmp__ ( self, x )
# 对象比较
# 简单的调用方法 : cmp(obj, x)

# 运算符重载
#
# Python同样支持运算符重载，实例如下

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2
