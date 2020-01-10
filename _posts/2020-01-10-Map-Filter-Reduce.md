---
title: Map, Filter, Reduce
date: 2020-01-10
edit: 2020-01-10
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

# Lisp

据说，前面的这些设计是借鉴了 Lisp，赶紧（假装我会过）去重温了一下lisp，

# Reference

- [MapReduce](https://en.wikipedia.org/wiki/MapReduce)
 
# Changelog
- 2020-01-10 init