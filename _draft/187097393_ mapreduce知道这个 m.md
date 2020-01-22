

### map/reduce

知道这个 map/reduce 特性始自大数据, java 中的 stream 也有了这个功能, 现在在 clojure 里面看到, 似乎这里(lisp)才是功能源头? 功能确实很爽, 省却了 n 多行代码.

map: 对集合中的每一个元素做操作
filter: 筛选集合中符合条件的元素
reduce: 整合筛选后的元素, 如求和等

想单独拎出来的是下面这个:

```
user=> (reduce conj [2] '(3 2 1))
[2 3 2 1]
user=> (reduce conj '(3 2 1) [2])
(2 3 2 1)

user=> (conj [2] '(3 2 1))
[2 (3 2 1)]
user=> (conj [2] [1 2 3])         
[2 [1 2 3]]

user=> (conj 2 [1 2 3]) 
Execution error (ClassCastException) at user/eval209 (REPL:1).
java.lang.Long cannot be cast to clojure.lang.IPersistentCollection
```

 除了求和这种 reduce, 这里能看出来 reduce+conj 还可以将 List 和 Vector 缩成 一个 Vector 或 List. 这和单独用 conj 的区别便很明显了, 后者是扩展 Vector 或 List.

 至于这些设计的背后 可能隐藏什么 待探索