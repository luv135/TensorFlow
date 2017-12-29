#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'LuoWei'

# python学习笔记

# 条件判断
name = 'tangyaya'

if name == 'tangydaya':
    print('yes')
else:
    print('no')
###############################

# 默认浮点除法
print(10 / 3)
# 取整
print(10 // 3)

s1 = 72
s2 = 87
r = s2 / s1
# 格式化
print('%.2f%%' % (r))


###############################


# 函数定义
def move(x, y):
    return x + y, x - y


r = move(8, 3)
print(r)


###############################


# 默认参数
def power(value, n=2):
    if n == 1:
        return value
    return value * power(value, n - 1)


def power2(value, n=2):
    return power_inter(value, n, value)


# 尾递归优化,然后Python并不能
def power_inter(value, n, total):
    if n == 1:
        return total
    return power_inter(value, n - 1, value * total)


print(power2(2, 2))
###############################

# List
L = []
n = 1
while n <= 99:
    L.append(n)
    n += 2
print(L)
# 切片
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
r = L[1:3]
print(r)
###############################

# dict
d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(d[key])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for a, b in d.items():
    print(a, '= ', b)
###############################

L1 = ['Hello', 'World', 18, 'Apple', None]

print([s.lower() for s in L1 if isinstance(s, str)])


###############################


# 杨辉三角
def triangles():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i - 1] + N[i] for i in range(0, len(N))]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


###############################


# 高阶函数,参数f为一个函数,感觉类似于C中的函数地址.
def add(x, y, f):
    return f(x) + f(y)


def pw(v):
    return pow(v, 2)


print(add(-3, 2, pw))
###############################

# range初始化List
L = [i for i in range(1, 10)]
print(L)


def fun(x):
    return x * 10

# map使用,其会作用于List的每个item
r = map(fun, L)
r = list(r)
print(r)
###############################


# 字符数字转int
from functools import reduce


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


m = map(char2num, '123456')

# 转换成列表输出
m = list(m)
print(m)


def fn(x, y):
    return x * 10 + y


r = reduce(fn, m)
r = reduce(lambda x, y: x * 10 + y, m)
print(r)


#############################################
# 装饰器

def log(text):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            print('%s call %s():' % (text, fun.__name__))
            return fun(*args, **kwargs)

        return wrapper

    return decorator


# `@`标签添加装饰的函数
# @log('like')
def now(name):
    print('hello %s' % name)


now('ty')
# 另一种写法,去掉@log('like')标签
log('like')(now)("ty")
##########################################################

# 作用域
# 以下划线`_`开头表示private
##############################################


# 类
# 类名大写开头
# 私有属性双下划线`__`
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_scroe(self):
        return self.__score


def p(std):
    print(std.name, std.get_scroe())


s = Student('ty', 30)
p(s)


#####################################



# 继承,动态语言(鸭子类型)
class Animal(object):
    def run(self):
        print('Animal run...')


class Dog(Animal):
    def run(self):
        print('Dog run..')


def f(animal):
    animal.run()


class Plane(object):
    def run(self):
        print("plane fly")

# 动态语言,不强调继承关系,只需有相应的函数即可调用
f(Plane())
f(Dog())
f(Animal())



#######################################


# 异常捕获

import logging

try:
    r = 10 / 0
    print("try")
except ZeroDivisionError as e:
    print("except", e)
    logging.exception(e)
finally:
    print("finally")

#######################################

# 文件读写

with open('D:/1.txt') as f:
    print(f.read())
######################################

# json解析
import json


class Student(object):
    def __init__(self, name=None, score=None):
        self.name = name
        self.score = score


s = Student('z', 33)

dumps = json.dumps(s, default=lambda obj: obj.__dict__)
print(dumps)

t = Student()
t.__dict__ = json.loads(dumps)

print(t.name)
################################################