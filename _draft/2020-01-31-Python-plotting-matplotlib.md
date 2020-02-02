---
title: Python 绘图 - matplotlib 初探
date: 2020-01-31
edit: 2020-01-31
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  一个晚上听到了 N 种可视化工具以及风格，头脑发蒙，这么多该怎么选择？想到也许真应该从工具创作的渊源出发去了解背景，然后找应用场景。所以开始挨个工具了解一下，本文主要是 matplotlib

---

# 背景

- Dash is for creating interactive web-apps, plotly.py with matplotlib is for graphing
# 安装

# 跑个 demo


```
>>> import matplotlib.pyplot as plt
>>> plt.style.use('ggplot')
```

基本就是类似以下三步：再加上一些坐标轴、样例等

```
fig, ax = plt.subplots()
ax.boxplot((x, y, z), vert=False, showmeans=True, meanline=True,
           labels=('x', 'y', 'z'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.show()

```

# 理解基本概念

# References

# ChangeLog
- 2020-01-30 init