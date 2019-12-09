---
title: Git - 删除分支(本地和远程)
date: 2019-12-08
edit: 2019-12-08
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  遇到问题的时候才知道原来我还不会删除分支; 原来本地和远程分支是要分别删除的.
---

# 背景

## Git 分支

[Git Branching Basics][(https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell#ch03-git-branching)

在学会删除之前, 我觉得有必要先了解一下branch的基础知识, 磨刀不误砍柴工.

Git branch 本质上就是一个指针, 指向什么呢? 

指向的是某个commit对象. 即 Branch -> a commit

而每个 commit 指向的是你的仓库文件的 snapshot, 即 commit -> snapshot of your file contents

Git 中有很多 branch, Git如何知道目前你是在哪个 branch 上工作呢? 

就又有了另一个指针 HEAD, 像下图这样.

图上显示的是很清楚, 具体在系统中是怎样的?

### HEAD

HEAD指针在系统中就是一个文件, 在你的仓库的 .git/HEAD文件, 打开是这样的:

```
ref: refs/heads/master
```

这个表明你现在是在 master 分支上.

如果这时候切换一下分支 `git checkout test```

再打开这个HEAD文件, 就会发现现在指向 test 分支了.

```
ref: refs/heads/test
```

### Branch

那前面说分支也是个指向某个commit的指针, 在系统中又是什么样子? 怎么找?

其实 HEAD 文件已经给了提示 ```ref: refs/heads/master```

文件 .git/refs/heads/master 就储存了这个指针指向的内容, 打开这个文件是这样子的:

```
eaa395c5edfa7a23a26e2fae3d006b04841bce0a
```

果然就是个 commit 对象了.

如果我们再做个切换分支, 这个文件中的commit对象就变成切换后分支的当前commit了.

现在, 设想一下, 如果我们删除了这个 ```.git/refs/heads/master ```文件, 是不是这个分支就不存在了呢?

事实上, 是的, 这便是删除本地分支的一种方法了. 


![](https://git-scm.com/book/en/v2/images/advance-testing.png)

从本地仓库的 .git 目录看, refs 下面除了 heads, 还有一个 remotes 目录, 
.git
└─HEAD
└─refs
    ├─heads                              此乃本地branches
        └─master
        └─test                           
    ├─remotes                            此乃remote branches
    │  └─origin                         
        └─HEAD
        └─master
        └─test
    └─tags


## 删除分支

### 删除本地分支

### 删除远程分支

## 思考

## ChangeLog

- 2019-12-08 init