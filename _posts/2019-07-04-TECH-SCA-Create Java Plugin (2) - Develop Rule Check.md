---
title: SonarQube - Create Custom Java Plugin (1)
date: 2019-07-04
edit: 2019-07-04
status: Writing
layout: post
categories:
  - Java
  - Static Code Analysis
tags:
  - Java
  - SCA
description: 静态代码扫描系列 - Create Custom Java Plugin (2), Create Rule
---

# SonarQube: Create Custom Java Plugin (2)

## Summary

- [X] Maven Dependencies
  - [X] Add sonarqube-server
  - [X] Add sonar-java
- [X] Create Rule Check class: [f52f242](https://gitlab.com/doituself/sonarqube_java_custom_plugin_demo/commit/f52f242abcff7f737043daa983ec7c7cb1f3c574)
  - [X] extends BaseTreeVisitor implements JavaFileScanner
  - [X] implement scanFile method
  - [X] Add visitLiteral() method
  - [X] Add check logic
  - [X] Report Issue
  
## Maven Dependencies

pom.xml: 

    <groupId>sonarqube.java.custom.plugin</groupId>
    <artifactId>demo</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <sonar.version>7.5</sonar.version>
        <sonarjava.version>5.9.2.16552</sonarjava.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.sonarsource.sonarqube</groupId>
            <artifactId>sonar-plugin-api</artifactId>
            <version>${sonar.version}</version>
            <scope>provided</scope>
            <exclusions>
                <!-- <exclusion>
                    <groupId>com.google.collections</groupId>
                    <artifactId>google-collections</artifactId>
                </exclusion> -->
            </exclusions>
        </dependency>

        <dependency>
            <groupId>org.sonarsource.java</groupId>
            <artifactId>sonar-java-plugin</artifactId>
            <version>${sonarjava.version}</version>
            <scope>compile</scope>
            <!-- <exclusions>
            <exclusion>
                <groupId>org.sonarsource.java</groupId>
                <artifactId>java-frontend</artifactId>
            </exclusion> -->

            <!--    </exclusions>-->
        </dependency>
    </dependencies>

we need the sonarQube Server version and the Sonar Java Plugin version, be sure put the same version number as they are in your sonarQube server environment. You can find the version number for Java plugin under sonarqube\extensions\plugin folder.


## Create Rule Check

In this section, we start to create the Rule Check class, aiming to scan the eligible .java files and find out strings that meet a certain pattern.

> Find any string values that meets the following patterns:
> 
        "[0-9|\\W]+",
        "\\d+",
> more patterns might be added later on.

### Pre-word

Before we start creating the rule class, firstly clarify some basics. 

There are two ways to develop a Java rule:

- extends IssuableSubscriptionVisitor class, the latter extends SubscriptionVisitor class

> This visitor offers an easy approach to writing quick and simple rules, because it allows us to narrow the focus of our rule to a given set of Kinds to visit by subscribing to them.

this visitor is actually encapsulating more, and you may find it not easy to customize vistis to some tree nodes.

- extends BaseTreeVisitor class
  
org.sonar.plugins.java.api.tree.BaseTreeVisitor. The BaseTreeVisitor contains a visit() method dedicated for each and every kind of the syntax tree, and is particularly useful when the visit of a file has to be fine tuned.

The good thing of this vistor is, it categorizes the visits of all kinds of Trees, in the runtime, when it scans a particular kind of tree, it will automatically go to its specific visit method. What you need to do is simply putting your detailed code logic in that visit method. That's it.

We will use the second way : extends BaseTreeVisitor in this demo.

### Start: create rule class

Now we **create a new java class**, and call it StringMatcherCheck

```
import org.sonar.plugins.java.api.JavaFileScanner;
import org.sonar.plugins.java.api.JavaFileScannerContext;
import org.sonar.plugins.java.api.tree.BaseTreeVisitor;

public class StringMatcherCheck extends BaseTreeVisitor implements JavaFileScanner{

}
```
**implement one of required method: scanFile**

```
    private JavaFileScannerContext context;

    @Override
    public void scanFile(JavaFileScannerContext context) {
        this.context = context;
        List<Tree> trees = context.getTree().types();
        if (!trees.isEmpty()) {
            scan(trees);
        }
    }
```

when the eligible .java file is being scanned, it will firstly get all its tree types, and then scan each tree line by line.

Now it comes to our core logic.

What we will check is String types of tree, its formal name is something like StringLiteralTree, if you go to BaseTreeVisitor class or its iterface TreeVisitor, you will find a visitLiteral method, override it in your StringMatcherCheck class:

**Override visitLiteral method:**

```
 @Override
    public void visitLiteral(LiteralTree tree){

    }
```

**put scan logic there**, let's try a simple one:

```
@Override
    public void visitLiteral(LiteralTree tree){
        String treeValue = tree.value();
        boolean isStringMatched = treeValue.matches("[0-9|\\W]+");
    }
```

as per our requirement, if matches found, we assume it's a potential issue, next we will need to report it. 

**report issue:**

  if (isStringMatched){
            context.reportIssue(this, tree, "Found string matched: " + treeValue);
  }

you can find the reportIssue method in JavaFileScannerContext class. 

```
void reportIssue(JavaCheck var1, Tree var2, String var3);
```

once this is done, the issue reported will be displayed on SonarQube UI, you don't need to worry about any other things.      

## Reference

- [Writing Custom Java Rules 101 - Plugins - Doc SonarQube](https://docs.sonarqube.org/display/PLUG/Writing+Custom+Java+Rules+101)