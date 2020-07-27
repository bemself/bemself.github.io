---
title: Python 调试简便大法
date: 2020-03-29
description:  python 调试，其实就是 print 大法，加上...

---

初始刚接触 python 的时候，出错调试的时候，颇有些不习惯。以前用 IDE 习惯加断点调试，而 python 初学的时候就被各种建议，不要用 IDE，不要用 IDE...，于是 sublime，vscode 都用过了，对加断点调试绝了念头（不会用）。

现在，即使在 pycharm 中，也习惯不加断点调试了。

因为，越来越觉得 print 确实是大法，很好用。

而且，再加上两个大法，更爽。

1. print 之后 加 return

如果只是跑一个 func，在出错的某行加了 print，可以在之后加 return，后面的代码就不会跑了，直接看打印出来的结果查错。

2. print 之后 加 quit()

复杂一点的，可能嵌套在或嵌套了其他 func，那就在 print 之后粗暴的 quit()就好了。

不过，print 也是有技巧的，如果输出是长串 json 格式的数据呢？如果是很长的文本呢？

这就可以用 python 自带的一些方法了：

- [pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint)来美化输出如 json 格式，当然必要的时候输出到文件看更方便。

- [textwrap — Text wrapping and filling — Python 3.8.2 documentation](https://docs.python.org/3/library/textwrap.html)
亦或，如果输出的文本很长，想 wrap 一下，或者保留某种格式输出，可以用 python 自带的

```
from textwrap import dedent
def test():
    # end first line with \ to avoid the empty line!
    s = '''\
    hello
      world
    '''
    print(repr(s))          # prints '    hello\n      world\n    '
    print(repr(dedent(s)))  # prints 'hello\n  world\n'
```

当然，这也有个人习惯的问题，以及项目大小的问题（我当然没做过大项目了，所以此大法用着很爽），也有很多 python 调试的工具，比如:

- [pdb — The Python Debugger — Python 3.8.2 documentation](https://docs.python.org/3/library/pdb.html), 
- [logging — Logging facility for Python — Python 3.8.2 documentation](https://docs.python.org/3/library/logging.html)
  - 专业一点的话，还是建议多打 log