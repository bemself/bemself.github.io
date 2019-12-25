---
title: Python - Sort 各种可能
date: 2019-12-20
edit: 2019-12-20
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

- [sorted(dtype)](https://docs.python.org/3/library/functions.html#sorted) 
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