---
title: Git - Git 操作问题罗列
date: 2019-12-14
edit: 2019-12-14
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description: 持续记录 Git 使用中遇到的各种问题，待后续重拾记忆~
---

# Git 操作问题多多

很多问题，如果不记下来，下次还会遇到，得重头再来，故写此文，持续记录~ 到哪天 Git 过时不用了，其实可能是我不用了~

## 问题

## git check 其他分支提示 untracked working tree files would be overwritten

本地的文件有修改，但还没有 indexed, 用 `git checkout` 不灵：
```
> git checkout <another_branch_name>
error: The following untracked working tree files would be overwritten by checkout:
        1-js/03-code-quality/01-debugging-chrome/largeIcons.svg
Please move or remove them before you switch branches.
```

如果你不想保留这些文件，那就加 `-f` 参数：

```
git checkout -f <another_branch_name> 
```

同样，在 `git merge`的时候也遇到过这个错误，但`git merge`没有 `-f`参数，所以只能先 track 文件再 merge 了，像这样：

```
git add * 
git stash
git stash drop        // 如果不想保留这个 stash
```

在 [这个答案](https://stackoverflow.com/questions/17404316/the-following-untracked-working-tree-files-would-be-overwritten-by-merge-but-i)中提到还有一种情况，上述解决方法就不灵了，

> This doesn't work if the files are from submodules that were removed and then readded as normal files

那样的话，就要用到这个命令：(我没有实操过这个，仅做记录待验)

```
git fetch --all
git reset --hard origin/{{your branch name}}
```

## git merge conflict, using ours or theirs

```
CONFLICT (content): Merge conflict in article.md
matic merge failed; fix conflicts and then commit the result.
```
解决方法：

```
git checkout --ours article.md
or
git checkout --theirs article.md
```
## unable to delete 'remote_branch': remote ref does not exist

我的某个 PR merge 之后， 页面提示我说你的 这个 PR 的分支可以安全删除了，我就愉快的删除了。

结果我到本地 `git brach -a` 发现还在呀：

```
remotes/origin/pr-branch
```

那就再删一遍吧：

```
git pu origin --delete pr-branch
```

但是报错了，`error: unable to delete 'pr-branch': remote ref does not exist`

原因自然是远程那个分支已经被删除了，那现在我`git br -a`看到的其实是我本地保存的 远程分支，只要把这个删除就好了

那怎么删？

首先想到用 `git branch -d remotes/origin/pr-branch` 来删，结果说`error: branch remotes/origin/pr-branch 不存在`，但如果我 `cat .git/refs/remotes/origin/pr-branch` 是没问题的，那是咋回事？没有想通，想是 git 哪个环节失灵了。

好在还有其他办法，在[git remove branch](GIT-remove-branch.html) 一文中提到过，分支就是个指针，在系统中以文件形式存在着，所以找到 `.git/refs/remotes/origin`下面的以分支命名的文件，删掉即可: ```rm -f .git/refs/remotes/origin/pr-branch```


##  ChangeLog
- 2019-12-20 update
- 2019-12-14 init