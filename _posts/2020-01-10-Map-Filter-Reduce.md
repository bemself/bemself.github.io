---
title: Map, Filter, Reduce
date: 2020-01-10
edit: 2020-01-22
layout: post
status: Writing
categories:
  - Python, Java, Lisp
tags:
  - Python, Java, Lisp
description:  最早知道 MapReduce 是赶时髦学大数据，后来陆续在各种语言中接触 map, reduce, filter， 一直没有什么感觉， 直到最近才联系起来，原来都一样~
---

# 背景

有没有发现发现，很多语言中都有 map, reduce, filter 等命名的方法，看似在不同的语言中，但实际多数都有相同的含义，用于相似的场景。

王垠在[如何掌握所有的程序语言](http://www.yinwang.org/blog-cn/2017/07/06/master-pl)中反复强调“语言特性，语言特性，语言特性”，很是赞同，在一种语言中了解了某个特性，迁移到其他语言便很容易。

# MapReduce in 大数据

最早是赶时髦参加公司大数据培训，知道了 MapReduce。

因为数据量大，所以：

- 有个分散处理的需求，
  -  Map 为之实现。
- 分散之后还得再合并，得到终结果
  - Reduce 为之实现

为啥取名 Map，一直觉得不好理解。

Map 本身是映射的意思，key-value pair 这个好理解，在 MapReduce 里面的 k-v pair怎么理解呢？

细想可能这样比较好记一点：

假设你一下子有了一大大大...堆钱，里面各种百元十元五十元钞。你想知道一共都有多少钱，或者有多少百元钞吧，你一个人可能要数好多天啊，关键你也没那么多时间去数。。。

怎么办？

自然是雇人，将这大大堆钱分成很多很多份，每人一份，分别数。----- 这就是 Map 要做的一些工作

这里的映射主要在：

- 人 <-> 分摊给他的那堆钱

对于每一对映射，都要做相同的事情：

- 数钱，百元的，十元的，五十元的等等，分别分开数，各自求总和

最后，等大家都数完了，再每个人报上各自的总数来，再求和，------- 这便是 Reduce 的工作了。

当然，实际情况要复杂复杂的多了。这个例子帮助了解个大致的原理。

# Java Map, Filter, Reduce

Java 8 引进了 [Stream (Java Platform SE 8 )](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html)， 

```
List<Student> students = new ArrayList<>();
...add some students in it
int sum = students.stream()
          .mapToInt(p -> p.getAge())
          .filter(p -> p.getAge() >= 10)
          .average();
  ```

很清爽的结构：

- map:  List<Person> => List<Integer>
- filter: 
- reduce: List<Integer> => int

# Python
[Built-in Functions — Python 3.7.6 documentation](https://docs.python.org/3.7/library/functions.html#map)
> 
map(function, iterable, ...)

    Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().

# Lisp

据说，前面的这些设计是借鉴了 Lisp，赶紧（假装我会过）去重温了一下lisp.

翻了以前的笔记，果然找到了，如果不是记录过，我都不记得之前我也猜到 lisp 是源头~,感谢笔记~

> 知道这个 `map/reduce` 特性始自大数据, java 中的 `stream` 也有了这个功能, 现在在 `clojure` 里面看到, 似乎这里(`lisp`)才是功能源头? 功能确实很爽, 省却了 n 多行代码.

- `map`: 对集合中的每一个元素做操作
- `filter`: 筛选集合中符合条件的元素
- `reduce`: 整合筛选后的元素, 如求和等

想单独拎出来的是下面这个:

```
user=> (reduce conj [2] '(3 2 1))
[2 3 2 1]
user=> (reduce conj '(3 2 1) [2])
(2 3 2 1)

user=> (conj [2] '(3 2 1))
[2 (3 2 1)]
user=> (conj [2] [1 2 3])         
[2 [1 2 3]]

user=> (conj 2 [1 2 3]) 
Execution error (ClassCastException) at user/eval209 (REPL:1).
java.lang.Long cannot be cast to clojure.lang.IPersistentCollection
```

 除了求和这种 `reduce`, 这里能看出来 `reduce+conj` 还可以将 `List` 和 `Vector` 缩成 一个 `Vector` 或 `List`. 这和单独用 `conj` 的区别便很明显了, 后者是扩展 `Vector` 或 `List`.

 至于这些设计的背后 可能隐藏什么 待探索

# Reference

- [MapReduce](https://en.wikipedia.org/wiki/MapReduce)
 
# Changelog
- 2020-01-22 update with lisp
- 2020-01-10 init