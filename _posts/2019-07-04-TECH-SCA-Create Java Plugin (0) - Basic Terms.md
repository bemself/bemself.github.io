---
title: Static Code Analysis Searies - Introduction
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
description: 静态代码扫描系列 - Create Custom Java Plugin (0), 介绍背景以及开发一览
---

# SonarQube: Create Custom Java Plugin (0)

## Background

SonarQube Java Analyzer offers hunderds of existing rules, but you still might not able to find one specific to your company's need. In this case, you can develop a new custom plugin, relying on SonarQube Java Plugin API.

SonarQube provides template projects to guide you on creating new rule, to save time, you can go to [java-custom-rules](https://github.com/SonarSource/sonar-custom-rules-examples/tree/master/java-custom-rules) and start.

Here, we will start from scratch and detail the steps to go.

## Requirement:

> Find any string values that meets the following patterns:
> 
        "[0-9|\\W]+",
        "\\d+",
> more patterns might be added later on.
> Export the issues found in xml format after the scan

## Develop Custom Plugin

Assume that you know how to create a maven project. Before start, do that please.

- [X] Configuration
- [X] [Rule Check](2019-07-04-TECH-SCA-Create Custom Java Plugin (2) - Develop Rule Check.md): 
- [X] Sensor (Pre)
  - [X] Read/Set Config Params
- [X] Sensor (Post)
  - [X] Export Issues
- [ ] Rule Definition
- [ ] Plugin
  - [ ] Register
    - [ ]  Rule Checks
    - [ ]  Sensor
    - [ ]  Rule Definitions
- [ ] Unit Test
- [ ] Run plugin
  - [ ] Add .jar to SonarQube Extension, restart server
  - [ ] Set SonarQube Properties
  - [ ] SonarQube UI Setup
    - [ ] Create Project
    - [ ] Create Profile (this can also be done from Code, here we do it manually)
    - [ ] Add rule to profile
    - [ ] Add project to profile
  - [ ] Run from Sonar-Scanner
  - [ ] Run from Maven
- [ ] Reporting
  - [ ] Check Issues

## Reference

- [Writing Custom Java Rules 101 - Plugins - Doc SonarQube](https://docs.sonarqube.org/display/PLUG/Writing+Custom+Java+Rules+101)