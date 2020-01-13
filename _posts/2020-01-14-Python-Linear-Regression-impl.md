---
title: Python - 线性回归（Linear Regression) 的 Python 实现
date: 2020-01-08
edit: 2020-01-08
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  在 Python 中如何实现线性回归？很简单，有不错的包和函数~
---

# 背景

学习 [Linear Regression in Python – Real Python](https://realpython.com/linear-regression-in-python/)，前面几篇文章分别讲了“regression怎么理解“，”线性回归怎么理解“，现在该是实现的时候了。

# 线性回归的 Python 实现：基本思路

- 导入 Python 包: 有哪些包推荐呢？
  - `Numpy`：数据源
  - [`scikit-learn`](https://scikit-learn.org/stable/)：ML
  - [`statsmodels`](https://www.statsmodels.org/stable/index.html): 比 `scikit-learn` 功能更强大
- 准备数据
- 建模拟合
- 验证模型的拟合度
- 预测：用模型来预测新的数据

# 实现细节

以最简单的线性回归为例，代码参考的是原文。

重点是掌握基本思路，以及关键的几个函数。影响拟合度的因素很多，数据源首当其冲，模型的选择也是关键，这些在实际应用中具体讨论，这里就简单的对应前面的基本思路将 sample 代码及运行结果贴一下，稍加解释。

## 安装并导入包

根据自己的需要导入

```
pip install scikit-learn
pip install numpy
pip install statsmodels

from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
```

## 准备数据

""" prepare data
x: regressor
y: predictor
reshape: make it two dimentional - one column and many rows
y can also be 2 dimensional
"""

```
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
"""
[[ 5]
 [15]
 [25]
 [35]
 [45]
 [55]] 
"""
y = np.array([5, 20, 14, 32, 22, 38])
print(x, y)
# [ 5 20 14 32 22 38]
```

## 建模

```
'''create a model and fit it'''
model = LinearRegression()
model = model.fit(x, y)
print(model)
# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
```

## 验证模型的拟合度

```
'''get result
y = b0 + b1x
'''
r_sq = model.score(x, y)
print('coefficient of determination(𝑅²) :', r_sq)
# coefficient of determination(𝑅²) : 0.715875613747954
print('intercept:', model.intercept_)
# （标量） 系数b0 intercept: 5.633333333333329 -------this will be an array when y is also 2-dimensional
print('slope:', model.coef_)
# （数组）斜率b1 slope: [0.54]        ---------this will be 2-d array when y is also 2-dimensional
```

## 预测

```
'''predict response
given x, get y from the model y = b0+b1x
'''
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')
#predicted response:
#[8.33333333 13.73333333 19.13333333 24.53333333 29.93333333 35.33333333]

'''forecast'''
z = np.arange(5).reshape((-1, 1))
y = model.predict(z)
print(y)
#[5.63333333 6.17333333 6.71333333 7.25333333 7.79333333]
```

# 问题

# Reference

- [Linear Regression in Python – Real Python](https://realpython.com/linear-regression-in-python/)

# Changelog
- 2020-01-14 init