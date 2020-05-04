---
title:  python 测试之 pytest flask app 初探
date:  2020-05-02 21:01:18
edit:  2020-05-02 21:01:05
layout: post
status: Writing
categories:
  - Python
tags:
  - Python
description:  用 pytest 测试 flask api service
---

# 背景

使用 pytest 测试 flask api service

# 框架之选择

为什么选 pytest? 并没有特别原因, 只是刚好看到有个 pytest-flask package, 就先试试了, 用起来还好, 就记录一下.

框架中用到了 fixture, 就是在实际测试的前后加入 setup, teardown 等操作, 是测试必备之选.

测试的几大要素就不多说了.

# 直接上步骤

安装: `pip install pytest-flask`

目录结构:
    
```
- module1
    - __init__.py
    - src
        - __init__.py
        - app.py
        - config.py
    - test
        - __init__.py
        - conftest.py
        - pytest.ini
        - test_f1.py
```

## 创建 flask api service

参考 [Application Setup — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/)

- 用工厂模式, 在 __init__.py 中创建 create_app 方法
- 在 app.py 中导入: `from src.app import create_app`

src/__init__.py:

```py
import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_pyfile(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

```

app.py:

```
from . import create_app
app = create_app()
```

## 测试 api service

在 conftest.py 中创建 fixture: `@pytest.fixture`

```py
import os
import tempfile
import pytest
from src.app import create_app

@pytest.fixture
def client():
    flask_app = create_app() 
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    client = flask_app.test_client()
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
    yield client  # this is where the testing happens!
    ctx.pop()
```

在 test_f1.py 中:

```py
import os
def test_f1(client, capsys):
    '''Test f1
    '''
    res = client.get('/hello')
    captured = capsys.readouterr()
    assert 'error' not in captured.err
    assert b'Hello, World!' in res.data
```

## 测试范围

有些 test 如果想 ignore 怎么办?

在 conftest.py 中添加:
```py
collect_ignore = [
    "test_f1.py"
    ]
```

当运行 pytest 的时候, "test_f1.py"就不会在 collected 列表中了.

参考: [Changing standard (Python) test discovery — pytest documentation](https://docs.pytest.org/en/latest/example/pythoncollection.html)

# Tutorials
- [Welcome to pytest-flask’s documentation! — pytest-flask 0.10.0 documentation](https://pytest-flask.readthedocs.io/en/latest/)
- [Python Web Applications With Flask – Part III – Real Python](https://realpython.com/python-web-applications-with-flask-part-iii/#the-tests)
- [Testing a Flask Application using pytest – Patrick's Software Blog](https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/)
- [Testing Flask Applications — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/testing/)
- [How to Test a Flask Application](https://www.damyanon.net/post/flask-series-testing/)
- [pytest fixtures: explicit, modular, scalable — pytest documentation](https://docs.pytest.org/en/latest/fixture.html)


- [Quickstart — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/quickstart/#redirects-and-errors)
- [the Flask API document for flask.url_for()](http://flask.pocoo.org/docs/api/#flask.url_for)

# ChangLog
- 2020-05-03 init

