---
title: Python 绘图 - Bokeh 初探
date: 2020-01-30
edit: 2020-01-30
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  一个晚上听到了 N 种可视化工具以及风格，头脑发蒙，这么多该怎么选择？想到也许真应该从工具创作的渊源出发去了解背景，然后找应用场景。所以开始挨个工具了解一下，本文主要是 Bokeh

---

# 背景

想了解一下 python 中的几个绘图工具，及其应用场景。`bokeh` 为其一.

先放一段 Bokeh 的 Vision：

> Bokeh is an **interactive** visualization library that targets modern web browsers for presentation. Its **goal** is to provide elegant, concise construction of versatile graphics, and to extend this capability with **high-performance** interactivity over very large or streaming datasets. Bokeh can help anyone who would like to quickly and easily create interactive plots, dashboards, and data applications. 

焦点词：交互式，高性能，浏览器。

# 安装

`pip install bokeh` 或使用镜像 `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple bokeh`

# 跑个 demo

参考：[Quickstart — Bokeh 1.4.0 documentation](https://docs.bokeh.org/en/latest/docs/user_guide/quickstart.html#getting-started)

基本步骤：

- 准备数据
- 确定输出方式：
  - html 文件 或
  - Jupyter Notebook
- 建Figure模块（对象）：
  - 用 `bokeh.plotting` 模块
    - 主要的函数：`figure()`
- 画图：
  -  glyphs, 比如线形图，圆饼等
    - 如 `line`
- 显示或保存图
  - `show()`
  - `save()`

demo 代码：

```
from bokeh.plotting import figure, output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="Temp.", line_width=2)

# show the results
show(p)
```

实际图形就不挂出来了，跑一下代码立刻生成。

**输出到 Jupyter Notebook**

如果是在 Jupyter Notebook 中，用 output_notebook(): 

```
from bokeh.io import output_notebook
output_notebook()
```

# 理解基本概念

参考：[Defining Key Concepts — Bokeh 1.4.0 documentation](https://docs.bokeh.org/en/latest/docs/user_guide/concepts.html)

> Bokeh is an **interactive** **visualization** library for modern web browsers. It provides elegant, concise construction of versatile **graphics**, and affords high-performance interactivity over large or streaming datasets. Bokeh can help anyone who would like to quickly and easily make interactive plots, dashboards, and data applications.

在浏览器中 交互式图表库，`interactive` 怎么理解呢？

一个简单的例子，比如[Interactive Legends — Bokeh 1.4.0 documentation](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/legends.html)，图表中的图例，可以点击某个或某几个显示或隐藏。

再比如，[Adding Widgets — Bokeh 1.4.0 documentation](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/widgets.html#button)，在浏览器页面上添加 button 等控件。

Bokeh Python 库 和 Bokeh 客户端库 BokehJS（有自己的API), 负责浏览器上图形的绘制和 render，所以这些交互式操作有 JS 的支持，这估计是 boken 的一大特色。


大致的结构和接口：

```
- 最上层:**BokehJS**          render UI and handle UI interactions
            |--- Documents
                    |---Models：
                          |------plots
                                |------glyphs
                          |------widgets 
                                
                    |---Data：      图表所需的数据
                    |---Widgets：   交互式控件，如 button 等
                    

- 中间层: **boken.plotting**
            |---figure()  -> Figure Model

- 最底层: **bokeh.models**
```

# References
- [bokeh/bokeh: Interactive Data Visualization in the browser, from Python](https://github.com/bokeh/bokeh)
- [Defining Key Concepts — Bokeh 1.4.0 documentation](https://docs.bokeh.org/en/latest/docs/user_guide/concepts.html)
- [Pypi | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)
- [Interactive Data Visualization in Python With Bokeh](https://realpython.com/python-data-visualization-bokeh/)

# ChangeLog
- 2020-01-30 init