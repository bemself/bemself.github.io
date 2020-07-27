---
title: Python 绘图 - Dash
date: 2020-02-02
description:  `Dash` 不仅仅是绘图，更是一个 `Python` 框架

---

# 背景

想熟悉另一个 Python 绘图工具 `Dash`，然而当我看到下面的官方介绍的时候，才意识到原来 `Dash` 不仅仅是绘图，更是一个 `Python` 框架，融合了 `Flask`，`Plotly.js`, `React.js`, 不会前端的（如我）可以直接用它来构造一个类似 `BI` Tools 的 UI，只要你会点 Python！当然去熟悉一下 [React](https://reactjs.org/tutorial/tutorial.html)会更容易理解Dash 中用到的 `components` 概念。

> Dash is a productive Python framework for building web applications.
Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It's particularly suited for anyone who works with data in Python.

# 安装

`pip install dash`

# 跑个 demo

参考：[Dash User Guide](https://dash.plot.ly/getting-started)

**基本步骤：**

- 准备工作
  - 准备 Assets，如外部样式和脚本，如 css， script 等
  - 准备数据（图表用）
    - 比如，可以从 csv 文件用 pandas 读取
  
- 创建 Dash app
  - 这里可以指定很多参数：如 Flask Server， StyleSheets， Assets 路径等等
  
- 创建 html component
  - 基本上每个`html tag`都对应一个`html component`,
  - 比如`html.H1` 代表 `<h1>`
  
- 创建 Dash Core Component: 
  - 如：Graph 用来渲染 plotly.js 数据可视化  
  
- 启动 Flask Server， 运行 Dash App

**示例代码：**

```
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

# 指定样式表或脚本
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# 创建 Dash app
# 这里可以指定很多参数：如 Flask Server， StyleSheets， Assets 路径等等
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# 创建 html component
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    # 创建 Dash Core Component: Graph
    # Graph can be used to render any plotly.js-powered data visualization.
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

# 启动 Flask Server， 运行 Dash App
if __name__ == '__main__':
    app.run_server(debug=True)
```

# Dash 应用场景？

> Dash is a user interface library for creating **analytical** **web** applications.Those who use Python for data analysis, data exploration, visualization,modelling, instrument control, and reporting will find immediate use for Dash...

显然，如果你想用 python 做一个数据分析/可视化/相关的 web app, 不管你对前端熟悉 or not，便可以试试 Dash。

具体见下文的架构。

# Dash 的架构

> Dash applications are web servers running Flask and communicating JSON packets over HTTP requests. Dash’s frontend renders components using React.js, the Javascript user-interface library written and maintained by Facebook

Dash 用的是 python [Flask](https://flask.palletsprojects.com/en/1.1.x/) web 框架，又借用了 React.js 来渲染前端的组件，但用户不需要很熟悉这些框架的细节，因为 Dash 又做了封装，暴露给用户的是 Dash 组件，即一些 python 类

Dash Components 主要有两种：

- Html 组件
- Core 组件

以 `html.H1` 组件为例，

代码中:
`html.H1(children='Hello Dash',id='h1',key='h1', ..., **kwargs):`
    
查看源码：

初始化的时候，将组件的属性分别用[setattr](https://docs.python.org/3/library/functions.html#setattr)设置了。
```
def __init__(self, **kwargs):
        # pylint: disable=super-init-not-called
        for k, v in list(kwargs.items()):
            setattr(self, k, v)
```

后续读取这些 attr 并转换为 json：
```
def to_plotly_json(self):
        # Add normal properties
        props = {
            p: getattr(self, p)
            for p in self._prop_names  # pylint: disable=no-member
            if hasattr(self, p)
        }
        # Add the wildcard properties data-* and aria-*
        props.update(
            ...)
        as_json = {
            "props": props,
            "type": self._type,  # pylint: disable=no-member
            "namespace": self._namespace,  # pylint: disable=no-member
        }

        return as_json
```

再之后呢，Dash 内部有工具可以将 React 组件自动生成 Python 类，这些 Python 类就是 Dash 组件了。

至于数据可视化，集成了[plotly.js](https://plot.ly/javascript/)，Javascript 的一个开源库，这个我不太熟悉。Dash 对外暴露的是 Graph 组件。

总的来说，Dash 的主要组件包括:

- **HTML Components** : `dash_html_components`
- **Dash Core Components**: `dash_core_components`
  - **Graph** component
    - 见前面 demo
  - **Markdown** component
    ```
    app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
    ])
    ```
  - **DropDown，CheckList** 等 component
    ```
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    )
    ```
  
# 求帮助：

```
import dash_core_components as dcc
>>> help(dcc.Dropdown)
```
  
# References:
- [plotly/dash: Analytical Web Apps for Python & R. No JavaScript Required.](https://github.com/plotly/dash)
- [introducing Dash](https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503)
- Dash - https://plot.ly/
- https://plot.ly/javascript/
- https://plot.ly/python/

- [dash · PyPI](https://pypi.org/project/dash/) 
- [tutorial](https://plot.ly/dash/getting-started)
- [Dash for Beginners (article)](https://www.datacamp.com/community/tutorials/learn-build-dash-python)

# Changelog
- 2020-02-02 init
