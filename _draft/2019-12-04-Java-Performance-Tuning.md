---
title: Java - 性能调试 (1)
date: 2019-12-04
edit: 2019-12-04
status: Writing
layout: post
categories:
  - Java
tags:
  - Java
description:  记录几个关于影响Java性能的写法
---

# 背景
Java 新手一个, 写代码的时候顾着早日完成任务, 疏忽了很多细节, 待看书时, 之前写过的代码相关的, 发现不少性能问题, 赶紧记录下来. 

本篇主要涉及以下几点:

- String
    - replace vs replaceAll
- Pattern
- contains
- for loop
- Stream
- File exists

日后遇到其他的, 当另开文述. 

我的记录很粗浅, 也欢迎读者留言指正和提醒^_^

# 分析


## String concatenation
- [String Concatenation](https://docs.oracle.com/javase/specs/jls/se9/html/jls-15.html#jls-15.18.1)

拼接字符串的几种常用方法:

- + :
    - 内部实现用的是 StringBuilder
- += : 便捷常用,但其实性能差的
    - 每次+= 都会生成新的String对象
- String.format( "{a: %s, b: %s, c: %s}", a, b, c );
    - 可读性略差
- String.concat()
- StringBuilder
    - not-synchronized, 适合单线程, 
    - concatenation in loops
    - 性能最优
- StringBuffer 
    - synchronized, 适合多线程

###  +=, +
这两者的拼接有几种情况:

- 一次性直接 "+"
- 循环 "+" (for loop)
- +=

#### 一次性直接 "+"

```
String str = "a" + "b" + "c";
```

这个内部实现用的是 StringBuilder, 所以一次性用没太大性能问题.

#### 循环 "+"/"+=" (for loop)
```
public String myConcat(String[] vals) {
    String str = "";
    for (String val : vals) {
        str = str + val;
    }
    return str;
}
```

由于 string 是immutable的, 每次 + 之后 都会生成新的String对象, 随着循环次数的增多, 生成的中间对象就越多, 自然不可取了.

#### +=
```
String str = "a";
 str += "b";
 str += "c";
```

与在循环中使用, 每一次拼接(+=), 都会生成一个新的 String 对象, (除非是已在 String pool 中).

拼接的次数越多, 就会有更多的 String 对象.

### StringBuilder & StringBuffer
这两个方法只有一个区别, 即 StringBuffer是 synchronized, 适合于多线程. 平常单线程用 StringBuilder. 所以下文单以StringBuilder为例.

- [StringBuilder (Java Platform SE 8 )](https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuilder.html)
> **StringBuilder** class provides an API compatible with **StringBuffer**, but with no guarantee of synchronization. This class is designed for use as a drop-in replacement for StringBuffer in places where the string buffer was being used by **a single thread** (as is generally the case). Where possible, it is recommended that this class be used in preference to StringBuffer as it will be **faster** under most implementations.

相较于 + 和 +=, StringBuiler 省却了生成大量中间产物(新的 String 对象).

- [The Java® Language Specification](https://docs.oracle.com/javase/specs/jls/se8/jls8.pdf)

> To increase the performance of **repeated** string concatenation, a Java compiler may use the **StringBuffer** class or a similar technique to reduce the number of intermediate String objects that are created by evaluation of an expression.

## file exists
文件处理常用到判断文件是否存在.

Java 中有两个类似方法:

- java.io.File.Files.exists()
- java.io.File.exists()


Java 8's "Files.exists" should not be used
 
Code smell
 
Major
squid:S3725
 
The Files.exists method has noticeably poor performance in JDK 8, and can slow an application significantly when used to check files that don't actually exist.
The same goes for Files.notExists, Files.isDirectory and Files.isRegularFile.
Note that this rule is automatically disabled when the project's sonar.java.source is not 8.
Noncompliant Code Example
  Path myPath;  if(java.nio.Files.exists(myPath)) { // Noncompliant   // do something  }  
Compliant Solution
  Path myPath;  if(myPath.toFile().exists())) {   // do something  }  
See
https://bugs.openjdk.java.net/browse/JDK-8153414
https://bugs.openjdk.java.net/browse/JDK-8154077

### java.io.File.Files.exists()


### java.io.File.exists
用法:

```
Path myPath = Paths.get("c:/temp/file.name");
if(myPath.toFile().exists())) { 
 // do something
}
```

首先看源码:

```
package java.io
public class File implements Serializable, Comparable<File> {
 private static final FileSystem fs = DefaultFileSystem.getFileSystem();
 public boolean exists() {
        ...some necessary check, omitted here
        return ((fs.getBooleanAttributes(this) & FileSystem.BA_EXISTS) != 0);
    }
}
```

这里主要的逻辑是在 fs 这个 FileSystem 实例中做的, 源代码如下:

```
/**
 * Package-private abstract class for the local filesystem abstraction.
 */

abstract class FileSystem {   
    @Override
    public native int getBooleanAttributes(File f);
```

可以看出, 实际的check工作并不是Java在做, 而是运行程序所在的OS底层做的, 所以性能也就与Java无关了.

## stream.reduce vs stream.collect
- Unlike the reduce method, which always creates a new value when it processes an element, the collect method modifies, or mutates, an existing value.

## Set: Hashset, linkedHashset, Treeset
The Java platform contains three general-purpose Set implementations: HashSet, TreeSet, and LinkedHashSet. 

- HashSet, which stores its elements in a hash table, is the best-performing implementation; however it makes no guarantees concerning the order of iteration. 

- TreeSet, which stores its elements in a red-black tree, orders its elements based on their values; it is substantially slower than HashSet. LinkedHashSet, which is implemented as a hash table with a linked list running through it, orders its elements based on the order in which they were inserted into the set (insertion-order). 

- LinkedHashSet spares its clients from the unspecified, generally chaotic ordering provided by HashSet at a cost that is only slightly higher.

## for loop
- move loop unrrelated outside loop
e.g. for (i;i<=strs.size()..)

## contains


### HashSet
- Internally, the HashSet implementation is based on a HashMap instance. The contains() method calls HashMap.containsKey(object).

Here, it's checking whether the object is in the internal map or not. The internal map stores data inside of the Nodes, known as buckets. Each bucket corresponds to a hash code generated with hashCode() method. So contains() is actually using hashCode() method to find the object's location.

the contains() of HashSet runs in O(1) time. Getting the object's bucket location is a constant time operation. Taking into account possible collisions, the lookup time may rise to log(n) because the internal bucket structure is a TreeMap.

### ArrayList
ArrayList uses the indexOf(object) method to check if the object is in the list. The indexOf(object) method iterates the entire array and compares each element with the equals(object) method.

Getting back to complexity analysis, the ArrayList.contains() method requires O(n) time. So the time we spend to find a specific object here depends on the number of items we have in the array.

## stream vs parallelstream
In JDK 8 and later, the preferred method of iterating over a collection is to obtain a stream and perform aggregate operations on it. Aggregate operations are often used in conjunction with lambda expressions to make programming more expressive, using less lines of code. The following code sequentially iterates through a collection of shapes and prints out the red objects: 
myShapesCollection.stream()
.filter(e -> e.getColor() == Color.RED)
.forEach(e -> System.out.println(e.getName()));
Likewise, you could easily request a parallel stream, which might make sense if the collection is large enough and your computer has enough cores: 
myShapesCollection.parallelStream()
.filter(e -> e.getColor() == Color.RED)
.forEach(e -> System.out.println(e.getName()));

## replace vs replaceAll

"String#replace" should be preferred to "String#replaceAll"
 
Code smell
 
Critical
squid:S5361
 
The underlying implementation of String::replaceAll calls the java.util.regex.Pattern.compile() method each time it is called even if the first argument is not a regular expression. This has a significant performance cost and therefore should be used with care.
When String::replaceAll is used, the first argument should be a real regular expression. If it’s not the case, String::replace does exactly the same thing as String::replaceAll without the performance drawback of the regex.
This rule raises an issue for each String::replaceAll used with a String as first parameter which doesn’t contains special regex character or pattern.
Noncompliant Code Example
  String init = "Bob is a Bird... Bob is a Plane... Bob is Superman!";  String changed = init.replaceAll("Bob is", "It's"); // Noncompliant  
Compliant Solution
  String init = "Bob is a Bird... Bob is a Plane... Bob is Superman!";  String changed = init.replace("Bob is", "It's");  
Or, with a regex:
  String init = "Bob is a Bird... Bob is a Plane... Bob is Superman!";  String changed = init.replaceAll("\\w*\\sis", "It's");  
See
{rule:squid:S4248} - Regex patterns should not be created needlessly

## Pattern
- Pattern.matches
- String.matches

# 性能调优何处知晓
Benchmark 是推荐做法, 不过我还没用过, 写在这里待以后需要时用.

- https://stackoverflow.com/questions/504103/how-do-i-write-a-correct-micro-benchmark-in-java

- [JMH](https://javapapers.com/java/java-micro-benchmark-with-jmh/) 
> JMH is a Java Microbenchmark Harness (JMH), a open source software by OpenJDK to create benchmarks for Java program

## JMH
运行[Java String vs StringBuilder vs StringBuffer Concatenation Performance Micro Benchmark - Javapapers](https://javapapers.com/java/java-string-vs-stringbuilder-vs-stringbuffer-concatenation-performance-micro-benchmark/)的代码, 得到的比较结果:

Benchmark           Mode  Cnt  Score   Error  Units
Demo.stringBuffer     ss  100  0.991 ± 0.207   s/op
Demo.stringBuilder    ss  100  0.645 ± 0.139   s/op
Demo.stringConcat     ss  100  1.539 ± 0.300   s/op
Demo.stringPlus       ss  100  0.763 ± 0.141   s/op

### setup
- [JMH 官网](http://openjdk.java.net/projects/code-tools/jmh/)

pom.xml

```
<!-- https://mvnrepository.com/artifact/org.openjdk.jmh/jmh-core -->
<dependency>
    <groupId>org.openjdk.jmh</groupId>
    <artifactId>jmh-core</artifactId>
    <version>1.22</version>
</dependency>
<!-- https://mvnrepository.com/artifact/org.openjdk.jmh/jmh-generator-annprocess -->
<dependency>
    <groupId>org.openjdk.jmh</groupId>
    <artifactId>jmh-generator-annprocess</artifactId>
    <version>1.22</version>
    <scope>test</scope>
</dependency>

```

### new project
$ mvn archetype:generate \
          -DinteractiveMode=false \
          -DarchetypeGroupId=org.openjdk.jmh \
          -DarchetypeArtifactId=jmh-java-benchmark-archetype \
          -DgroupId=org.sample \
          -DartifactId=test \
          -Dversion=1.0

### run
mvn clean install exec:exec > result.log

### Terms


#### Throughput
@BenchmarkMode({Mode.Throughput}) calculates the operations per second

#### AverageTime
@BenchmarkMode({Mode.AverageTime}) calculates seconds by operations.

### issues


#### Exception in thread "main" org.openjdk.jmh.runner.RunnerException: ERROR: Unable to acquire the JMH lock (E:\Temp\/jmh.lock): already taken by another JMH in
Exception in thread "main" org.openjdk.jmh.runner.RunnerException: ERROR: Unable to acquire the JMH lock (E:\Temp\/jmh.lock): already taken by another JMH in
stance, exiting. Use -Djmh.ignoreLock=true to forcefully continue.

不知道怎么办,最后是kill process了

#### build failure: no executable...
运行 mvn clean install exec:exec > result.log

报错: no executable...

解决:
```
<plugin>
                        <groupId>org.codehaus.mojo</groupId>
                        <artifactId>exec-maven-plugin</artifactId>
                        <version>1.4.0</version>
                        <configuration>
                            <executable>java</executable>
                            <arguments>
                                <argument>-classpath</argument>
                                <classpath/>
                                <argument>benchmark.jmh.HelloWorldBenchmark</argument>
                            </arguments>
                        </configuration>
                    </plugin>
```

# Reference
- https://java-performance.com/
- [The Java® Language Specification](https://docs.oracle.com/javase/specs/jls/se9/html/index.html)

