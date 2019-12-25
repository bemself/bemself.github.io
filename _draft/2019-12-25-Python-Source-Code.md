---
title: Python - 如何看 Python 模块源码和帮助
date: 2019-12-22
edit: 2019-12-22
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  确切的说是去哪里看~ 因为我还看不懂 Python 源码，只是有想看的愿望，以及偶尔有那么点需求
---

# 背景

Python 随便找个编辑器就能写，方便；代价就是非 IDE 的那种编辑器，看源码找 module 等就不方便；

虽然看不懂源码，但还是抑制不住（想高手学习般）的浏览一下，就想找找去哪儿看源码

## Github

既然开源，自然首先是[github- python](https://github.com/python/cpython)

但是上去看了一圈，目录结构看不懂，找到官方说明 [CPython Source Code Layout](https://devguide.python.org/exploring/)，：

我们常用的 builtin 模块（用 py）写的部分基本在`Lib`目录下。另外测试代码都是 py 文件，如果看不懂 c 代码， 可以考虑直接看 test.py

```
For Python modules, the typical layout is:

    Lib/<module>.py
    Modules/_<module>.c (if there’s also a C accelerator module)
    Lib/test/test_<module>.py
    Doc/library/<module>.rst
```

## [py inspect module - retrieving source code](https://docs.python.org/2/library/inspect.html#retrieving-source-code)

看帮助：

```
>>> import inspect
>>> inspect.getdoc(sorted)
'Return a new list containing all items from the iterable in ascending order.\n\nA custom key function can be supplied to customize the sort order, and the\nreverse flag can be set to request the result in descending order.'
```
但是看源码：
```
>>> sorted
<built-in function sorted>
>>> inspect.getsource(sorted)
TypeError: module, class, method, function, traceback, frame, or code object was expected, got builtin_function_or_method
```

因为 sorted 是 builtin functions ，是用 c 语言写的，所以这个办法看不了。

不过我目前有个疑惑， `Lib\os.py` 明明是 py 代码，用 `inspect`也看不了，不知道是我没用对还是啥，待解，求解。

## help() 方法

```
>>> help(sorted)
Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
```

## 参考

- [ why are there separate tuple and list data types](https://docs.python.org/3/faq/design.html#why-are-there-separate-tuple-and-list-data-types)

## ChangeLog
- 2019-12-22 init