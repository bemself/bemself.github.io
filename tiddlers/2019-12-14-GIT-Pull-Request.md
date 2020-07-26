
# 背景

最近参加了一个开源项目, 第一次公开提 Pull Request, 从 Github 网页直接操作, 先是认真看了下别人的, 简单了解了下 Pull Request, 成功后挺开心的, 原来也不难, 但后来就陆续遇到了问题, 比如如果别人 reivew 后要你再改点啥怎么办? 以及这个 PR 没关, 我还想做点别的不相干的啥怎么办? 这些以前我都没有思考过~

现在能顺利的提 PR 了, 回顾记录一下;

## 问题重现

- PR review的结果需要做相应修改

一度不知道要如何提交修改, 其实只要继续在当前PR的分支下操作提交就好了

- 我在master分支上提 PR

直接导致PR未关之前, 我在master上做的改动, 全部列在这个PR下面了...

幸好发现的及时, 赶紧将 PR 设为 Working In Progress, 手忙脚乱的修复. (期间不得不面对以前一直逃避的 git revert, git reset...)

衍生的一堆问题:

- 怎么删已提交的 commit
- 怎么删分支
- 如果merge分支
- 怎么查某个文件的历史
- 如何sync origin 和 upstream 仓库
- ...

## 在 Forked 仓库中提交 Pull Request

一番摸索之后, 列一下自己现在觉得该这样操作:

### Fork 远程仓库
> 不用细说

拉取到本地后, 你的 Forked 仓库成了 Origin

再把远程的被你Forked的upstream仓库加进来:

```
git remote add upstream <your forked repo's upstream>
```

现在你的 `git remote -v` 应该有两个了, origin 和 upstream

当然别忘了把 upstream 的最新内容拉下来:
 ```
 git fetch upstream
 git checkout master
 git merge upstream/master
 git pu origin master
 ```

现在你的forked仓库和它的upstream仓库是同步了.

### 开发之前, 先开个新分支啊啊啊, 这个是最重要的了
  
这就是所谓的[分支开发流](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)

这个词听来好久了, 却一直没有想到用, 直至现在被迫用上, 然后发觉还挺好用.

```
git checkout -b new-branch upstream/master
<make your changes>
git ci -m "your new changes"
git pu origin new-branch
```

### 现在可以去 Github上提 Pull Request拉
> 网页操作

记着选择新建的分支即可

这个分支就不要再做其他无关的事情了.

### 如果 PR Reviewer 要你做点改动呢

因为你现在是在干净的分支上, 放心大胆的改后正常提交就好了:

```
git checkout new-branch
<改代码>
git add .
git ci -m "新改动"
git pu origin new-branch
```

### PR approve and merge 后, 可以删除你的这个new-branch了

参考: [2019-12-08-GIT-remove-branch.md](GIT-remove-branch.html)

## 思考

- 在用中学

## ChangeLog
- 2019-12-14 init