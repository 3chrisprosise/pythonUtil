# -*- encoding:utf-8 -*-
from math import pi
import string

# # 整数除法 //
# print(3//2)  # 结果为 1

# #序列相加
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# print(list1+list2)

# #创建空列表
# squence = [None]*10
# print(squence)

# 判断成员

# date = ['Mon', 'Tue', 'Ths', 'Wen']
# print('Mon' in date)  # True
# print('Wen' in date)  # False
# print(len(date))  # 3 获取长度
# numbers = [22, 33, 44]
# print(max(date))  # 返回Tue  这里是如何判断的？
# print(max(numbers))  # 返回44  max对不同内容的处理

# # 列表元素删除
# date = ['Mon', 'Tue', 'Ths']
# del date[2]
# print(date)
# print(len(date)) # 删除元素后列表长度改变

# # 分片赋值
# numbers = [1, 5]
# num = [2, 3, 4]
# numbers[1:1] = num
# print(numbers)  # 这里直接将num插入到numbers中间
# print(len(numbers))
# print(numbers[1:4])
# numbers[1:4] = []
# print(numbers)
# print(len(numbers))  # 空列表不占位

# # 列表方法
# numbers = [1, 2, 3]
# numbers.append(4)
# numbers.append(4)
# numbers.append(4)
# numbers.append(4)
# print(numbers)
# print(numbers.count(4))  # 统计4出现的次数
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)  #利用列表拓展原有列表
#
# location = numbers.index(4)
# print(location)  # 只显示4 第一次出现的位置
#
# numbers.insert(4, 'ok')
# print(numbers)  # 在某个元素第一次出现的位置后方插入新的对象
#
# numbers.pop(3)  # 移除列表中某一个元素 默认为最后一个， 参数为元素的位置
# print(numbers)
#
# numbers.remove('ok')  # 移除列表中某个元素，参数为这个元素
# print(numbers)
#
# numbers.reverse()  # 列表中元素反序存放
# print(numbers)
#
# # numbers.insert('ok')
# numbers.sort()
# print(numbers)  # 改变原列表的排列顺序，按照一定的顺序,不是数字的排序会出错,而且sort函数不返回值
#
# after = sorted(numbers)  # sorted()可以用来获取副本
# print(after)

#
# # 元组
# source = (1, 2, 3)
# print(source)  #创建元组
#
# # 仅仅包含一个元素的元组
# print((3,))  # 这里的逗号非常重要

# 将列表转换为元组

# source = tuple([1, 2, 3])
# print(source)
#
# # 元组和列表的区别 1 元组可以在影射中当作键使用


# # 字符串操作
# fromat = "Pi with three decimals: %.3f"
# print(fromat % pi)
#
# print('%x' % 42)  # x 16进制
# print('%f' % pi)
# print('%10f' % pi)
# print('%10.2f' % pi)
# print('%.2f' % pi)
# print('%010f' % pi)  # 用0 填充空位
# print('%-020.2f' % pi)

# print(string.digits)  # 0-9 字符串
# print(string.ascii_letters)  # 所有大写和小写的字符
# print(string.ascii_lowercase)  # 所有小写字符
# print(string.ascii_uppercase)  # 所有大写字符
# print(string.printable)
# print(string.punctuation)  # 所有标点字符串

# str = ' This is a very long String '
# location = str.find('is')  # in只能用来查找单个字符，find可以查找一串字符
# print(location)  # 返回最左段索引，没有则返回-1
#
# seq = ['1', '2', '3', '4', '5', '6']
# sep = '+'.join(seq)
# print(sep)  # join 可以使用字符来连接字典中的元素
# str = str.lower()  # 转变为小写的字符串
# str = str.replace('is', 'is not')  # 替换字符串的内容
# str = str.strip() # 去除字符串两边的空格
#
# print(str)


# 字典操作
# d = dict(name='Chris', age=20)  # 创建字典
# print(len(d))
# del d['name']
# print(len(d))  # 删除键同样会释放空间
# print('age' in d)  # 查询字典中的键
# print('My age is %d' % d['age'])  # 字典格式化字符串
# # d.clear()  # 清空字典
# p = d.copy()  # 创建一个新的字典，内容与之前的内容相同
# p = d.fromkeys(['age', 'name', 'action'])
# print(p)  # 创建一个新的字典
# #print(d['name'])  # 这里会报错，因为没有name对应的值
# print(d.get('name'))  # 这里找不到键对应的值时候会返回None ，不会触发程序异常
# print(d.items())  # 将字典所有项以列表的形式返回
# print(d.__iter__())  # __iter__() 方法返回对象本身
# d['name'] = 'Chris'
# print(d)
# d.pop('name')  # 删除了字典中对应的项
# print(d)
# print(d.keys())  # 返回字典中的所有键
# d['name'] = 'Chris'
# d['action'] = 'run'
# d['eat'] = 'apple'
# d.popitem()
# print(d)  # 随即删除一个项，经过验证确实是随即的。。。。。
# d.setdefault('speak', 'loudly')
# #  如果没有对应的值，则创建一个健值，如果有，则返回对应键的值
# d.update({'name': 'Tom'})  # 覆盖或者添加对应的键值
# print(d)
# key, value = d.popitem()  # popitem() 随即删除项
# print(key)
# print(value)

# 链式赋值
# z= 3
# x=y=z
#
# # # 等价与
# print(x)
# print(y)
# # 这里的x与y共享一个地址？是的
# x = 4
# print(y)

# print(False==False)  #True
# print(False=={})  #False
# print(False==0)  # True
# print(False=='')  # False
# print(False==None) # False
# print(False==()) # False

# # 解释器会将以下的表达式看作假值
#
# print(bool(False))  # False
# print(bool({}))# False
# print(bool([]))# False
# print(bool(()))# False
# print(bool(None))# False
# # print(bool(''))# False
# # print(bool(0))# False
# z = 3
# p = 3
# x = z
# y = p
# print(x is y)  # is 运算符的结果有时不可测 ,少用
#
# print([2, 3, 4] < [1, 7, 8])  # False
# print([2, 3, 4] < [2, 7, 8])  # True
#
# # 比较符号  < > <=  >= 都是依照排列顺序比较的
#
# number = 7
# # 这种表达式可以简化
# if 0 <= number <= 7:
#     print('ok')

# 列表推导式

# list = [x*x for x in range(10)] # 这种循环返回一个列表
# print(list)
# list = [(x, y) for x in range(10) for y in range(10)]  # 共81 个点 ，相当于两个for循环嵌套
# print(list)

# del 可以用来删除无用对象

# 动态创建命名空间 py 3.0 不适用
# from math import sqrt
# scope = {}
# exec('sqrt = 1 in scope')
# print(sqrt)
# print(scope['sqrt'])

def add(x,y):
    '''
    两个数字的求和
    :param x: 一个数字
    :param y: 另一个数字
    :return: 求和
    '''
    return x + y

print(callable(add))  # 判断函数是否可以调用

# help(add)  # 函数的说明是存储在  .__doc__ 属性中的，在python 的内建函数help中可以查看这些函数的说明


# 两个变量引用同一个列表的时候其实是同时引用一个列表
list1 = ['one', 'two', 'three']
# list2 = list1
# list2[0] = 'apple'  # 这个操作会改变list1

list2 = list1[:]
list2[0] = 'apple'  # list2  获取了list1 的一个副本，并没有功共用一个列表
print(list1)
a=1
b=2
c=3
d=4
e=5
f=6
def lookuppara(*para):
    return para  # 这里返回的是一个元组
def lookuppara2(**para):
    return para  # 这里返回的是一个列表 两个 * 与一个 * 的区别

print(lookuppara(a, b, c, d, e, f))
print(lookuppara2(a=1, b=2, c=3, d=4, e=5, f=6))