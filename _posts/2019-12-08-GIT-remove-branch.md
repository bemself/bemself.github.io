---
title: Git - 删除分支(本地和远程)
date: 2019-12-08
edit: 2019-12-12
layout: post
status: Completed
categories:
  - Python
tags:
  - Python
description:  遇到问题的时候才知道原来我还不会删除分支; 原来本地和远程分支是要分别删除的.
---

# 背景

## Git 分支

[Git Branching Basics](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell#ch03-git-branching)

在学会删除之前, 我觉得有必要先了解一下 分支（branch）的基础知识, 磨刀不误砍柴工.

Git branch 本质上是一个指针, 指向什么呢? 

指向的是某个 commit 对象. 即 Branch -> a commit

而每个 commit 指向的是你的仓库文件的 snapshot, 即 commit -> snapshot of your file contents

Git 中有很多 branch, 它如何知道目前你是在哪个 branch 上工作呢? 

就又有了另一个指针 HEAD, 像下图这样.

![](https://git-scm.com/book/en/v2/images/advance-testing.png)

图上显示的是很清楚, 具体在系统中是怎样的?

### HEAD

HEAD 指针在系统中就是一个文件, 你的仓库的 .git/HEAD 文件, 打开是这样的:

```
ref: refs/heads/master
```

这个表明你现在是在 master 分支上.

如果这时候切换一下分支 `git checkout test`

再打开这个HEAD文件, 就会发现现在指向 test 分支了.

```
ref: refs/heads/test
```

### Branch

那前面说分支是个指向某个 commit 的指针, 在系统中又是什么样子? 怎么找?

其实 HEAD 文件已经给了提示 ```ref: refs/heads/master```

文件 `.git/refs/heads/master` 就储存了这个指针指向的内容, 打开这个文件是这样子的:

```
eaa395c5edfa7a23a26e2fae3d006b04841bce0a
```

果然就是个 commit 对象了.

如果我们再做个切换分支, 这个文件中的 commit 对象就变成切换后分支的当前 commit 了.

现在, 设想一下, 如果我们删除了这个 `.git/refs/heads/<branch_name> `文件, 是不是这个分支就不存在了呢?

事实上, 是的, 这便是删除本地分支的一种方法了. 


从本地仓库的 .git 目录看, refs 下面除了 heads, 还有一个 remotes 目录, 

```
.git
└─HEAD
└─refs
    ├─heads                              本地 branches
        └─master
        └─test                           
    ├─remotes                             remote branches
    │  └─origin                         
        └─HEAD
        └─master
        └─test
    └─tags
```

对照一下 `git remote -v` 的运行结果，就更一目了然了。

## 删除分支
实际删除分支就简单了。

### 删除本地分支

两种方法：

- 用 Git 命令： 

假设我们创建了一个分支，
```
git checkout <branch_name>
```
本地做了些更改后提交，并 push 到远程仓库：

```
git add .
git ci -m "init new branch"
git pu origin <branch_name>
```

如果要删除这个本地（比如已将更改 merge 到 master 了，本分支可以弃用了），运行下面命令即可：

```
git br -d <branch_name>   
git br -D <branch_name>   // 强制删除
```

虽然没看到 git 上述删除命令的源代码，我猜其实它可能也是做了下面这个直接删除文件的事儿~

- 直接删除文件：

前面提到过了，直接删除这个文件即可： ```.git/refs/heads/<branch_name>```

同样，如果你想删除比如 `remotes/origin/<branch_name>` 也没人拦你，不过删的还是你本地的，远程的分支依然在。

### 删除远程分支

要真正删除远程分支， 还得用到 git push。命令很简单：

```
git push <remote_name> --delete <branch_name>
```

其实还有个命令，也做这个事，但是那个命令乖乖的有点绕，做之前得费点脑子想明白，不如上面这个清晰安全，所以就弃用了这里。

## 思考

- 理解基本概念还是很重要，比如这里就有几个地方得先搞清楚
  - 分支 就是个指针，在本地的话对应就是个文件，里面存了一个路径，指向另一个以分支名命名的文件
  - Git 分支有本地和远程两种，它们名字相同，但领地不同，删除一个并不影响另一个
- 实操，实操，实操

## ChangeLog
- 2019-12-12 .5h
- 2019-12-08 init