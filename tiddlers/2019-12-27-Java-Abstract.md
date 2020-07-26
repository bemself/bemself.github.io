
# 背景

一个简单的功能，读取一个文件，内包含一堆文件列表，运行时我们要读取一个目录，挨个检查里面的文件是否再这个文件列表中，如不在则抛弃，否则继续；

然后发现，文件中的列表越长，运行的速度慢的很；

# 分析

我最初的设计是，（以下用伪代码, 实际需求逻辑要复杂些，这里简化了）

在 main.java 中，

```
loop dirUnderTest:
  if (Utils.isIgnored(filename)){
    // do sth
  }
```

在 Utils.java 中：

```
public boolean isIgnored(fileName){
  if (fileList exists){
    files = readFromFileList()
    check if fileToCheck is in files
  }
}
```

相信有经验的朋友已经看出问题了。

但是欠缺经验的我，并没有看出这里的问题。

但意识中知道这个 isIgnored 检查放在 Utils 里面在程序运行的时候多次调用，不妥。

应该最好是一次性在别处（loop dirUnderTest)之前就做好，甚至，将 dirUnderTest 中的文件列表内容直接替换为 fileList 中的文件列表。

于是我朝着这个思路行进，结果被阻，限于第三方 plugin 的局限性，没法控制。

同事看了我的逻辑，一眼便找出问题所在，好丢人，我竟然在 isIngored 方法中读取文件，以至于每次调用这个方法，都要读一遍文件...

还没完，同事又建议我，抽象出一个 File 对象，将文件名、ignored 等属性都放进去，这样也方便将来提取信息；

恍悟。

# 收获

其实已经见过很多这种应用，比如 Json/xml/db 与 java 实体类 之间的转换，只是，以前是见别人用，然后在自己的程序中遇到 xml 序列化时也这么用了，但都还只限于模仿，并没有“举一反三“的应用，比如像这次同事的建议。所以印象深刻了。

也醒悟，我离专业程序员的道路还好远好远啊啊啊。

# ChangeLog
- 2019-12-28 init