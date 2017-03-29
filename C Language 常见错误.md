1. ​

​    当执行窗口仍在运行时，无法输入；



2. ​

```
    multiple definition of
```

​    把函数名前面加一个 `static`。



3. ​

```
    [Error] parameter '...' has just a forward declaration
```

​    声明函数时使用了 `;` 而不是 `,`



4. ​

```
    expected declaration specifiers or '...' before '*' token
```

​    `include` 头文件混乱；



5. ​

```
    Program terminated with signal SIGSEGV, Segmentation fault.(调试时报错)
```

​    非法的内存访问。

​    例如数组的越界，在循环操作时循环变量的控制问题，也有字符串拷贝时长度溢出，指针指向了非法的空间，

​    还有就是申明一个指针，但却没有对其初始化，就直接引用，或者没有开辟内存空间就释放内存，

​    所以要检查申请空间时间偶成功



6. ​

​    由于把一段代码改成注释的时候漏加了一小段进去，导致错误。



7. ​

```
    Segmentation fault
```

​    内存非法访问之类的



8. ​

```
    dereferencing pointer to incomplete type
```

​    `struct` 定义在 `#ifndef` 中



9. ​

```
undefined reference to ....
```

​	点击全部重新编译即可



10. ​

    `MakeFile` 出错

    缺乏 `main()` 

    囊括了多个 `main()` 