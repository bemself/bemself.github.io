---
title: Java - 多环境下代码切换
date: 2019-12-20
edit: 2019-12-20
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description: 应对不同版本的依赖管理
---

# 背景

学员提交代码后，大妈和助教会去逐行 review 代码，提一些 comments，但是，不少同学都 get 不到这些 comments，甚至有的同学第一次用 gitlab，还不知道 Commit Comments 是啥，不知道哪里去看，不知道什么时候有了 comments 得去看看，所以这里就简单聊一下。

# Commit Comments 是啥

先打个比方，传统教学中：

- 老师布置作业
- 学生做好交作业
- 老师批改作业写评语
- 发回同学或表扬或要求修改

网络教学其实也很相似啊，只是更加灵活，甚至灵活的有时候学员找不到北：

- 老师布置作业（比如每周周任务）
- 同学提交作业代码 （即 commit)
- 老师“批改”代码，其实这里常用的词是 Review（审阅）
- 老师在某行代码上写“评语”，这里的评语就是 comment 了，即 commit comment
  - 甚至同学相互之间都可以点评，因为所有人都能看到其他人的代码

到此，网络教学和传统教学基本相同，差别主要在后面，同学如何 get 到老师的评语

传统教学中，老师或者当面或者委托学习委员发作业，没有同学会 get 不到，对吧

网络教学就不太一样了，虽然老师够不着同学，但是网络、计算机几乎无所不能，反而是提供了很多渠道，只是多未必就是好，依然有很多同学 get 不到。所以下面就讲讲几个渠道。

## 如何接收老师评语（Commit Comments)

### 渠道 1： 邮件

习惯邮件工作的同学，这个是最快了。老师的每个 comment 都会第一时间自动发送到邮件列表中，所有的同学都能看到老师对任何人的点评；

### 渠道 2： Slack

Slack 绑定了 Gitlab 仓库，仓库中的任何动态也都会第一时间推送到 Slack 的学员频道中

### 渠道 3：Gitlab

- [Gitlab Commits 页面](https://gitlab.com/101camp/4py/tasks/commits/master)
- [Gitlab Graph](https://gitlab.com/101camp/4py/tasks/-/network/master)
- [Gitlab TO-DO](https://gitlab.com/dashboard/todos)
- Gitlab Blame (for 助教点评) [blame](https://gitlab.com/101camp/4py/tasks/blame/master/ch2.md)

## ChangeLog
- 2019-12-17 init