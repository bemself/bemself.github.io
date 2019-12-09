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
description: 静态代码扫描系列 - Create Custom Java Plugin (1), 介绍一些术语
---

# SonarQube: Create Custom Java Plugin (1)

## Basic Terms

Before we start, it would be a good idea to understand some basic terms of SonarQube.

- **plugin**: this is the final product you will develop, it's packaged into jar, and you put in sonarqube extension list, then it will work as you expect 

one plugin can contain multiple profiles.

- **Profile**: this is a group of rules. To make your custom rule work, be sure to put it into a java profile. One profile can contain multiple rules. In the runtime, SonarQube get all the rules in the specified profile, and apply the rule logic for all eligible files one by one.

one profile can contain multiple rules.

- **Rule**: this is where your code scan logic is held in your plugin. It does your main job.

for example, if you want to check if the .java file is containing some specific strings, put the scan logic in a rule.

Rule implements interface JavaFileScanner, so you can see, in the runtime, your plugin will scan each eligible file by this custom rule. 

- **Sensor**: this is where the rule check is invoked.

you can also use Sensor to do some jobs before or after the rule check.

e.g. passing some config settings to rule, or export issues after rule is done.

## Reference

- [Writing Custom Java Rules 101 - Plugins - Doc SonarQube](https://docs.sonarqube.org/display/PLUG/Writing+Custom+Java+Rules+101)