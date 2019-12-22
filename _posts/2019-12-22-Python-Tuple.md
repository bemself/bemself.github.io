---
title: Python - Tuple 怎么用，为什么有 tuple 这种设计？
date: 2019-12-22
edit: 2019-12-22
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  Python tuple 什么时候用？
---

# 背景

看到有同学很执着的用 `tuple`，想起自己刚学 `python` 时，也是很喜欢 `tuple`，为啥？因为以前从来没见过这种样子的数据 `(1,2)`, 感觉很特别，用起来也挺好用 `i,j=(1,2)`, 一下子就得到两个变量了； 

而且如果函数返回值超过 1 个的话， 用 `tuple` 挺好，直接就返回了，解析起来也方便。

但 `tuple` 为啥这么好？是真的这么好吗？真的这么好，为啥比如 `json` 什么的很少用 `tuple` 呢？没有细想过。

## 探索

所以就挺想搞明白，为啥设计了 `tuple`，应该怎么用？

去官网查，找到[ why are there separate tuple and list data types](https://docs.python.org/3/faq/design.html#why-are-there-separate-tuple-and-list-data-types)，有点感觉了。

大致写一下理解：

`tuple` 和 `list` 很相似，但基本的用处还是不一样的。

`tuple` 的设计类似于 Pascal records 或 C structs（这两个都不熟悉。。。）；

它是啥？
- 一组相关联的数据的集合
  - 集合规模 小
- 这些数据可以是不同类型
  - 但合起来是一个组合

一个比较典型的应用是，笛卡尔坐标系，`(x,y,z)` 表示一个物体的坐标。看起来是挺直观的，比 `list`,`dict`都直观。

还有一点， `tuple` 是 `immutable` 类型，就是说，一旦定义了 `tuple`, 它里面的数据就不能更改了。比如:

```
>>> a = (1,2)
>>> a[0]=3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> a[0]
1
```

我定义了一个 `tuple` a, 我想更改它的第一个值，但是报错了 `'tuple' object does not support item assignment`, 这个错其实就是提示了， `a` 里面的值是不能更改了。

如果你想更改，那不如改为定义一个 `list`, 这个 `list` 就是 `mutable`的，即可以任意更改里面的值，这个大家基本都熟悉常用的了。

## 小结

`tuple` 用起来比较爽的地方有几个，依我自己的感觉：

-  组合(group)的感觉比较好，正如其设计的，`tuple` 就是将几个相关的组合起来代表某个事/物
   -  我的理解是，这个组合起来的事物，是有某个具体有意义的事物，比如笛卡尔坐标系
-  解析的时候比较方便，比如如下，一行代码就可以获得两个变量了

```
>>> i , j = (1, 2)
>>> i
1
>>> j
2
```
- 同样，设计一个函数，需要返回多个变量的时候，可以用 `list`, 但也可以用 `tuple`, 解析的时候就有了上面那条的便利。
- 补充一点，因为 `tuple` 是 `immutable` 的，所以可以当做 字典（dict）的 `key` 来用，因为 字典的 `key` 是用到 `hashtable` 实现的， 是不能（该）变动的。
- 还有啥？暂时没想到

那不太建议用 `tuple` 的地方感觉就比较重要了：

- `tuple` 定义后，里面的值是不能改的，这个就很不方便了
- 如果 `tuple` 里面的元素之间没有什么关联的话，用起来也缺失了实际设计的本质

## 参考

- [ why are there separate tuple and list data types](https://docs.python.org/3/faq/design.html#why-are-there-separate-tuple-and-list-data-types)
- [why must dictionary keys be immutable?](https://docs.python.org/3/faq/design.html#id21)

## ChangeLog
- 2019-12-22 init