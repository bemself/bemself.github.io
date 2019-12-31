---
title: Python - 装饰器 Decorator
date: 2019-12-22
edit: 2019-12-22
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  经常感觉自己看懂了，实际再遇到 Decorator 就还是懵，干脆自己写一遍，教教自己，分享他人
---

# 从概念解析入手总没错

命名是一门艺术，理解一个事物，先从它的名字入手总没错，除非”名不符实“。

Decorator，装饰器，顾名思义，装饰一个器物。

- 装饰：意味着会有所改动，比如给涂个漆，画上画，
- 器物：可以是桌子，椅子，墙，

当然，在 Python 中，这个器物自然不是实物，那会是什么呢？

首先想，Python 中有什么？
- 各种数据类型
- 函数
- 类，对象
- 各种表达式
- ...

那会是其中的什么？想来都有可能吧？？？？（先存疑）

不过，以我有限的经验，我可以肯定的是，**函数**确定是的。

所以就先以函数为例。那**装饰函数**意味着什么？

便是：可以对函数进行修改。

但是，具体怎么改？改什么？函数不是定义好了后，就不太好改了吗？

# 装饰函数 - 怎么改，改什么

先来想一想，函数一经定义后，什么情况下需要修改？

# 引申

AOP

http://en.wikipedia.org/wiki/Decorator_pattern

# 参考

- [ Python Decorator](https://wiki.python.org/moin/PythonDecorators#What_is_a_Decorator)
- [Primer-on-python-decorators](https://realpython.com/primer-on-python-decorators/)

## ChangeLog
- 2019-12-22 init