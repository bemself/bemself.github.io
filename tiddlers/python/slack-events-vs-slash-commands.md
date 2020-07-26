---
title:  Slack 交互- bot, slash command, events, RTM 之简单区别
date:  2020-05-04 11:00:55
edit:  2020-05-04 11:00:59
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  slack 这几种交互方式有啥区别, bot 又是啥
---

# 背景

想研究下怎么通过 slack 发送指令给第三方应用程序, 以及接收第三方程序的反馈.  从 slash command 开始看, 结果到 events 和 RTM 转了一圈, 又回到 slash commands, 发现这个才是最实惠简单符合需求的.

所以就简单记录一下我认为的三者的区别


# 必备

进行交互前, 得先理解:

- [Slack apps](https://api.slack.com/start/overview)
- [Using the Slack Web API](https://api.slack.com/web)
- [Bots](https://api.slack.com/bot-users#bots-overview)

简单两句话:
- slack app 是扩展了 slack 本身, 除了常规手动能做的操作外, 通过 api 强化了自动化操作. 
- bots 也是一类 slack app, 只不过是"虚拟的"你可以与之对话的"人", 通过 bot user 来实现实时对话.

这些自动化操作, 除了 slack 本身提供的之外, 便是第三方应用程序可与之交互实现的.

# 简述

slack 与第三方应用程序交互, 目前看起来有三种交互方式:

## [Event Subscriptions](https://api.slack.com/events-api#subscriptions)

理念是 `Don't call us, we'll call you`:

    - 3rd server 订阅了 slack 的某个类型的 event, 比如 react_added 了表情之类
    - 当用户在 slack 端触发了这个 event 时,
    - slack 发送请求到 3rd server, 带着包含这个 event 信息的 json payload
    - 3rd server 接受请求, 并针对这个 event 处理内部业务逻辑

这里的 3rd server 就静静的等着 slack 推送就好. 当然如果想主动去交互也 ok, 但这个不是设计应用重点.

> Before you can use the [Events API](https://api.slack.com/events-api) you must [create a Slack App](https://api.slack.com/apps/new), and turn on [Event Subscriptions](https://api.slack.com/events-api#subscriptions).

如果想用 python 开发, 可以试试 
[slackapi/python-slack-events-api: Slack Events API adapter for Python](https://github.com/slackapi/python-slack-events-api)

示例: [python-slack-events-api/example](https://github.com/slackapi/python-slack-events-api/tree/master/example)

虽然这个 events 很好用, 

>  Slack events are delivered to a secure webhook, and allows you to connect to slack without the RTM websocket connection.

但是实际环境中, 有些 3rd server 在防火墙后面, 可能不能主动收到 slack 的 events 请求. 这时候可以用 RTM client.

## [Real Time Messaging API](https://api.slack.com/rtm)

这个是可以实时监听 slack 的 events, 即 app server 得建立个连接, 放在那儿监听 slack 的信息. 不同于 events api 的那种 PUSH 模式 "slack 有了消息就 call 你", 而是 PULL 模式 "你去看看 slack 有消息了没". 
[slackapi/python-slackclient: Slack Python SDK https://slack.dev/python-slackclient/](https://github.com/slackapi/python-slackclient)

支持异步通信. 不过新的 slack app 已不太用这种方式了

>  New Slack apps may not use any Real Time Messaging API method. Create a classic app and use the V1 Oauth flow to use RTM.


## [Slash Commands](https://api.slack.com/slash-commands)
> Slash commands are special commands triggered by typing a "/" then a command. 

这个交互最简单直接, 在 slack channel 对话框中输入 "/<slash command> <your customized app command + args>, 比如输入 /say hello <name>, 你的 app server 会收到一个请求, payload 中有 text="hello <name>" , 你的 app 程序便可以解析并执行对应的业务逻辑, 然后返回结果给 slack.

实现上也很简单, 搭建个 flask api server, 处理一下 slack 请求就好. 不需要应对各种不同的 events (相对前面几类交互而言)

# Reference

- [Events API](https://api.slack.com/events-api) 
- [Serverless Slash Commands with Python - Renzo Lucioni](https://renzo.lucioni.xyz/serverless-slash-commands-with-python/)
- [slackapi/python-slackclient: Slack Python SDK https://slack.dev/python-slackclient/](https://github.com/slackapi/python-slackclient)
- [Botkit and Slack - Botkit Documentation](https://botkit.ai/docs/v0/readme-slack.html)

# ChangeLog
- 2020-05-04 init
