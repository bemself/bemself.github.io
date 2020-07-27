
# 背景

最近了解了 `tuple` 的设计由来，写了[Tuple 怎么用，为什么有 tuple 这种设计？](https://bemself.github.io/python/Python-Tuple.html)，便留意起来 `tuple` 的一些具体应用，观察到了已经没有留意到的点，记录一下，持续增补。

## for loop

经常用，但从未想过为什么可以这么写，`for _name, _value in _dict.items():`, `_name, _value` 可以这么逗号分隔直接罗列。

```
>>> _dict = {"name1": "test1", "name2": "test2"}
>>> for _name, _value in _dict.items():
...   print(type(_dict.items()))
...   print(_name, _value)
... 
<class 'dict_items'>
name1 test1
<class 'dict_items'>
name2 test2
```

打印一下 `_dict.items()` 的类型，返回的是 `dict_item` 类，这是一个 `set-like` 对象

> def items()
  D.items() -> a set-like object providing a view on D's items

所以也可以这么写：
```
>>> for _item in _dict.items():
...   print(_item)
...   _name, _value = _item
... 
('name1', 'test1')
('name2', 'test2')
```

可见，`_name, _value = _item` 便是 `for _name, _value in _dict`  由来了。

## sort

tuple 和 list 按官方说法，是很相似的数据类型，不过用处不一样。

list 有个 sort() 方法，可以原地排序列表，想当然的以为 tuple 也可以，实际其实不可以，因为我忘记了 tuple 一旦定义了，是不可改变的元组，自然不能原地排序了。

不过依然可以用 sorted() 方法。

## 单元素 tuple 为啥后面有个逗号

官方这么说的：

> Using a trailing comma for a singleton tuple: a, or (a,)

为啥要加个逗号，而不直接写成 `("a")`，这似乎才符合常规。

在 REPL 里面试过如下，原来 `("a")` 返回的是一个字符 `'a'`, 这就有点意思了，为啥要这么设计呢？不懂。

```
>>> "a",
('a',)
>>> ("a",)
('a',)
>>> ("a")
'a'
```

## [zip](https://realpython.com/python-zip-function/)


## 参考

- [tuple]([Using a trailing comma for a singleton tuple: a, or (a,)](https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple))

## ChangeLog
- 2019-12-25 init