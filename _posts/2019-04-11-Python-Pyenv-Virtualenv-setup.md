---
title: Python - pyenv virtualenv setup
date: 2019-04-11
edit: 2019-04-11
status: Writing
layout: post
categories:
  - Python
tags:
  - Python
description: Python 2 和 3 如何和平共处在同一台电脑中？同一版本的 Python 如何安装不同版本的模块等等，pyenv virtualenv来帮忙
---

# 配置pyenv virtualenv 环境

本文节选自大妈的蟒营课程笔记。

安装python模块时出错，经查，现有环境是py3, 而所安装的模块用的execfile是python2的，在python3中变成了exec(), 所以需要安装Python2的环境。其实大妈任务中已指明2.7.15, 我自作主张以为py3应该可以用没问题。。。

由于电脑中已有py2和py3，已混乱，很早被提醒pyenv很好用，一直拒绝开始。

## 关于 pyenv, virtualenv, pyenv-virtualenv

先理一下三者的关系，异同。

**pyenv**是管理环境中的**Python版本**的，比如可以有Python 2.7.10, Python 2.7.15, Python 3.6等。

**virtualenv**是管理某个具体Python版本的**Packages**(包)的，比如可以有：

```pyenv 2.7.10 virtualenv1```, ```pyenv 2.7.10 virtualenv2```

- virtualenv1中：基于python2.7.10的django app需要用到django 1.6

- virtualenv2中：基于Python2.7.10的django app需要用到django 2.6

以此来隔离app开发环境。

virtualenv的创建，其实是将系统当前Python版本的解析器等复制了一份到本地app 文件夹中，再加载app所需的各种包。这样便和系统Python环境隔离开了。

但是这样有一个不足之处，如果开发其他的app也要用到类似的环境，就需要在新的app folder里面重新创建一个virtualenv，再同样加载所需的包。这样就达不到类似编程中的**复用（Reuse）**效果。

所以又有了Pyenv-virtualenv, 直接在系统环境下创建某个Python版本的多个virtual环境，各赋予一个名字。当开发各种app时:

- 如有直接可用的virtual环境，直接调用之。
- 如无现有可用的，pyenv-virtualenv 新创建一个，然后调用之。

## 使用pyenv搭建python2.7.15

官方github：[pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv#homebrew-on-macos)

pyenv全部可用命令：[pyenv/COMMANDS.md at master · pyenv/pyenv](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md) 

安装pyenv：（Mac）

```
brew install pyenv
```

查看所有pyenv命令：

```
pyenv commands
```

查看python 2.7.15是否可安装

```
pyenv install --list
```

pyenv versions 查看，2.7.15在列，OK

```
* system (set by /Users/test/.pyenv/version)
  2.7.15
```

方便起见，先将py2.7.15设为全局环境

```
pyenv global 2.7.15
```

pyenv version：显示目前环境中的确实是2.7.15

```
2.7.15 (set by /Users/test/.pyenv/version)
```

以后如需要，再单独设local环境，如：

```
pyenv local 3.6
```

至此以为一切OK了，但是在命令行里跑```python```,显示的却是系统自带的2.7.10，咋回事？

```
Python 2.7.10 (default, Aug 17 2018, 17:41:52) 
```

尝试下pyenv local，依然如此，不得其解ing。。。待尝试[pyenv/pyenv-virtualenv: a pyenv plugin to manage virtualenv (a.k.a. python-virtualenv)](https://github.com/pyenv/pyenv-virtualenv).【解决方案见下文】


## 安装pyenv-virtualenv

 [pyenv/pyenv-virtualenv: a pyenv plugin to manage virtualenv (a.k.a. python-virtualenv)](https://github.com/pyenv/pyenv-virtualenv)

为啥有了pyenv, virtualenv, 又出来个结合版？

> The main difference is that :
>
> - pyenv : copies an entire Python installation every time 
>   you create a new pyenv version. 
> - In contrast, virtualenv makes use of 
>   symbolic links to decrease the size of the virtualenv’s.
> - `pyenv-virtualenv`: adds complete virtualenv functionality to pyenv:
>
> —— [pyenv Tutorial - Guides - Resources - Amaral Lab](https://amaral.northwestern.edu/resources/guides/pyenv-tutorial)

安装pyenv-virtualenv on Mac

```
brew install pyenv-virtualenv
```

使用：

准备建一个专门用于camp的2.7.15环境，运行：

```
pyenv virtuanenv 2.7.15 camp
```

看看装完什么情况：

```
pyenv versions
```

```
pyenv: version `2.7.15/envs/camp_orphan' is not installed (set by /Users/gitlab.com.camp/orphan/.python-version)
  system
  camp
  2.7.15
  2.7.15/envs/camp
```


## 坑们

- Mac上安装 ```python 2.7.15``` 失败报错:

```
ERROR: The Python zlib extension was not compiled. Missing the zlib?
```

通过Stack Overflow 找到官方wiki [Common build problems · pyenv/pyenv Wiki](https://github.com/pyenv/pyenv/wiki/Common-build-problems)

解决：

```
brew install zlib
```

Not working. 再试，因为我的mac是 Mojave or higher (10.14+) 

> you will also [need to install the additional SDK headers](https://developer.apple.com/documentation/xcode_release_notes/xcode_10_release_notes#3035624)

```
sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
```

再重新安装2.7.15 成功。

- pyenv 环境中运行 python 显示的是系统python版本

运行：```pyenv global 2.7.15```后，```pyenv version```显示正常为2.7.15, 但是再运行 ```python```却显示为系统本地的python 2.7.10：


```
Python 2.7.10 (default, Aug 17 2018, 17:41:52) 
```

尝试下pyenv local，依然如此，不得其解ing。。。

**问题解决**：

在~/.bash_profile中添加一下几行，并保存

```
export PATH="~/.pyenv/bin:$PATH"    
eval "$(pyenv init -)"    
eval "$(pyenv virtualenv-init -)"  
```

运行python，依然是2.7.10，而不是2.7.15。而且我的folder前面依然是光秃秃的，没有出现类似(2.7.15)这种虚拟环境的标识。

想着是不是virtualenv没有成功activate呢？试着手动去activate：

```
pyenv activate 2.7.15/envs/camp
```

哈，报错了

```
Failed to activate virtualenv.

Perhaps pyenv-virtualenv has not been loaded into your shell properly.
Please restart current shell and try again.
```

再运行

```
pyenv shell 2.7.15/envs/camp
```

有点线索了，结果提示：

```
pyenv: shell integration not enabled. Run `pyenv init' for instructions.
```

运行 ```pyenv init ```后，有眉目了：

```
# Load pyenv automatically by appending
# the following to ~/.bash_profile:

eval "$(pyenv init -)"
```

原来是，我虽然在~/.bash_profile文件中加入了这一行，但这个并未生效，我还需要运行

```
source ~/.bash_profile
```

现在，看到了virtual环境的标识了，自动activate成功：

```
(2.7.15/envs/camp) 
```

现在再运行python, 便是2.7.15了。

## 待解问题（已解决）

``` pyenv install 3.7.0```后，切换到 ```pyenv local 3.7.0```, 运行 python, 显示仍然是 2.7...

### 找原因：

刚终于认真去看了[pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv#how-it-works)官方文档，其中提到了一点：

> Directories in PATH are searched **from left to right**, so a matching executable in a directory at the beginning of the list takes precedence over another one at the end

我查看了下我的 PATH，最左面竟然是 /usr/local/bin: /usr/bin，系统自带的python都在这里面了。

### 解决：

所以我的解决方案：删了这俩（因为后面还有这俩）。现在OK了。

现在再理解一下 pyenv 运行命令的顺序：PATH 是第一位的。

> So with pyenv installed, when you run, say, pip, your operating system will do the following:
Search your **PATH** for an executable file named pip
Find the **pyenv shim** named pip at the beginning of your PATH
Run the shim named pip, which in turn passes the command along to pyenv

## 参考:

- [pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv#how-it-works)
- [怎么才能放飞自我的玩儿Python · Yixuan](http://yixuan.li/geek/2018/07/31/pyenvVirtualenv/)
