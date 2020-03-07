---
title: Python 绘图 - Bokeh 堆叠柱状图(stacked bar)
date: 2020-01-30
edit: 2020-01-30
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  在 [Bokeh 初探](https://bemself.github.io/python/Python-plotting-bokeh.html)之后，学习使用它来做个堆叠柱状图

---

# 背景

在 [Bokeh 初探](https://bemself.github.io/python/Python-plotting-bokeh.html)之后，学习使用它来做个图

# 目标

做一个柱状图，支持多个 y 数据源，即有堆叠效果的柱状图 stacked bar

# 实现

## 单数据源 简单的柱状图

参考 [Handling Categorical Data — Bokeh 1.4.0 documentation](https://docs.bokeh.org/en/latest/docs/user_guide/categorical.html)

```
from bokeh.io import show, output_file
from bokeh.plotting import figure

output_file("bars.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]

p = figure(x_range=fruits, plot_height=250, title="Fruit Counts", toolbar_location=None, tools="")

p.vbar(x=fruits, top=counts, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
```

效果图见上述参考

## 增加一个 y 数据源，做堆叠效果

这样的话，需要考虑：

- 数据源：不能是单一的列表了，得能容纳多组数据。用字典。

```
fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ["2015", "2016", "2017"]

data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 4, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}
```

- 颜色：区分不同的数据源

`colors = ["green", "#718dbf", "#e84d60","#e84d20","#e84361"]`

配色是个问题，一不小心就会很丑，后面会提到用调色板 `palette`

- 画图：上面的`vbar`不支持堆叠
```
p.vbar_stack(years, x='fruits', width=0.9, color=colors, source=data,legend_label=years)
```

## 导出为文件
[Exporting Plots — Bokeh 1.4.0 documentation](https://docs.bokeh.org/en/latest/docs/user_guide/export.html)
- html

output_file("file.html")

- png

- `npm install selenium phantomjs`
- `npm install -g phantomjs-prebuilt`
- `pip install bokeh`

然后 `from bokeh.io import export_png`

## 数据源： 从 .csv 文件读取数据

我试过两种方式，现在用的是第二种 pandas

- **numpy 的 `genfromtxt`**

但是我遇到很多问题，包括不同的 dtype参数，names参数等，返回不同的数据类型的 array，感觉很不方便（如排序等），所以后来弃用了，当然也是因为我不太熟。

```
from numpy import genfromtxt
    my_data = genfromtxt("data.csv", delimiter=',', dtype=None, encoding="utf8")
```

- **pandas** 

还是这个方便，读取文件 :

```
df = pd.read_csv("data.csv",header=0)
``` 

**取前 7 行**：`df = df.head(n=7)`

**取某一列**：`df['col1']`

**几列求和**： df['col1'] + df['col2'] + df['col3']

**排序**：`df = df.sort_values(by='col1', ascending=False)`

## x axis 旋转

[Styling Visual Attributes — Bokeh 1.4.0 documentation](https://docs.bokeh.org/en/latest/docs/user_guide/styling.html#tick-label-orientation)

比如左斜 旋转 45 度：

```
    p.xaxis.major_label_orientation = 360-45
```

## 调色板

前面我们用 `colors = ["green", "#718dbf", "#e84d60","#e84d20","#e84361"]` 人工配色，会很丑不专业，bokeh 有自带的调色板，倒是很方便，还好看。

```
>>> from bokeh.palettes import brewer
>>> colors = brewer["Blues"][6]
>>> colors
['#08519c', '#3182bd', '#6baed6', '#9ecae1', '#c6dbef', '#eff3ff']
```

具体列表参考：
  
- [bokeh.palettes](https://docs.bokeh.org/en/latest/docs/reference/palettes.html)
- [源码：bokeh/palettes.py at master · bokeh/bokeh](https://github.com/bokeh/bokeh/blob/master/bokeh/palettes.py)
- [bokeh.colors — Bokeh 1.4.0 documentation](https://docs.bokeh.org/en/latest/docs/reference/colors.html)


## 分类数据处理

如果 x 数据只是数字 如`[1,2,3]`，上面demo 中的 `p.figure`足以处理

但如果 x 或 y 坐标是一些分类数据如`["apple","orange"]` ，则需要再添加 `x_range`,或 `y_range`等

如 

```
fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
p = figure(x_range=fruits, ... )
p.vbar(x=x, top=y, legend_label="Temp.", width=0.9)
```

参考 [Handling Categorical Data — Bokeh 1.4.0 documentation](https://docs.bokeh.org/en/latest/docs/user_guide/categorical.html)


# References
- [bokeh/bokeh: Interactive Data Visualization in the browser, from Python](https://github.com/bokeh/bokeh)
- [数据可视化 到 可视化信息 浅述 ](http://wiki.zoomquiet.io/IMHO/data-v-info)
  
# ChangeLog
- 2020-03-07 init