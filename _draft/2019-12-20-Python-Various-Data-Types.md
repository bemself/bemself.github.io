---
title: Python - 各种数据类型及应用场景
date: 2019-12-20
edit: 2019-12-20
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  Python 各种数据类型，都怎么用，什么时候用？
---

# 背景

## Summary

- [sorted(dtype)](https://docs.python.org/3/library/functions.html#sorted) 返回一个排序好的 dtype 同类型
- [list.sort()](https://docs.python.org/3/library/stdtypes.html#list.sort) **不返回** 一个新的 list 
  - 而是将 list 列表本身排序

## List

- [Why doesn't list.sort() return the sorted list?](https://docs.python.org/3/faq/design.html#why-doesn-t-list-sort-return-the-sorted-list)

原因就是：返回一个新的 list 成本大啊啊，浪费

## ChangeLog
- 2019-12-17 init