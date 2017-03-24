:       #作为结尾说明下一行缩进的是代码块
    
\   #转义字符

\n  #换行

r'something' #内部的字符串默认不转义

'''something1

something2''' #表示多行内容

None #特殊的空值

#变量名必须是大小写英文、数字和_的组合，且不能用数字开头

PI = 3.14159265359 #所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量

/ #除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数

// #称为地板除，两个整数的除法仍然是整数,只取结果的整数部分

% #余数运算，可以得到两个整数相除的余数

ord()#函数获取字符的整数表示

chr()#函数把编码转换为对应的字符

b'something' #bytes类型的数据

str #字符串类型

encode() #str通过encode()方法可以编码为指定的bytes,eg:
>>> 'ABC'.encode('ascii')
b'ABC'
#含有中文的str可以用UTF-8编码为bytes。
#含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

len()  #计算str包含多少个字符,计算bytes字节数，计算list元素个数

ascii

unicode

utf-8

%s #表示用字符串替换

%d #表示用整数替换

%f #浮点数

%x #十六进制整数

%% #表示一个%,普通字符
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'

'%3.5' % num #整数字前占3位，小数保留5位

list #有序的集合

#删除list指定位置的元素，用pop(i)，eg：
mate.pop(2)

#往list中追加元素到末尾
mate.append()

#把元素插入到指定的位置
mate.insert(1,something)

tuple #元组，tuple一旦初始化就不能修改
#定义一个只有1个元素的tuple
>>> t = (1,)

elif #else if的缩写

#if语句从上往下按顺序判断

int() #将str转换成整数，eg：
s = input('birth: ')
birth = int(s)

for x in ...  #循环就是把每个元素代入变量x，然后执行缩进块的语句

list(range(num)) #生成0至num-1的整数序列

while #条件循环，只要满足条件，就会循环下去

dict #eg:
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95

in #判断key是否在dic内：
>>> 'Thomas' in d
False

get #也用于判断key是否在dic内，如果key不存在，可以返回None，或者自己指定的value：
>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1
#注意：返回None的时候Python的交互式命令行不显示结果

d.pop(key) #将key与value在dic中删除

#dict的key必须是不可变对象,在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

#要创建一个set，需要提供一个list作为输入集合
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}

set(somelist)
#重复元素在set中自动被过滤

add(key) #添加元素到set中，可以重复添加，但不会有效果
>>> s.add(4)

remove(key) #删除元素

#set可以看成数学意义上的无序和无重复元素的集合

& #取交集
| #取并集

def #定义函数,eg:
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。

#return None可以简写为return

from something import something #导入函数

pass #该语句什么都不做，作为占位符

isinstance() #数据类型检查

import math #导入math包

#函数可以同时返回多个值，但其实就是一个tuple

#定义默认参数要牢记一点：默认参数必须指向不变对象

#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号

#可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个

#关键字参数可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。
 #试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求

#命名关键字参数必须传入参数名
#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
#如果缺少*，Python解释器将无法识别位置参数和命名关键字参数

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数


汉诺塔看不懂！！！！！

[num1;mum2] #切片操作：取出第num1+1个到num2-1个，可对list、tuple、str操作

#迭代(遍历整个对象）：
#迭代dict的key（默认）：
for something in name

#迭代dict的value：
for something in name.values()

#迭代dict的key和value：
for something1,something2 in name.items()

#判断一个对象是可迭代对象:
>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True

#把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身:
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C

list(range(1,11)) #生成[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100] #偶数的平方

>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ'] #生成全排列

>>> isinstance(x, str)
True #判断一个变量是不是字符串

>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630> #，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#称为生成器：generator

next() #通过next()函数获得generator的下一个返回值
>>> next(g)
0

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
#生成斐波那契数列的generator，yield b 相当于print(b)

#可以直接作用于for循环的对象统称为可迭代对象：Iterable
#可以使用isinstance()判断一个对象是否是Iterable对象

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#可以使用isinstance()判断一个对象是否是Iterator对象







