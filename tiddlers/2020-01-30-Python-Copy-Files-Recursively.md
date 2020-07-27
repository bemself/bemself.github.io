
# 背景

做工具的时候，遇到这种需求：将目录 A 复制到目录 B。

需求简单，但可能有多种情况：

- 目录 A 包含子目录吗
  - 如果只需要复制 A 中的文件呢？
  - 是否有文件需要过滤掉？
- 目录 B 是否已存在
- ...

比如，我做的时候遇到一个问题， 我的目录 A 中含有隐藏的 `.git` 目录，结果我忘记了，直接复制覆盖了目录 B 中的 `.git`, 然后 git 提交后发现把 A 指向的仓库给改掉了。这个可囧了。

所以在做之前，**先分析一下文件结构很重要**

# 分析文件结构

如前所述，我的目录中有`.git`目录需要过滤掉。其他都还好。

# 探索

找 python 中有哪些模块可以复制目录。

- **[distutils.dir_util copy_tree](https://docs.python.org/2.4/dist/module-distutils.dirutil.html)**

```
from distutils.dir_util import copy_tree
```

python 自带，用起来也很方便，

> copy_tree( 	src, dst[preserve_mode=1, preserve_times=1, preserve_symlinks=0, update=0, verbose=0, dry_run=0])
    every file in src is copied to dst, and directories under src are recursively copied to dst. Return the list of files that were copied or might have been copied, using their output name. 

然而，无法过滤指定的目录或文件。

- **[shutil](https://docs.python.org/3.7/library/shutil.html)**

>  shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)

    Recursively copy an entire directory tree rooted at src, returning the destination directory. The destination directory, named by dst, **must not already exist**; 

分析：

- 可以将目录A下的所有文件和子目录们都复制到 B，满足需求
- 有 `ignore pattern`, 可以 过滤掉 `.git`目录，满足需求
- 但是问题是：目标路径`dst`必须不能已存在，否则会报错。不满足需求
  - 不过，python 3.8 解决了这个问题，提供了`dirs_exist_ok=False`参数。
  - 但我本地还是 3.7，尚不想换到 3.8
  - 只好先删除 B 再复制

sample 代码：

```
if os.path.exists(dst):
  shutil.rmtree(dst, ignore_errors=False)
  shutil.copytree(src, dst,ignore=shutil.ignore_patterns(".git"))
```

- 自己写 loop，比如用 [os.walk](https://docs.python.org/3.7/library/os.html?highlight=os%20walk#os.walk) 或者 [glob.glob](https://docs.python.org/3.7/library/glob.html)

不详述了。建议是，能不造轮子就不造。但，如果是初学者，自己写则非常推荐。

# Changelog
- 2020-01-30 init