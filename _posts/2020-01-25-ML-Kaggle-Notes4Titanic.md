---
title: 我的第一个 Kaggle 比赛学习 - Titanic
date: 2020-01-25
edit: 2020-01-25
layout: post
status: Writing
categories:
  - Python, ML,Kaggle
tags:
  - Python, ML,Kaggle
description:  熟悉 Random Forest 算法，初识 ensemble learning
---

# 背景

[Titanic: Machine Learning from Disaster | Kaggle](https://www.kaggle.com/c/titanic)

2 年前就被推荐照着这个比赛做一下，结果我打开这个页面便蒙了，完全不知道该如何下手。

两年后，再次打开这个页面，看到清清楚楚的[Titanic Tutorial | Kaggle](https://www.kaggle.com/alexisbcook/titanic-tutorial)，完全傻瓜式的照着做就能做下来。当年是什么蒙蔽了我的眼睛~

## Target

use machine learning to create a model that predicts which passengers survived the Titanic shipwreck

## Data

[Titanic: Machine Learning from Disaster | Kaggle](https://www.kaggle.com/c/titanic/data)

- train.csv
  - Survived: 1=yes, 0=No
- test.csv
- gender_submission.csv: for prediction
  - PassengerId: those from test.csv
  - Survived: final result

## Guide to help start and follow

[Titanic Tutorial | Kaggle](https://www.kaggle.com/alexisbcook/titanic-tutorial)

- [Join the Competition Here!](https://www.kaggle.com/account/login?returnUrl=%2Fc%2Ftitanic)
- [Submit a initial result](https://www.kaggle.com/c/titanic/submit): 
- [NoteBook](https://www.kaggle.com/c/titanic/notebooks)
  
## Learning Model

摘抄的网站的解释，后面具体谈。

- random forest model
  -  constructed of several "trees" 
     -  that will individually consider each passenger's data 
     -  and vote on whether the individual survived. 
     -  Then, the random forest model makes a democratic decision: 
        -  the outcome with the most votes wins!

## [sklearn.ensemble.RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

Titanic比赛中用到的是 `RandomForestClassifier` 算法，在了解这个算法前，我注意到 `sklearn` 中这个算法类是在 `ensemble` 模块中，英文不好，不知道 `ensemble` 是什么意思？所以想先了解一下 `ensemble`

### ensemble

字典的解释是：`a number of things considered as a group`

听起来有组合的意思。

搜索了一下，在 ML 中有 `ensemble learning`, 翻译多是“集成学习”，参考[集成学习（ensemble learning）应如何入门？ - 知乎](https://www.zhihu.com/question/29036379)提到，有三种常见的集成学习框架：`bagging`，`boosting` 和 `stacking`。

从 [API Reference — scikit-learn 0.22.1 documentation](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.ensemble)中也能看出来这几种框架都有相应的算法。

`Random Forest` 是 `bagging` 框架中的一个算法。这里就单先试着理解这个，其他框架等以后遇到了再说。但是了解这个之前，还是得先清楚 [Ensemble Learning](https://en.wikipedia.org/wiki/Ensemble_learning) 到底是什么？

> In statistics and machine learning, ensemble methods use multiple learning algorithms to obtain better predictive performance than could be obtained from any of the constituent learning algorithms alone. 

这个解释应和了字面上的意思，组合了多种算法来获得更好的预测性能，结果优于单用其中的单个算法。

### bagging 框架

[sklearn.ensemble.BaggingClassifier — scikit-learn 0.22.1 documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html)

> A Bagging classifier is an ensemble meta-estimator that fits base classifiers each on random subsets of the original dataset and then aggregate their individual predictions (either by voting or by averaging) to form a final prediction.

大意就是：

- 从源数据集中随机抽样一部分子集样本
- 在这个子集样本上训练分类器
- 重复多次上述步骤
- 然后将各分类器的预测结果整合 （求平均或投票）
- 形成最终的预测

问题是：

- 抽取多少次子集样本，即要做多少分类器？
- 随机抽取的算法用什么？
- 整合各分类器结果的时候，求平均和投票各有什么优劣势？
- 如何训练各个分类器？

我都不晓得~

前面提到 `Random Forest` 是 `bagging` 框架的一种算法。现在来看看这个算法如何解答我的一些疑问。

### Random Forest 算法

[1.11. Ensemble methods — scikit-learn 0.22.1 documentation](https://scikit-learn.org/stable/modules/ensemble.html#forest)

> The prediction of the ensemble is given as the averaged prediction of the individual classifiers.

先明确了一个，这个算法是怼各分类器求平均的。Forest of what? 自然是 forest of trees, 而这里的 tree 指的是 **[decision trees](https://scikit-learn.org/stable/modules/tree.html#tree)**，所以这个算法其实是 **`averaging algorithms based on randomized decision trees`**

> random forest builds multiple decision trees and merges them together to get a more accurate and stable prediction.

`Random forest`对每个分类器都建一个决策树，然后再合并。

分类器是如何划分的呢？还是以 Titanic 的代码为例来试着理解下：

```
from sklearn.ensemble import RandomForestClassifier

y = train_data["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
```

- `y`：是训练集中灾难中存活的人的集合
- `features`: 是这些人的特征值，如性别，几等舱等
- X ：生成 dummy 数据，为什么要用 `get_dummies`而不是直接用`train_data[features]`呢？

尝试直接用 `train_data[features]`, 打印 X 的结果是这样的：

```
     Pclass     Sex  SibSp  Parch
0         3    male      1      0
1         1  female      1      0
```

如果再继续用这个 X 建模的话，会报错：

```
ValueError: could not convert string to float: 'male'
```

显然，因为 Sex 字段是 string 类型，而模型需要的是 float 类型，所以不能直接用  `train_data[features]`

那 `get_dummies()` 的作用也清楚了，就是将这些 string 类型的字段转化成 float 类型。从下面的打印结果也可以看出，Sex 字段被分成了两个字段，Sex_male, Sex_female, 其值分别是 0 和 1.

```
Pclass  SibSp  Parch  Sex_female  Sex_male
0         3      1      0           0         1
1         1      1      0           1         0
2         3      0      0           1         0
3         1      1      0           1         0
4         3      0      0           0         1
..      ...    ...    ...         ...       ...
886       2      0      0           0         1
887       1      0      0           1         0
888       3      1      2           1         0
889       1      0      0           0         1
890       3      0      0           0         1
```

- `RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)`
  - 这几个参数分别是什么意思？
    - n_estimators ： 决策树的数量
    - max_depths：决策树的最大深度
    - [random_state](https://scikit-learn.org/stable/glossary.html#term-random-state): 控制随机数生成器的，（实际没太明白，这个随机是不是指随机抽样？），可能要和其他参数配合用比如 shuffle。另外还提到，这个数用了控制随机算法，使得运行多次每次都还是产生相同结果？
      - To make a randomized algorithm deterministic (i.e. running it multiple times will produce the same result), an arbitrary integer random_state can be used

具体如何调参，参考 [parameter tuning guidelines](https://scikit-learn.org/stable/modules/ensemble.html#random-forest-parameters)

## `Random Forest`的应用场景

既然是分类器算法，自然很多分类应用的场景都适合了；另外还有回归问题的场景。

这篇文章[The Random Forest Algorithm: A Complete Guide | Built In](https://builtin.com/data-science/random-forest-algorithm)给出了一个实际例子的类比：

- 你在决定去哪儿旅行，去询问你的朋友
- 朋友问，你以前的旅行中喜欢和不喜欢的方面都哪些
  - 在这个基础上给出了一些建议
- 这为你的决策提供了素材
- 同样的步骤，你又去询问另一个朋友
- 以及另另一个朋友
- ...

同样，你拿到了几个 offer，犹豫该接哪个等等；看中了几套房子，决定选哪个，貌似都可以套用这个算法一试了。

## 学到的几个之前不熟悉的代码

- [pandas.DataFrame.head](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html)：返回数据集中的头几行数据，参数为 n，默认 n=5

```
test_data = pd.read_csv("/kaggle/input/titanic/test.csv")
test_data.head()
```

- [pandas.DataFrame.loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)

```
men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)
```

## Reference

- [集成学习（ensemble learning）应如何入门？ - 知乎](https://www.zhihu.com/question/29036379)
- [Ensemble Learning》](https://link.zhihu.com/?target=http%3A//cs.nju.edu.cn/zhouzh/zhouzh.files/publication/springerEBR09.pdf)
- [The Random Forest Algorithm: A Complete Guide | Built In](https://builtin.com/data-science/random-forest-algorithm)

## ChangeLog
- 2020-01-22 init