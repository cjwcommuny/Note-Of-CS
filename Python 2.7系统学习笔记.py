输入函数
    input(string) string 是提示,返回输入内容
    raw_input(string) 

输出语句
    print 
        eg1:
            >>>print 1,2,3 #每个参数之间插入空格
                1 2 3 

运算符
    比较运算符(比较运算符可以连接)
        x is y #x, y是同一个对象
        x is not y
        x in y
        x not in y
        x < y #也可用于字符串等的比较
    布尔运算符
        and
        or
        not


阶乘函数
    pow(x, y)
    x**y


导入模块
    eg1:
        import math
        math.floor(32.9)
    eg2:
        from math import sqrt, ceil
        sqrt(3)
    eg3:
        from math import * #导入所有函数
    eg4:
        import math as foobar #as语句为模块、函数创建别名
        from math import sqrt as sq


类型强制转换
    int()
    str()
    long()
    float()
    bool()

库及函数

    abs()
    pow(,)
    raw_input()
    repr(string) 将任何对象转换成供解释器阅读的字符串形式(即加上'')
    round()
    range(m, n) #产生[m,n)的元组
        range(n) #产生[0,n)的元组
        xrange()
    zip(sequence1, sequence2) #将两个序列压缩返回元组,处理不等长序列时，处理完短的为止
    enumerate(sequence) #返回索引-值 对
    vars()
    globals()
    map(function, iterable) 将函数逐个作用于可迭代对象的元素
    filter(function, iterable) 将函数(这个函数必须返回布尔值)作用于可迭代对象的元素。如果元素符合则放入列表(?)返回否则不返回
    issubclass(class1, class2) 判断class1 是否是 class2 的子类
    math 
        ceil()
        floor()
        sqrt()

    cmath
        sqrt()


    string
        字符串常量
            digits 包含 0~9 的数字
            letters 包含大写或小写的字母(与地区有关)
                ascii_letters 强制用ASCII字母
            lowercase
            uppercase
            printable   所有可打印的字符
            punctuation 所有标点
        函数
            capwords(string) 所有单词首字母大写
            maketrans(str1, str2) 将转换表中(含有 256 个项目)，第一个字符串中每一个字符用第二个字符串(等长)中对应字符替换


    copy
        deepcopy(dict1) 返回复制的一份副本

赋值
    eg:
        foo = math.sqrt
    序列解包
        eg:
            x, y, z = 1, 2, 3
        eg:
            x, y = y, x
        eg:
            >>>dict1 = {'name':'John', 'age': 42}
            >>>key, value = dict1.popitem()
            >>>key
                'john'
            >>>value
                42
    链式赋值
        x = y = 1
    增量赋值
        x += 2

转义
    \


字符串的操作
    拼接字符串 +
    创建并以合法方式表达并返回一个字符串 repr(string)


长字符串(跨行)
    eg1:
        ''' it
        do'''
    eg2:
        """it
        do"""
    eg3:
        'hello \
        world'   #通过'\'转义换行符

原始字符串
    eg:
        r'C:\nowhere'
    等价于
        'C:\\nowhere'


分类
容器
    序列
        列表
        元组
        字符串
        Unicode字符串
        buffer对象
        xrange对象
    映射
        字典
    集合


序列
    通用操作：
        索引
            eg:
                sequence[2]
        分片
            eg:
                sequence[3,6]
                sequence[3,]
                sequence[,6]
                sequence[,] #复制序列
            eg2: #设置步长
                sequence[0, 10, 1]
                sequence[10, 0, -1]
        加
            序列的拼接
        乘 
            eg:
            >>>'ok' * 3
            >>>'okokok'
            #生成一个新序列，新序列中原序列被重复n次
        迭代
        成员资格检查
            '##' in sequence #返回布尔值
        返回一个排序(以列表形式)
            sorted(sequence)
    通用函数
        len()
        max()
        min()
    列表
        空列表 sequence[]
        列表初始化 
            eg:
            sequence[None] * 10
        列表操作
            赋值
            删除元素 
                eg:
                    del sequence[2]
            分片赋值
                eg:
                    sequence[2,5] = list('ay')
        列表方法 #对象.方法(参数)
            list1.append(element) 列表末尾加入元素
            list1.count(element) 返回某元素出现个数
            list1.extend(list2) 在列表末尾接上另一个列表(修改原有列表，不像连接操作，不返回)
            list1.index(element) 返回第一个匹配项
            list1.insert(index, element) 插入
            list1.pop() 弹出最后一个元素
            list1.remove(element) 移除第一个匹配项
            list1.reverse() 将原列表反向存放列表中的元素
            list1.sort() 将原列表排列(升序？)
                list1.sort(function) 按function的比较函数进行排序
                    list1.sort() 等价于 list1.sort(cmp)
                list1.sort(key=function) 为每一个元素创建键，根据对应键进行排序
                list1.sort(reverse=True/False) 通过布尔值来指明是否要反向排序
            

    字符串(不可变)
        函数 
            list(string) #把字符串转化为列表
        字符串的格式化
            法1：
                eg1:
                    >>>print "hello, %s. I am %s." % ('world', 'Chen')
                        hello, world. I am Chen.
                eg2:
                    >>>print "hello, %s." % ['world']
                        hello, ['world']. #如果用除了元组之外的序列代替元组，序列会被解释为一个值
                eg3:
                    >>>'%.*s' % (3, 'Chen') #星号可以替代字段宽度和精度，此时数值从元组中读取
                        'Che'
                eg3:
                    >>>'%07.2f' % pi
                        '0003.14' #用0表示用0填充
                eg4:
                    >>>print ('% 5d' % 10) + '\n' + ('% 5d' % -10) #SPACE意味着在正数前加一个空格
                         10
                        -10
                eg5:
                    >>>'%+5d' % 10 #正号代表不论正负数前面都加上符号
                        '+10'
            法2:(模板字符串)
            法3：(用字典格式化字符串)
                eg:
                    >>>phonebook = {'Beth':'331','John':'445'}
                    >>>"John's number is %(John)s." % phonebook
        字符串方法
            string1.find(substring) 寻找子字符串，返回最左端索引，若无返回-1
                string1.find(substring, x, y) 确定起始和终止点
            string1.join(sequence) #被连接的序列元素必须是字符串
                eg1:
                    >>>str1 =['1','2','3','4']
                    >>>'+'.join(str1)
                        '1+2+3+4'
                eg2:
                    >>>str1 = 'usr', 'bin'
                    >>>'/'.join(str1)
                        'usr/bin'
            string1.lower() 转换成小写
            string1.title() 转换成每个单词首字母大写
            string1.replace(str1, str2) 把所有str1替换成str2
            string1.split(string) join的逆方法
                string1.split() 把所有空格、制表符、换行符当作分隔符
            string1.strip(string2) 在string1首尾中去除所有string2中含有的字符
                string1.strip() 去除字符串首尾的空格
            string1.translate(table) 根据转换表替换对应字符
                string1.translate(table, string2) 转换后并删除string1中，string2所含有的字符
    元组
        单元素元组：
            eg: (42,) #(42) 等价于 42
        函数：
            tuple(sequence) 把序列转换为元组
映射
    字典
        创建字典
            eg1:
                phonebook = {'Alice': '2341', 'Beth': '9102'}
            eg2:
                phonebook = {}
            用 dict() 建立字典
                eg1: #通过(键，值)对的序列建立字典
                    >>>d = dict([('name', 'Gumby'), ('age', 42)])
                    >>>d
                        {'age': 42, 'name': 'Gumby'}
                eg2:
                    >>>d = dict()
                    >>>d
                       {}
                通过其他映射建立字典

                通过关键字建立字典
                    >>>d = dict(name='Gumby', age=42)
                    >>>d
                       {'age':42, 'name':'Gumby'}
        基本字典操作
            len(dict1)
            dict1[n] #索引，如果键不存在却为它赋值那么新建一个键(但是列表却会报错)
            del dict1[n]
            key1 in dict1 #成员资格检查(查找的是键不是值)
        字典方法
            dict1.clear() 清除“原始”字典中所有的项(原地操作)
            dict1.copy() 返回复制的字典(这种复制不是副本)
            dict1.fromkey(SequenceOfKeys) 根据给定的键建立新的字典，并把值设为None
                dict1.fromkey(SequenceOfKeys, value) 把值设为value
            dict1.get(key) 访问字典，但是如果访问不存在的项会返回None，而不会出错
                dict1.get(key, result) 如果访问不存在的项返回 result
            dict1.item() 将字典的项按列表返回，但无固定顺序
                dict1.iteritems() 将字典的项按迭代器返回，但无固定顺序
            dict1.keys() 将字典中的键以列表形式返回
                dict1.iterkeys() 将字典中的键以迭代器形式返回
            dict1.values() 以列表形式返回字典的值
                dict1.itervalues() 以迭代器形式返回字典的值
            dict1.pop(key) 将key对应的项从字典中移除
            dict1.popitem() 弹出随机的项
            dict1.setdefault(key, result) 返回与键关联的值，若无返回result(若不设置返回None)，并更新字典
            dict1.update(item) 用一个字典项更新字典，若有相同的键会被覆盖 

语句
    条件语句
        False, None, 0, 空序列, 空字典 布尔值为 0; 其余为 1
        eg:
            if ConditionExpression:
                body
            elif:
                body
            else:
                body
    循环语句
        while 循环
            while condition:
                body
        for 循环(按次序迭代可迭代对象)
            循环遍历字典
                for key in dict1:
                    body
            eg:
                for i in range(100): #0~100 进行迭代
                    body
            并行迭代
                for a, b in zip(seq1, seq2):
                    body
            按索引迭代
                for 
            翻转和排序迭代
            列表推导式
                eg:
                    [x*x for x in range(10)]
                eg:
                    [(x,y) for x in range(3) for y in range(3)]
    pass 语句 (python中空代码块是非法的)
    del 语句 
        eg:
            >>>x = 1
            >>>del x #删掉x这个名字(对象若无其他引用也会由于垃圾收集被删除)
    exec 语句
    eval 




        
        
    


断言
    assert condition "explanation" #若条件不满足则退出程序，且打印explanation
函数
    定义
        def function(argument):
            'explanation' #用于说明函数的文档
            body
            return 
    参数
        位置参数
        关键字参数
        收集参数
            定义时，参数之前加上一个星号，把剩余参数收集到一个元组中
                加上两个星号则，返回的是字典，可以处理关键字参数
            调用时，参数加星号或双星号时收集参数的逆过程
    变量
        函数内部声明全局变量
            eg:
                global x

表达式：
    lambda


继承
    多重继承
类
    类的定义
        eg:
            class A:

                def method(self, argument):
                    body
        eg:
            class A:

                def __method(self, argument): #让方法私有化，外部无法访问
                    body
    特性
        __bases__ 知道已知类的基类
        __class__ 知道一个对象属于哪一个类

魔法方法
    __init__() 在创建类时就初始化执行该方法
    __del__() 当对象被垃圾回收时调用
