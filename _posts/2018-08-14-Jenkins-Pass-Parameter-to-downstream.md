---
title: Jenkins - pass parameters to downstream
edit: 2018-08-10
layout: post
categories:
- Python
tags:
- Python
description: Jenkins持续集成。After Jenkins is upgraded from 1.0 to 2.0, our master job stops to pass parameter values to its downstream jobs. Here is to solve this problem
---

# Background

After Jenkins is upgraded from 1.0 to 2.0, our master job stops to pass parameter values to its downstream jobs.

When in Jenkins 1.0, we have a master-slave job definitions, where a BUILD_PATH parameter is defined in master job, and its value will be passed directly to the slaves at runtime. On the slave machines, no additional work is needed except referencing it in the build steps, e.g. %BUILD_PATH % a windows batch command step.

But this stopped working in Jenkins 2.0

# Analysis

In Jenkins 2.0, with [Parameterized Trigger](https://wiki.jenkins.io/display/JENKINS/Parameterized+Trigger+Plugin) plugin, when you want to pass a parameter to downstream,

> ***\** YOU MUST DEFINE THE PARAMETER IN DOWNSTREAM JOBS VIA  "This project is parameterized". For example, if job1 passes ABC=123 to job2 then in job2 mark the job as "This project is parameterized" and "Add Parameter" named "ABC". *****

So modification is needed on the downstream jobs as well.

# Solution

Two places to take care and be modified:

- On the master job, 
  - define the parameter in the Parameterized section
  - Add "Current Build Parameter" in the Trigger Build Step section
- On the slave job, add a parameter with the same name as the one on master job

Now it should ok to go.

