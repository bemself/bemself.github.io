---
title:  Python Logging 日志输出到文件
date:  2020-05-03 21:01:18
edit:  2020-05-03 21:01:05
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  使用日志配置文件, 输出 log 到文件
---

# 背景

了解如何使用 python logging, 输出日志到文件中. 

并初步结合 flask 框架以及多模块的环境配置, 尚不太成熟, 待改进

至于为什么要用 logging, 而不是之前的 print, 原因也简单, logging 的信息量更大, 如果输出到文件中也更方便.

# Python Logging 碎碎念之配置文件

python 有自带的 logging 模块, 足够用了, 也挺好用.

用前先想想:

- 要能兼顾所有模块
- 要有时间戳
- 要方便配置, 比如更改 log文件名, log level 等
    - 文件名不写死在代码中...
- ...

自然需要外置 conf 配置文件.

当然, 外置 conf 文件虽然配置起来方便, 但要在代码中操控它就有点麻烦, 不过从用户角度看, 这个还是首选. 具体的 pro 和 cons 请参考[Logging — The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/logging/)

那:

- conf 文件格式有什么要求?
- conf 文件内容怎么写?
- conf 文件怎么读?

文件格式一般有几种:

- ini 文件: 类似 key=value
- yml 文件
- json 文件

对他们的解析不一样, 读取的时候用到的模块:

- ini 文件: `logging.config.fileConfg`
- yml/json 文件: `logging.config.dictConfig`

示例见下节

文件内容怎么写?  

一般比较重要的得包含:

- level: debug/info/warn...
- handlers
    - file handler
        - file name: 比如带时间戳等
    - console handler
- formatters
    - file formatter
    - console formatter

简单的示例如下, 详细示例请见文末的附录

```
[logger_root]
level=DEBUG
handlers=fileHandler

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=logFormatter
args=("_log/" + time.strftime("%%Y%%m%%d%%H%%M%%S")+'.log', 'a')

[formatter_logFormatter]
format=%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s
```

# 在代码中加载 log 配置文件

加载 yml/json 文件:

```py
import logging
import logging.config.dictConfig(yaml.load(open('logging.yml', Loader=yaml.FullLoader))))
```

加载 .ini 文件

```py
import logging
logging.config.fileConfig("logging.ini")
```

# 在模块中使用就很简单了, 

```py
logger = logging.getLogger(__name__)
logger.debug("log %s", it)
```

当然这只是很简单的场景, 实际应用中会需要用到 filter, 更改文件名, 获取 log 文件名等等

比如, 我想在程序运行结束的时候把 log 文件地址也输出到 log 文件中, 然而却发现有点难度, 试了几种方法, 只成功了下面这个:

```py
LOG_FILE = logging.getLoggerClass().root.handlers[0].baseFilename
logger = logging.getLogger(__name__)
logger.debug(f"LOG_FILE: , {LOG_FILE}")
```

未成功之一: 我拿到的 handlers list 总是为空...

```py
import logging
dir(logging.FileHandler)
>>> handler = job_logger.handlers[0]
>>> filename = handler.baseFilename
>>> print(filename)
'/tmp/test_logging_file'
```

# 还想输出 exception details

先在需要处理 exception 的地方 raise exception

```
raise Exception(msg)
```

然后, catch 的时候输出到 log 中

```py
import traceback
except Exception as e:
    msg = traceback.from_exec()
    logger.debug(msg)
```

注意, 这里的 form_exec() 是不带参数的

我之前忽略了, 想当然的加了 e 作为参数, 结果错误: `'>=' not supported between instances of 'Exception' and 'int'`

# Flask Logging

如果代码中用到了 flask 框架, 如何输出 log 呢?

同样, 重用前面的 log 配置, 在 app.py 中直接用 app.logger 即可, 底层用的还是 python logging 模块

```
app = create_app()
logger = app.logger
```

# Reference

## Python logging
- [logging — Logging facility for Python — Python 3.8.3rc1 documentation](https://docs.python.org/3/library/logging.html)
- [Logging — The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/logging/)

## flask logging
[Logging — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/logging/)

# 附录: 大致的目录结构

log 配置文件的读取是在 module2/__init__.py 中;

```py
import os
import logging
from logging.config import fileConfig

if not os.path.exists("_log"):
    os.mkdir("_log")
logging.config.fileConfig("logging.conf"))
LOG_FILE = logging.getLoggerClass().root.handlers[0].baseFilename
logger = logging.getLogger(__name__)
logger.debug(f"LOG_FILE: , {LOG_FILE}")
```

main.py 启动 flask app

.root
├── logging.conf
├── logging.yml
├── main.py
├── README.md
├── _log
            └── 20200503204102.log
├── module1
            ├── __init__.py
            ├── requirements.txt
            ├── src
            │   ├── __init__.py
            │   └── app.py
            └── test
└── module2
            ├── __init__.py
            ├── src
                        ├── __init__.py
            └── test
                        ├── __init__.py
            ├── requirements.txt
            ├── README.md
            ├── data
            ├── docs
            ├── invoke.yml

# 附录: logging.ini sample (摘自网络),

因为带了注释, 所以摘录在此供参考:

如需 yml 文件, 可参考[python - Flask logging - Cannot get it to write to a file - Stack Overflow](https://stackoverflow.com/questions/17743019/flask-logging-cannot-get-it-to-write-to-a-file)

```ini
#These are the loggers that are available from the code
#Each logger requires a handler, but can have more than one
[loggers]
keys=root,Admin_Client

#Each handler requires a single formatter
[handlers]
keys=fileHandler, consoleHandler

[formatters]
keys=logFormatter, consoleFormatter

[logger_root]
level=DEBUG
handlers=fileHandler

[logger_Admin_Client]
level=DEBUG
handlers=fileHandler, consoleHandler
qualname=Admin_Client
#propagate=0 Does not pass messages to ancestor loggers(root)
propagate=0

# Do not use a console logger when running scripts from a bat file without a console
# because it hangs!
[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=consoleFormatter
args=(sys.stdout,)# The comma is correct, because the parser is looking for args

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=logFormatter
# This causes a new file to be created for each script
# Change time.strftime("%Y%m%d%H%M%S") to time.strftime("%Y%m%d")
# And only one log per day will be created. All messages will be amended to it.
args=("_log/" + time.strftime("%%Y%%m%%d%%H%%M%%S")+'.log', 'a')

[formatter_logFormatter]
#name is the name of the logger root or Admin_Client
#levelname is the log message level debug, warn, ect 
#lineno is the line number from where the call to log is made
#04d is simple formatting to ensure there are four numeric places with leading zeros
#4s would work as well, but would simply pad the string with leading spaces, right justify
#-4s would work as well, but would simply pad the string with trailing spaces, left justify
#filename is the file name from where the call to log is made
#funcName is the method name from where the call to log is made
#format=%(asctime)s | %(lineno)d | %(message)s
#format=%(asctime)s | %(name)s | %(levelname)s | %(message)s
#format=%(asctime)s | %(name)s | %(module)s-%(lineno) | %(levelname)s | %(message)s
#format=%(asctime)s | %(name)s | %(module)s-%(lineno)04d | %(levelname)s | %(message)s
#format=%(asctime)s | %(name)s | %(module)s-%(lineno)4s | %(levelname)-8s | %(message)s
format=%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s

#Use a separate formatter for the console if you want
[formatter_consoleFormatter]
format=%(asctime)s | %(levelname)-8s | %(filename)s-%(funcName)s-%(lineno)04d | %(message)s
```

# ChangeLog
- 2020-05-03 init