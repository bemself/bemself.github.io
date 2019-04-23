---
title: Python - 文本文件中如何插入内容
date: 2019-04-23
edit: 2019-04-23
status: Writing
layout: post
categories:
  - Python
tags:
  - Python
description:  对文本文件进行读写追加很简单, 但插入或替换内容就不方便了, 本文探讨了几种方法.
---

# Python: 在文本文件中插入内容

文本文件的操作用的比较多的, 读\写\追加, 通常都是在末尾追加.

如何在我们需要的某一处**插入**新的内容呢? 

这个需求最早是在怼周刊的自动化时遇到, 当时的需求是:

- 将 .txt 文件的内容读出来
- 然后插入到 .md 文件中的 Progress 部分

当时用了 [fileinput — Iterate over lines from multiple input streams](https://docs.python.org/2/library/fileinput.html) 模块, 使用还算方便, 因为只有一处需要替换.

后来又在蟒营的 PoW 蟒通证的工具中, 遇到类似需求:

- 将收集来的数据分别插入 .md 文件的各个指定位置

本想继续用 fileinput, 试了一下, 发现不方便了, 因为 fileinput 需要指定原文件中的placeholder文本, 一旦这个文本内容变化了, 而且非常可能变化, 就需要调整脚本.

想到大妈有批量生成过学员邮件内容, 便想看一下高手是咋处理的, 然后果然思路不一样, 便有了此文.

## Python自带: fileinput

> [fileinput — Iterate over lines from multiple input streams](https://docs.python.org/2/library/fileinput.html)

这个和[open()](https://docs.python.org/2/library/functions.html#open)有什么区别?

- open(): 常规的文件读写追加
- fileinput: 可以逐行 loop 文件, 显然, 如果我们想在某处插入点新内容, 当扫描到那行时, 便可以操作了.
	- 比如, 可以将每一行缩进几个空格
	- 删除某行,
	- 修改某行的内容
	-....

看一个简单的例子: 将每行都加入列表符

原文件内容:

```
Monday
Tuesday
Friday
```

代码:
```
def process(line):
    print( "- " + line)

for line in fileinput.input(files=filename, inplace=True):
    process(line)
```

运行后文件内容便是这样了:
```
- Monday
- Tuesday
- Friday
```

具体用法请参考官网链接[fileinput](https://docs.python.org/2/library/fileinput.html), 注意这个 inplace=True 参数, 如果要内容改动生效的话.

现在我们来看, 如何在指定位置插入内容.

假如我们想在这个文件:

```
Time log:
> Insert time log for this week below:

Actions:
- Getup and run
```

中的 Time Log 下面插入以下实际运行的数据:

```
Reading 1h
Writing 1.5h
```

用 fileinput 可以这样来:

```
placeholder = "> Insert time log for this week below"

with fileinput.input(files=filename, inplace=True) as f:
    for line in f:
        print(line, end='')      <------------
		if line.startswith(placeholder):
			print(txt2insert, end='\n')
```

需要注意的是 这行 ```print(line, end='')```可不能漏了, 不然文件中的逐行扫过去的内容, 如果不符合条件的, 就被清空了.


## string formatting

> [Built-in Types — Python 2.7.16 documentation](https://docs.python.org/2/library/stdtypes.html#string-formatting)

在介绍大妈的方法之前, 先回顾一下 python 中的 "str".format 方法:

占位符 ```{}```中的值在运行时会替换为 format 方法中的变量值 (username)
```
str = "Hello {}".format(username)
```

这样, 我们可以动态的传入任意 username.

例子中的字符串很短, 想象一下, 如果:

- 要动态传入多个变量呢?

自然可以这样:

```
str = "Hello {}, today is {}".format(username, week)
```

想一下, 如果占位符很多的情况, 比如这样:

```
str = "Hello {}, today is {}, it is {} now, it's time to {}".format(username, week, datetime, study)
```

是不是看的眼花了, 读起来不甚友好, python 有个解决方法:

- 我们可以将所有变量放到一个字典中
- 在占位符中显性给个名字

即: (为了缩短篇幅, 咱以两个变量为例)

```
name = "sir"
week = "Monday"
data = {"name": name, "week":week}
print(data)
str = "Hello {name}, today is {week}".format(**data)
```
这样舒服了.

继续, 如果是个更长\更多动态变量的情况呢? 再假设这个字串可能会被重复使用呢?

这么长且常用的字串一般如何存储? 通常是会放到文件中吧.

这样想来, 我们便离大妈的方法近了.

## 模板

现在介绍大妈的方法, 没错, 就是标题上写的模板.

- 将要进行替换处理的原字符串放到一个模板文件中, 比如命名为 blah_tpl.md
- 在模板文件中, 将要处理的字串中的各个位置, 用占位符{git-it-a-name}

然后:
	- 读取模板文件内容
	- 用 ```文件内容.format(**_dict)```

具体就不展开了, 上面的string formatting部分已经介绍过了, 更多细节详见官网.

## Web 模板

还没结束, 有没有觉得上面的模板方法很眼熟?

学 python 框架的时候, 前端的渲染咱们都接触过 [Jinja2 (The Python Template Engine)](http://jinja.pocoo.org/)

```
{ ex-tends "layout.html" }
{ block body }
  <ul>
  {% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
  {% endfor %}
  </ul>
{ endblock }
```

上面这段便是 Jinja 的模板文件样例, 其中的```{{ user.username }}```虽然长得不太一样, 但是很相像不是? 
虽然没看过 Jinja 源码, 不知道其背后的实现逻辑(比如是否也是用的 "str".format?), 但其设计思想想来是相通的.

Note: 原谅我把 jinja 模板中的 % 都去掉了, 因为上传此文到 我的jekyll blog时, 总是 build 失败 ```unknown tag extends```
, 原因是上面引用的 jinja 模板中用到了 ```% extends```, 被 jekyll 当做自己的关键词了...看来模板也有局限性的, 如何 在模板中 escape 这种关键词呢??

## 启示

学习还是得融会贯通~~

## 参考

- [fileinput — Iterate over lines from multiple input streams](https://docs.python.org/2/library/fileinput.html)
- [Built-in Types — Python 2.7.16 documentation](https://docs.python.org/2/library/stdtypes.html#string-formatting)
- [Jinja2 (The Python Template Engine)](http://jinja.pocoo.org/)

## ChangeLog

- 2019-04-23 init 2h