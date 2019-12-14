---
title: Git - 删除 Git Commit 历史记录
date: 2019-12-14
edit: 2019-12-14
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description: 绕开这个问题好久了, 一直对删除心有余悸, 至今其实也不能完全应对, 但至少进步了点, 稍微理解了点 [git reset](https://git-scm.com/docs/git-reset), [git revert](https://git-scm.com/docs/git-reset)
---

# 背景

常在河边走, 难免不湿鞋, Git 虽然操作不多, 但错误接二连三, 其中最逃避的就是 回滚, 提交错了想回退, 战战兢兢不敢 hard 模式, 以至于 commit history 总是夹杂着问题.

## 问题重现

需要 删除历史记录的情况很多, 比如 删本地的, 删远程的我也没都遇到过, 也没都能尝试, 仅就自己遇到的先写点, 以后再慢慢增补

我遇到的多是:

- 本地 git add 后, 后悔了
- 本地 git ci 后, 后悔了
- 本地 git pu 后, 后悔了

## git commit 后回滚

- 如果还想保留之前的更改

```
git add .
git ci -m "test git reset after commit"
git reset --soft
```

做了啥事呢, 保留了你之前的更改, git现在 在等你继续改

现在到 `.git` 目录下会看到两个相关的文件:

  - ORIG_HEAD, 这个是从 HEAD 文件复制过来的

  这里面存的是一个 Head 指针, 指向的是当前最新的COMMIT (当前不是你刚才做的那个, 因为那个还在修改中), 比如这样子:

  ```
  b0c7fa87481d33f5277e49e0e92373aa50a4dc58

  ```

  - COMMIT_EDITMSG
  这里面是保存了你刚才reset的commit的msg, 即`test git reset after commit`
  为啥要有这个文件? 因为git想方便你修改后继续用这个msg提交, 当然你也可以替换掉用新的


## 思考

- 在用中学

## ChangeLog
- 2019-12-14 init