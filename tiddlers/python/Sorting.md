---
title: Python - Sort 各种可能
date: 2019-12-25
edit: 2019-12-25
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  Python 各种数据类型，都怎么排序的？
---

# 背景

## Summary

- [sorted(a datatype)](https://docs.python.org/3/library/functions.html#sorted) 
  - 返回一个排序好的 dtype 同类型
  - iterable 的数据类型都适用
  
- [list.sort()](https://docs.python.org/3/library/stdtypes.html#list.sort) 
  - **不返回** 一个新的 list 
    - 即，原地 sort 列表本身
  - 只有 list 有这个方法

## List.sort()

- [Why doesn't list.sort() return the sorted list?](https://docs.python.org/3/faq/design.html#why-doesn-t-list-sort-return-the-sorted-list)

原因就是：返回一个新的 list 成本大，浪费

## sorted()

sorted 有两个重要参数：

- reverse: 这个很好理解，不提了。
- key: 重点说这个，因为我绕进去过。

### key 参数

本意就是：我要按照这个 key 来排序，这个 key 由你定义，比如：
- 如果有一组数，你可能想从小到大排
- 如果是一组字符串，你可能想按字母顺序排
- 如果是一组对象，比如一群学生，你可能想按年龄排，或者身高排，等等 你说了算

对应到程序里，这个 key 怎么来表达？先记着：这个 key 的值是个 `function`。

**先看简单的情况: 不传 key 值**：，就是默认按 `<` 来排需，即从小到大，从 a 到 z 排序。

以 `alist = [1, 3, 2]` 为例，
```
>>> alist = [1,3,2]
>>> sorted(alist)
[1, 2, 3]
```

**现在看传入 key 值（function）- 简单的函数**: 

```
>>> alist = "This is a test".split()
>>> sorted(alist, key=str.lower)
['a', 'is', 'test', 'This']
```

上面这个例子中， key的值是 str.lower 函数。

```
>>> str.lower
<method 'lower' of 'str' objects
>>>> str.lower('This')
'this'
```

当在 sorted 里面用于排序的时候，这个 key 是怎么用的？

```
alist = ["this", "is", "a", "test"]
key = str.lower
```

大致是这样的顺序：

- 新建一个list, 如称之为 sorted_list
- 对于 alist 里面的每一个元素，分别将其作为参数传入 str.lower() 函数中，
- 得到的新值添加到 sorted_list 中
- 返回这个 sorted_list


**继续看传入 key 值（function）- Tuple**: 

**继续看传入 key 值（function）- 复杂列表**: 

**继续看传入 key 值（function）- 字典**: 

**继续看传入 key 值（function）- 嵌套字典**: 

## Issues

终于能看懂点这种报错了：

> TypeError: '<' not supported between instances of 'dict' and 'dict'

因为设计中明确写了：

>  sort(*, key=None, reverse=False)

    This method sorts the list in place, using only < comparisons between items.

## 要注意的点

- list.sort()：
  - 如果中间比较的时候出错，很可能这个列表已经是半排序过了~
  - 如果排序过程中，列表又有改动（比如别人插入了新记录），也可能导致列表乱掉~

## ChangeLog
- 2019-12-25 init