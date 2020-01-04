---
title: Python 线性回归（Linear Regression) - 到底什么是 regression？
date: 2020-01-03
edit: 2020-01-03
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  了解线性回归前，先看看 Regression 的由来
---

# 背景

学习 [Linear Regression in Python – Real Python](https://realpython.com/linear-regression-in-python/)，对 regression 一词比较疑惑.

这个 linear Regression 中的 Regression 是什么意思，字面上 Regression 是衰退的意思，线性衰退？相信理解了这个词，对线性回归可能印象深刻些。

# Regression 到底是什么意思

搜了一番，原来是为了纪念生物统计学家高尔顿的发现，他是达尔文的表兄，一直想从进化论来研究为何人各有不同。

他的一个重大发现是，父母的身高与子女的身高之间有某种关系。

平时生活中我们也经常纳闷，为啥有的父母个子都很高，子女却比较矮，相反，有的父母都很矮，孩子却很高。高尔顿的解释是，子代的平均身高向中心回归了。正是这种子代身高向同龄人平均身高回归的趋势，使得人类身高没有两极分化。

所以他用“回归”这个词来描述父辈身高 y 和子代身高 x 之间的关系。

还有一个有趣的解释，是从词源来解，regression 中：
-  "re" ：向后，往回，相反，相对
-  gress = walk， 走
-  ion ：表名词：行动，状态等

[回归分析中的“回归”是什么意思？ - 我是观察员的回答 - 知乎](https://www.zhihu.com/question/30123729/answer/205476) 这个答案用炒菜来比喻，很有意思：

> 炒菜的体验。假设你炒西红柿鸡蛋，要放盐等调料才觉得好吃，你放了一小撮，不够，再加点，结果多了；那就加点水，味道淡了。你感觉有点太淡了，那就再加点盐，直到你炒好了菜，你加盐的过程才结束。 对你来说是美味吧？这就是回归的感觉。

意思就是，不断的调整影响菜的口味的各种调料（盐，水，等）,直至找到一个均衡的比例。这个调整的过程中有不断的“回退”。

至此终于理解 regression 的含义了。不过，统计学上的 y 与 x 之间的关系并不总是“回归”的含义。

# 统计学上的 regression
> 研究变量之间的关系

变量是指什么？关系是指什么样的关系？

先拿一个具体的线性回归的例子来说：

> 你想知道，为啥同是 dev，某同事 A 比你年轻，工资却比你高？
> 换句话说，影响你们工资的因素有哪些？
> 你想了想，A 虽然年轻，但比你来公司早一点，学历比你高，会说话（可能刚来的时候谈的工资就高？），等等。

对应上面的问题，这个例子中，

- 变量是什么？ 
  
  工资(y)

- 关系是指什么样的关系？

  工资和年龄(x1)、工龄(x2)、学历(x3)、性格(x4)等因素之间有什么样的关系

用统计学来表达，就是要找寻一个函-=数 y = f(x), where x: x1....xn.

这里，y (工资) 是因变量，x1...xn(影响 y 的因素) 是自变量。

再举一个例子：

> 某领导要求下属去考察某市的房地产状况
> 房价(y)是他要做的考察之一
> 他要研究哪些因素(x1...xn)影响着该市的房价走向

还有很多其他例子。

重点在于：线性回归研究这两点：

- x1...xn 是否有影响 y
- 如影响，则在多大程度上影响 y


# Reference

- [Linear Regression in Python – Real Python](https://realpython.com/linear-regression-in-python/)
- [为何会有统计学上的回归现象的出现？](https://www.zhihu.com/question/20483629)
- [回归分析中的回归是什么意思](https://www.zhihu.com/question/30123729?sort=created)
- 书：应用回归分析

# Changelog
- 2020-01-03 init