---
title: Git - 从历史中真正删除文件
date: 2020-01-10
edit: 2020-01-10
layout: post
status: Completed
categories:
  -  Git
tags:
  - Git
description:   也算是历史遗留问题了，今天终于似乎搞定了，记录一下~
---

# 背景

Git 操作时，经常“不小心”上传一些不必要的（大）文件，或者私密数据，等等。

当然可以从本地把这些文件删除，加入 `.gitignore`, 避免下次再上传。

然而，之前已经上传过的，还遗留在 git 历史中，“有心人”还是会能挖掘到你的私密数据。。。

# 分析

[Git - git-filter-branch](https://git-scm.com/docs/git-filter-branch) 可以从历史中删除文件，但据说“挺危险的”，于是前车之鉴我也没敢试试。

从大妈那儿拿到建议用 [BFG Repo-Cleaner by rtyley](https://rtyley.github.io/bfg-repo-cleaner/#download)，值得一试，这个大概是终极工具了。

# BFG 删除历史文件

网站的帮助还算清楚，直接上操作：

- 环境：Java8+

- `git clone --mirror your-repo.git`

- `cd your-repo.git`

- [下载bfg.jar](http://repo1.maven.org/maven2/com/madgag/bfg/1.12.16/bfg-1.12.16.jar)，我为了省事，直接将其复制到 `your-repo.git` 目录下了（不建议参考哈）

- `java -jar bfg-1.12.16.jar --delete-files test1.py`

如果是要删文件夹：

`--delete-folders "{folderA,folderB,folderC}"` 这个就好了

- `git reflog expire --expire=now --all && git gc --prune=now --aggressive`

- `git push`

再去看历史，那个文件`test1.py`不见了~done.

- 最好把本地旧的 repo 删除了，不然可能又不小心 mess up 了
- 通知其他仓库使用者重新 clone 吧，他们本地的旧的也好删除了。

> 清理后, 
全新 clone , 检验,
然后, 增补 gitnigore 配置, 防止再次...
如果有必要, 可以将数据目录移到工程目录之外,
增补 ENV 声明来指向

要注意的是：

- BFG 默认不会 touch最新的commit，即如果你要删除的文件在最新的 commit 中，则不会删除之。为什么？因为最新的 commit 很可能是已上线在 production 的，所以~
- BFG 用的是仓库镜像，具体是什么，见下文。
- 如果要删除的文件在受保护的`commit`中，BFG 不会删，不建议删。至于`commit`什么情况下会受保护，我还不太清楚。
  

#  Git 仓库镜像

值得注意的是，BFG 用的是仓库镜像 `git clone --mirror` ， 它和普通的`git clone`有什么区别？

[git-clone doc](https://git-scm.com/docs/git-clone#git-clone---mirror):

> `--mirror`

    Set up a mirror of the source repository. This implies --bare. Compared to --bare, --mirror not only maps local branches of the source to local branches of the target, it maps all refs (including remote-tracking branches, notes etc.) and sets up a refspec configuration such that all these refs are overwritten by a git remote update in the target repository.

我没看懂，对“refs"还是挺迷惑，模糊感觉， `--mirror` 类似深拷贝, 复制一切~， 具体理解还得和另外两种 `git clone`的方式结合起来：

- `git clone your-repo.git`
- `git clone --bare your-repo.git`: 这个貌似最浅层次的 copy 了(bare嘛)

[What's the difference between git clone --mirror and git clone --bare - Stack Overflow](https://stackoverflow.com/questions/3959924/whats-the-difference-between-git-clone-mirror-and-git-clone-bare) 这里面有详细的讲解, 摘一段如下：

> git clone --mirror origin-url: Every last one of those refs will be copied as-is. You'll get all the tags, local branches master (HEAD), next, pu, and maint, remote branches devA/master and devB/master, other refs refs/foo/bar and refs/foo/baz. Everything is exactly as it was in the cloned remote. Remote tracking is set up so that if you run git remote update all refs will be overwritten from origin, as if you'd just deleted the mirror and recloned it. As the docs originally said, it's a mirror. It's supposed to be a functionally identical copy, interchangeable with the original.

# BFG 的原理

可能也是因为 `--mirror` 是深拷贝，复制一切，所以也便于更新修改了~

本来以为 BFG 也用了 `git-filter-branch`，查了一下源码，没找到类似的 git 命令，看到的是这样：

```
clean(commits)
updateRefsWithCleanedIds()
objectIdCleaner.stats()
objectIdCleaner.cleanedObjectMap()
```

后来去官网再仔细看，发现有一段和`git-filter-branch`的性能比较：

- `git-filter-branch` 循环每一个 commit， 在每个 commit 中 walk 整个文件目录结构，慢而且浪费
- BFG：用 git 下面这个特性，只具体处理要删除的文件或文件夹
  
  > every file and folder is represented precisely once (and given a unique SHA-1 hash-id)

  不知道是否可以这么理解，用过 `git log --oneline <文件名>` 都知道，这个命令会显示文件的各个 commit 历史。BFG 大概用的这种每个文件在每次 commit 中都有一个 `sha`，找到这个文件所有的 `commit sha`, 然后再分别处理之似乎就可以了，不必考虑 commit 的文件目录循环了。

# 问题

我现在用的还不多，等遇到了继续补充。

## 问题 1： 还是有文件没删除，在某些 commits 中依然能看到

这个问题有两方面：

- 经大妈指正，我混淆了 commit 本身数据 和 版本中的文件数据

我查看的是`https://gitlab.com/<repo>/commit/187e9d07`。

而实际应是 `https://gitlab.com/<repo>/tree/187e9d07/...`, 这里才是对应版本树的文件。

- 有些删除在运行 `bfg` 命令后，我没有及时做 `git reflog expire --expire=now --all && git gc --prune=now --aggressive`

这就等于在数据库中插入数据后没有做 commit 一样，如大妈所言：

> 对 git 仓库进行调整后~
得刷入数据才生效啊~
将git 视为数据库的话~

## 问题 2： BFG 之前忘了先清理仓库，删除想删的文件了

这个就有点傻了，我忘记了先把仓库里面想删的文件先物理上删除，结果先跑了 BFG~ 导致后面又跑了几遍~

# 附录

想贴出来这个，就因为挺好笑的~自己找, BFG repo 好多 commits message 也是 Trump~

```
Using repo : your-repo.git

Found 16 objects to protect
Found 26 commit-pointing refs : HEAD, refs/heads/test1, refs/heads/test2, ...

Protected commits
-----------------

These are your protected commits, and so their contents will NOT be altered:

 * commit 260b0811 (protected by 'HEAD')

Cleaning
--------

Found 81 commits
Cleaning commits:       100% (81/81)
Cleaning commits completed in 430 ms.

Updating 1 Ref
--------------

        Ref                    Before     After   
        ------------------------------------------
        refs/heads/test1 | 3db4545b | 87b66f4b

Updating references:    100% (1/1)
...Ref update completed in 46 ms.

Commit Tree-Dirt History
------------------------

        Earliest                                              Latest
        |                                                          |
        ..........................................................DD

        D = dirty commits (file tree fixed)
        m = modified commits (commit message or parents changed)
        . = clean commits (no changes to file tree)

                                Before     After   
        -------------------------------------------
        First modified commit | 707a5be5 | 37820e97
        Last dirty commit     | 3db4545b | 87b66f4b

Deleted files
-------------

        Filename   Git id                          
        -------------------------------------------
        test1.py | 37677ac6 (28 B), d1758471 (20 B)


In total, 6 object ids were changed. Full details are logged here:

        your-repo.git.bfg-report/2020-01-10/21-41-09

BFG run is complete! When ready, run: git reflog expire --expire=now --all && git gc --prune=now --aggressive


--
You can rewrite history in Git - don't let Trump do it for real!
Trump's administration has lied consistently, to make people give up on ever
being told the truth. Don't give up: https://www.theguardian.com/us-news/trump-administration
--
```

# Reference

- [BFG Repo-Cleaner by rtyley](https://rtyley.github.io/bfg-repo-cleaner/#download)
- [Reducing the repo size using git · Repository · Project · User · Help · GitLab](https://gitlab.com/help/user/project/repository/reducing_the_repo_size_using_git.md)
  
# Changelog
- 2020-01-11 增补问题
- 2020-01-10 init