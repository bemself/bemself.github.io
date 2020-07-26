
# 背景

学习 [Linear Regression in Python – Real Python](https://realpython.com/linear-regression-in-python/)，对线性回归理论上的理解做个回顾，文章是前天读完，今天凭着记忆和理解写一遍，再回温更正。

# 线性回归(Linear Regression) 

刚好今天听大妈讲机器学习，各种复杂高大上的算法，其背后都是在求”拟合“。

线性回归估计是最简单的拟合了。也是基础中的基础。

依然是从字面上先来试着拆解和组合：

首先，**Regression** 回归，指的是研究变量之间的关系，这个由来在[Python 线性回归（Linear Regression) - 到底什么是 regression？](https://bemself.github.io/python/Python-Linear-Regression-Concept.html)一文中讲多了，这里不多重复。

然后，**linear** 线性，很直观：直线。

二者连在一起，便是：变量之间呈直线关系。

**那具体是哪些变量之间？**

因变量 y 和 自变量 (x1...xr) 之间。

`𝑦 = 𝛽₀ + 𝛽₁𝑥₁ + ⋯ + 𝛽ᵣ𝑥ᵣ + 𝜀`

当只有一个 x1 的时候，就是最简单的线性回归 `𝑦 = 𝛽₀ + 𝛽₁𝑥₁`。

**具体怎么理解这个公式呢？**

举个简化的例子：员工的工资 y 与 学历 x 的关系。

> 假设学历越高，工资也越高，二者是某种程度上的线性关系，

那在**理论上**会存在这么一个公式 `y = 𝛽₀ + 𝛽₁𝑥`，其中，x1...xn, y1...yn：

- x 和 y 的数据很容易拿到（当然合法渠道了，假设你是 hr 总监）
- hr 总监想做的是，根据这组 (x y)数据，找出 𝛽₀ 和 𝛽₁ 的值，二者称为**回归系数**
- 这样，下一次招聘的时候，根据应聘者的学历，可以先估一个工资了。

这个过程便是：数据 -> 建立模型 f(x) -> 预测

只是，理论和实际总是有差别的，就像 1/3 ~= 0.3333333333333...

所以，**实际拟合**到的模型可能是这样的： `f(x) = 𝑏₀ + 𝑏₁𝑥`

𝛽₀ 和 𝛽₁ 分别与 𝑏₀ 和 𝑏₁ 有多接近？

当然是拟合出来的越接近越好；
![](https://files.realpython.com/media/fig-lin-reg.a506035b654a.png)

**如何知道有多接近？**

简单，

- 将 x1...xn 代入到拟合后的模型中 f(x), 
- 求得新的 new_y1...new_yn 
- 再跟原 y1...yn 比较，比如 `new_y1 - y1` （称为残差）
  - 这里要用到最小二乘法（method of ordinary least squares）
  - 因为残差可能是负的，
  - 所以用残差平方和

**回归要解决的问题就是：**以最简单的线性回归为例：

- 找到最佳的 𝑏₀ 和 𝑏₁， 使模型 `f(x) = 𝑏₀ + 𝑏₁𝑥` 最接近理论上的线性模型 `y = 𝛽₀ + 𝛽₁𝑥`
- 然后，用这个拟合好的模型 `f(x) = 𝑏₀ + 𝑏₁𝑥` 来预测新的数据

# 线性回归好多种

除了上面例子中的最简单的线性回归，还有：

- 多元线性回归：Multiple linear Regression
  - `𝑓(𝑥₁, 𝑥₂) = 𝑏₀ + 𝑏₁𝑥₁ + 𝑏₂𝑥₂`
- 多项式回归：Polynomial Regression
  - `𝑓(𝑥) = 𝑏₀ + 𝑏₁𝑥 + 𝑏₂𝑥²`....

即从二维转为三维、多维空间拟合了。这个有点复杂了，不过原理和前面是相通的。

# 拟合的程度

过犹不及用在这里也适合，过度拟合也很脆弱的，因为可能新增加一个或几个数据就破坏了之前的完美，就好像专门为你定制的帽子戴在别人头上就没那么合适和美了。

![overfitting](https://files.realpython.com/media/poly-reg.5790f47603d8.png)](https://files.realpython.com/media/poly-reg.5790f47603d8.png)

当然，拟合的不及也不好，这时候可能就要换模型或者调参了吧

![underfitting](https://files.realpython.com/media/poly-reg.5790f47603d8.png)

# Reference

- [Linear Regression in Python – Real Python](https://realpython.com/linear-regression-in-python/)

# Changelog
- 2020-01-08 init