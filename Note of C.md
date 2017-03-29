/*这是笔记*/

1. ​

```c
while(loop_time--)
```

  等价于 

  ```c
for (i=0;i<loop_time;i++)
  ```



2. ​

​    对于以 `i` 作为index variable且为分母（如求平均数）的情况，注意讨论 `i=0` 的情况，`i=0` 时认为平均值为0



3. ​

​    输出语句后记得换行



4. ​

​    test whether a number is prime.

​    my version:

```c
int IsPrime(int n)
    {
        int i, floor_sqrtn;
        floor_sqrtn = floor(sqrt(n));
        if (n == 1) return 0;
        if (n % 2 == 0) return 0;
        for (i = 2; i <= floor_sqrtn + 1; i++) {
            if (n % i ==0) break;
        }
        if (i < floor_sqrtn + 1) return 0;
        else return 1;
    }	
```

  version of textbook

```c
 int IsPrime(int n)
    {
        int i, limit;
        if (n <= 1) return 0;
        if (n == 2) return 1;
        if (n % 2 == 0) return 0;
        limit = sqrt(n) + 1;
        for (i = 3; i <= limit; i+=2) {
            if (n % i == 0) return 0;
        }
        return 1;
    }
```



5. ​

​    factorial

```c
 int factorial(int n)
    {
        int i, f;
        if (n == 0) return 1;
        f = 1;
        for (i = 1; i <= n; i++) {
            f *= i;
        }
        return f;
    }
```



6. ​

​    每5个换一行地实现要注意 `printf("\n");` 放在哪里

​    应该放在最小地循环里。



7. ​

​    以digit依次取每一位数

```c
digit = N % 10;
    for (i = 0; i < k; i++) {                           /其中k是输入的数字的位数的上界/
        N = (N - digit) / 10;
        digit = N % 10;
    }
```

​    另法：?

```c
digit = N % 10;
    while (N / 10) {
        digit = (N / 10) % 10;
    }
```



8. ​

​    计算近似值时要求展开式最后一项小于精确度e

```c
do {
        term = expression;
        i++;
        s += term;
    } while (ABS(term) >= e);    /ABS()函数是自己定义的绝对值函数/
                                /用do-while结构而不是while就能把最后一项也加进展开式中/
```



9. ​

​    计算斐波那契数列

​    1.

```c
 long fib(int n)
        {
            int fib;
            fib = round((pow(((1 + sqrt(5)) / 2),n) - pow(((1 - sqrt(5)) / 2),n)) / sqrt(5));
            return fib;
        } 
```

​    2.

```c
long fib(int n)
        {
            int x1, x2;
            int i;
            x1 = x2 = 1;
            for (i = 1; i <= n; i++) {
                if (i % 2) {
                    x1 += x2;
                } else {
                    x2 += x1;
                }
            }
            if (n % 2 == 0) return x2;
            else return x1;
        }
```

​        

10. ​

```c
 long reverse(long number)                /求逆序数/
{
    long reverse, N;
    int digit;
    N = number;
    if (N < 0) N = - N;
    digit = N % 10;                               /求个位数/    /此处易错：将N错写成number/
    reverse = 0;
    while (N) {
        N /= 10                  /求除了个位数以外的其他数/      /*不必写成 N = (N - digit) / 10; */
        reverse = reverse * 10 + digit;
        digit = N % 10;
    }
    if (number < 0) return -reverse;
    else return reverse;
}
```

```c
long reverse(long number) /?/
    {
        int digit, newnum;
        newnum = 0;
        numcopy = number;
        if (number < 0) number = -number;
        while (number) {
            newnum *= 10;
            newnum += (number % 10);
            number /= 10;
        }
        if (newcopy < 0) newnum = -newnum;
        return newnum;
    }
```



11. ​

​    栈的实现

```c
void  push(int  n)
    {
        int  Stack[MAX_STACK];
        if (sp == MAX_STACK-1)
            return;
        Stack[++sp] = n;
    }

    int  pop(void)
    {
        int  Stack[MAX_STACK];
        if (sp == -1)
            return  NULL;
        return Stack[sp--];
    }
```



12. ​

​    在array中查找某个element的index.

```c
	int CheckElement(int a[], int element,int n)
	{
		int i;

		for (i = 0; i < n - 1; i++) {
			if (element == a[i]) break;
		}
		return i;
	}
```



13. ​

​    找出 `array` 中的最大 `element(int)`

```c
	max = a[0];
	for (i = 1; i < n; i++) {
		if (max < a[i]) max = a[i];
	}
```



14. ​

​    写 `printf` 时忘记加上 `“”`



15. ​

​    编译的时候如果已经打开了执行窗口会报错



16. ​

​    经常犯写条件的时候会把之前被赋值的变量作为条件，而不是新的变量（从而相当于没有变过）；



17.

```c
	char a;

	a = 0;
	a = '0';
```

​    两者不同。后者指数字0的 char 形式，前者就是指 '\000'或'\0'



18. ​

​    `scanf` 中 `double` 要用 `%lf` 读

​    输出时 `printf()` 中 `double` 可以用 `%f`

​    每次调用用 `sscanf` 读同一个 `string` 时，都是从头开始。

​    而用 `fgets` 之类读文件时都是顺序都下去。

​    `rewind()` 使文件内部的位置指针重新指向开头



19. ​

​    `%-2d` 如果没有 `2`，那么 `-` 没有用，所谓左右对齐是基于占位进行的

​    对于 `float` 类型的变量，`printf()` 中的说明符可以用 `%f` 或 `%lf`，而 `scanf()` 中的说明符则只能用 `%f`；

​    对于 `double` 类型的变量，`printf()` 中的说明符可以用 `%f` 或 `%lf`，而 `scanf()` 中的说明符则只能用 `%lf`；

​    对于 `long double` 类型的变量，`printf()` 中的说明符可以用 `%f` 或 `%lf`，而 `scanf()` 中的说明符则只能用 `%lf`。



20. ​

​    对于 例如

```c
        unsigned short int k = 700000;
```

​    由于 `unsigned short int` 的范围是 `0~65535`，所以会溢出输出。

​    但是如果是

```c
        unsigned short int k;
        k = 7000000;
```

​        那么输出值会是自带的值而不是赋予的溢出值。



21. ​

​    `scanf` 不会输入 `space character`， 而 `gets` 会，二者都以此为结束标志



22. ​

​    `scanf` 返回读入的数据的项数，都到末尾返回 `EOF`。



23. ​

​    优先级

​    相同优先级，一般从左至右运算。除了一元运算符、条件运算符、赋值运算符之外。

​    指针优先级最大，然后是一元运算符，再是多元运算符；

​    最后逻辑运算符



24. ​

​    如果没有超过 `8` 的数字 `\` 后面的数字默认是8进制的，对应的ASCII就是输出的字符

​    如 `\102` 是指八进制数代表十进制的 `66D`，即 `B`。



25. ​

​    作为右值（例如，赋值语句右边）时数组名可视为指针常量（系统自动转换）；作为左值，例如取地址，`sizeof`，则不能视为指针。

​    `sizeof` (一个数组)返回的是数组大小 `*` 每个元素占字节数；而 `sizeof` (一个指针）返回 `4`。



26. ​

​    C 语言标准定义的32 个关键字：

​    `auto` 声明自动变量，缺省时编译器一般默认为 `auto`

​    `int` 声明整型变量

​    `double` 声明双精度变量

​    `long` 声明长整型变量

​    `char` 声明字符型变量

​    `float` 声明浮点型变量

​    `short` 声明短整型变量

​    `signed` 声明有符号类型变量

​    `unsigned` 声明无符号类型变量

​    `struct` 声明结构体变量

​    `union` 声明联合数据类型

​    `enum` 声明枚举类型

​    `static` 声明静态变量

​    `switch` 用于开关语句

​    `case` 开关语句分支

​    `default` 开关语句中的“其他”分支

​    `break` 跳出当前循环

​    `register` 声明寄存器变量

​    `const` 声明只读变量

​    `volatile` 说明变量在程序执行中可被隐含地改变

​    `typedef` 用以给数据类型取别名(当然还有其他作用)

​    `extern` 声明变量是在其他文件正声明(也可以看做是引用变量)

​    `return` 子程序返回语句(可以带参数，也可不带参数)

​    `void` 声明函数无返回值或无参数，声明空类型指针

​    `continue` 结束当前循环，开始下一轮循环

​    `do` 循环语句的循环体

​    `while` 循环语句的循环条件

​    `if` 条件语句

​    `else` 条件语句否定分支(与 `if` 连用)

​    `for` 一种循环语句(可意会不可言传)

​    `goto` 无条件跳转语句

​    `sizeof` 计算对象所占内存空间大小



27. ​

​    转义字符后面可以跟8进制数来表示一个字符，其形式为：`\nnn`，`n` 的个数最多三位，最小一位，按最大匹配进行解释。与8进制常数不同的是，开头的0也算一位



28. ​

​    c语言编码风格

​    1. 每一个函数都要有注释，即使很短的函数

​    2. 不同的函数之间要有空行

​    3. 一个函数内，变量定义和函数执行语句之间要空行

​    4. 逻辑密切的语句之间不空行，否则空行

​    5. 复杂的函数内，循环语句、分支语句结束后要加上注释

​    6. 修改别人代码时，不要轻易删除别人的代码，善于使用注释

​    7. 缩进量用4个字符，不用 `TAB`。因为 `TAB` 与编辑器有关

​    8. 控制单行的代码长度

​    9. 长表达式要在低优先级运算符处换行，行首为该运算符

​    10. 函数的参数较长时，要换行进行划分



29. ​

​    选择排序算法(由大到小排列)

```c
		for (i = 0; i < len; i++)
			for (j = i; j < len; j++)
				if (num[j] > num[i]) num[i] = num[j];
```

​    冒泡排序算法(由大到小排列)

```c
		for (i = 0; i < len; i++)
			for (j = i; j < len; j++)
				if (num[j] < num[j+1]) exchange(num, j, j+1);
	/*可以添加一个指示器，因为在全部遍历之前就可能已经达到有序*/
```

​    插入排序算法

```c
		for (i = 1; i < len; i++)
			for (j = i-1; j >= 0; j--)
				if (num[i] > num[j]) exchange(num, i, j);
```



30. ​

​    顺序查找

```c
		for (i = 0; i < len; i++)
			if (num[i] == target) return i;
```

​    折半查找（对于有序(从大到小)的表）

```c
		while (first <= last) {
			mid = (first + last) / 2;
			if (target == mid) return  mid;
			else if (target > mid) last = mid;
			else first = mid;
		}
		return -1; /*NOT FOUND*/
```



31. ​

​    `unsigned char` 取值 `0~255`

​    `signed char` 取值 `-128~127`

​    `char`       不同编译器默认的 `char` 不一样。VC编译器、x86上的GCC都把 `char` 定义为 `signed char`，而arm-linux-gcc却把 `char` 定义为 `unsigned char`,

​    原始的ASCII标准里，定义的字符码值是只有 `0~127`，所以怎么定义的 `char` 都刚好好装得下

​    事实上，类型本身只有在解析的时候才会真正存在，在内存中，`unsigned char` 和 `signed char` 都是一串 bit 而已，所以对 `unsigned char` 的变量赋值 `-1` 的时候，会当作 `255`.



32. ​

​    默认 `int`, `double`, `float` 都是 `signed`.



33.

​    `short` 2 byte

​    `int` 4 byte

​    `long` 4 byte (win) / 8 byte (*nix)



34. ​

​    进行调试找bug时，可以用 `printf` 变量的方法进行跟踪；



35. ​

​    定义 `record` 时，内部的指针本身不用分配空间（只要为结构类型的指针分配了空间），但它指向的对象依旧要分配。在使用结构时最容易出错的是非法内存访问。

​    教材库里的 `ReadLine` 似乎不用再分配空间



36. ​

​    易忽视：把指针传入函数时，指针自身的值(地址)无法改变，要改变必须传入二级指针。



37. ​

​    如果有这个式子：

```c
char *temp;
if (temp == 'a') Process();
```

​    这样的话dev c++编译器不会报错，可能有warming...竟然无法识别 char *和 char



38. ​

    如果出现有时答案正确有时又无法运行可能是出现了这样的错误：

    ```c
    if (a > b) Function();
    ```

    其中 `a` 的值由指针指向错误的对象(未初始化的内存)，这样一来该判断的真假完全随机地取决于该内存部分地随机初始值

    ​

39. ​

    ```c
    char *line = "It's allowed."
    ```

    这种 `string` 的初始化方式是允许的。

    ​

40. 如果把函数名直接作为变量而忘记加括号，那么函数名就作为指向函数所占据内存的指针，很多时候编译器不会报错



41. ​

```c
printf("%d ", pointer);
```

这样编译器竟然不会报错