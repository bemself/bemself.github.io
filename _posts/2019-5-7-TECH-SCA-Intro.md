---
title: Static Code Analysis Searies - Introduction
date: 2019-05-07
edit: 2019-07-04
layout: post
categories:
  - Java
  - Static Code Analysis
tags:
  - Java
  - SCA
description: 静态代码扫描系列, 此为 SonarQube 之初介绍. 
---

## Background

Looking for a tool to do some source code analysis on Java projects, and possibly other language projects like Javascript, html etc.

## Static Code Analysis

	[Static Code Analysis](https://en.wikipedia.org/wiki/Static_code_analysis_

### Why

We all know about Code Reviews.

As a developer:

- you are assigned with a requirement
- you analyze it and finish desining
- then coding done
- next, you'd like to commit the changes
- but, before that, you have to ask someone (e.g. your manager) to review it
- review is done, ok you can push your code.

What's the difference here, between code review and static code analysis?

basically it might be:

- Code Review is a **manual** process, normally done by a more **experienced person**, 
	- it involves a dynamic process
	- in the code reviewer's brain, it is executed and verified against the actual requirement
	- well it could be static only, that all depends on the code reviewer

- Static Code Analysis is an auto process, normally done by a **machine**
	- as its name implies, it's mainly static, 
		- no execution
		- no idea of actual requirement

As an auto process, it surely does things quicker or not-imaginable than a manual process, that's why it stands.

Well actually it's not easy to differeniate them, as they both play an important role in ensuring better proram quality. 

	- The focus/emphasis differs

### What

In one word, static code analysis is :

- analyze the source code without executing it

Analyze What?:

- Coding standard violations
- Programming errors
	- control flows
	- data flows
	- interfaces
	- ...
- security vulnerabilities
- customize as needed
- metircs

### Where

most of SCA tools integrates with IDEs like Intellij, Eclipse etc.

As well as:

- DevOps: Jenkins etc
- CLI: sonarqube scanner
- UI rendering (reports)

### When

	Static code analysis is performed early in development, before software testing begins. For organizations practicing DevOps, static code analysis takes place during the “Create” phase. 

 here it comes with another comparation: 

 - static code anlysis vs dynamic anlysis

 basic difference is that:

 - static code anlysis :
 	- happens **before** software runs
	 	- early in development 
	 	- before software testing begins
 - dynamic analysis:
	- happens **after** software runs 
	 	- e.g. unit testing
	 	- integration testing
	 	- system testing

### Who

	[List of Tools](http://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis)

	[Topic: static-code-analysis](https://github.com/topics/static-code-analysis)

As said, static code analysis is done by machine.

however its output result is reviewed by developers.

There are a lot of existing tools, for different program languages.

These tools also integrates with IDEs for developers' convenience.

From manager point of view, an integrated dashboard portal is welcome, SonarQube is one of the popular one.

- [Continuous Inspection | SonarQube](https://www.sonarqube.org/)
	- is Open Source
	- Supports multiple languages, dashboard reporting, customization for second development

After some investigation, Sonarqube seems to be a good choice for Existing Tool with Second Development, reasons are as below:

1. It's an open source tool, dedicated to code inspection for java and other languages
	- [Continuous Inspection | SonarQube](https://www.sonarqube.org/)
	- [GitHub - SonarSource/sonarqube: Continuous Inspection](https://github.com/SonarSource/sonarqube)

2. there is specific sonarqube java project
	- [GitHub - SonarSource/sonar-java: SonarJava : Java static analyzer for SonarQube & SonarLint](file:///C:/Users/AppData/Roaming/Mozilla/Firefox/Profiles/9myqpgnw.default/ScrapBook/data/20190115224759/index.html)

3. Dashboard Report

4. Multiple Projects and Multiple programming languages supported

5. Integrate with Jenkins:

	- [Analyzing with SonarQube Scanner for Jenkins](file:///C:/Users//AppData/Roaming/Mozilla/Firefox/Profiles/9myqpgnw.default/ScrapBook/data/20190116111215/index.html)
	- [Jenkins Plugins](https://plugins.jenkins.io/sonar)

6. For extensibility, as Javascript would be the next one to inspect, Sonarqube supports JS as well as other languages e.g. c#

7. If you don't find an existing rule that meet your needs, you are welcome to develop a custom plugin.

- There are also some Commercial Tools like
[Market-Leading i18n Software | Lingoport Suite](file:///C:/Users/AppData/Roaming/Mozilla/Firefox/Profiles/9myqpgnw.default/ScrapBook/data/20190115213716/index.html)
	- It's dedicated to I18n check and has a dashboard for reporting and management
	- Its dasboard shows much like a second development based on the below open source tool: SonarQube

### How

Normally a code analysis follows:

- Lexical analyzer： Strin -> Tokens series。
- Syntactic analyzer: Tokens series -> Syntax Tree
- Contextual analysis: semantics etc

specifically from **Words** 、**Syntax**、**Context** to parse the expressions

## Limitations

	Machine differs from human

SCA cannot tell:
	- whether it does as the requirement expects
	- whether it does as the developer expects

	this will sure leads to false positives or false negatives

it might also slows down the performance:
	- esp when you enables it in IDE
		- as it does the analysis before compiling your code

even it might report issues differently from different Tools.
	- the rules defined might differ among tools 

however all the limitations doesn't stop SCA from being a good helper.

## Reference

- [What Is Static Analysis (Static Code Analysis)? | Perforce](https://www.perforce.com/blog/qac/what-static-code-analysis)
- [How Static Code Analysis Works — Plus Static Analysis Example | Perforce](https://www.perforce.com/blog/qac/how-static-code-analysis-works)
- [False Positives and False Negatives (Plus Examples) in Static Analysis | Perforce](https://www.perforce.com/blog/qac/what-are-false-positives-and-false-negatives-plus-examples)