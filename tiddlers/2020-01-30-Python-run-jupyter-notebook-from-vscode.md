
# 背景

Jupyter Notebook 很好用，但是要在浏览器中用，个人很不喜欢在浏览器上操作。平常编辑和跑 python 代码都是在 vscode 中，用的挺爽的。

喜闻 VSCode 支持 Jupyter Notebook 了，便立即安装了。只是过程中遇到点问题，所以记录一下。

# 在 vscode 中安装配置 jupyter

参考：[Working with Jupyter Notebooks in Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support)

我是直接在 Vscode Extensions 里面找到 "Jupyter" 安装的。

`command + shift + P` 选择 `新建 jupyter notebook` 即可。

建好后，直接像在浏览器中操作一样，运行修改。

# 遇到的问题

- `Error: Activating Python 3.7.0 64-bit ('general': venv) to run Jupyter failed with Error: StdErr from ShellExec, pyenv: activate: command not found`

我是在 `pyenv` 环境中运行 cell 的时候遇到此问题，参考 
[pyenv + virtualenv not working - use pyenv activate for all · Issue #4013 · microsoft/vscode-python](https://github.com/microsoft/vscode-python/issues/4013)提示的解决方案，成功解决：

在 vscode settings 文件中的 `settings` 部分 加入： `"python.terminal.activateEnvironment": false`，无需重启 vscode 即可。

- `Error: Jupyter cannot be started. Error attempting to locate jupyter: Error: Module 'notebook' not installed.`

vscode 用这命令来找 notebook: `python -m jupyter notebook --version`

在我的 `pyenv` 环境中： `pip install notebook`

## ChangeLog
- 2020-01-30 init