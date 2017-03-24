## Learn Git ##

安装后自报家门：

```git
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```

`git config`和`--global`用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置

```
$ mkdir FolderName
$ cd FolderName
$ pwd
/Users/michael/FolderName
```
通过`git init`命令把这个目录变成Git可以管理的仓库

```
$ git add Example.txt
```

用命令`git commit`告诉Git，把文件提交到仓库：

```
$ git commit -m "example"
```

`git status`命令可以让我们时刻掌握仓库当前的状态

`git diff`顾名思义就是查看difference，显示的格式正是Unix通用的diff格式

`git log`命令显示从最近到最远的提交日志，如果嫌输出信息太多，看得眼花缭乱的，可以试试加上`--pretty=oneline`参数

Git必须知道当前版本是哪个版本，在Git中，用`HEAD`表示当前版本，上一个版本就是`HEAD^`，上上一个版本就是`HEAD^^`，当然往上100个版本写100个`^`比较容易数不过来，所以写成`HEAD~100`，使用`git reset`命令

只要上面的命令行窗口还没有被关掉，你就可以顺着往上找啊找啊，找到那个`append GPL`的`commit id`是`3628164...`，于是就可以指定回到未来的某个版本

Git提供了一个命令`git reflog`用来记录你的每一次命令，可以找到 commit ID

![2017-03-19 1547 19](D:\桌面\2017-03-19 1547 19.jpg)

命令`git checkout -- readme.txt`意思就是，把`readme.txt`文件在工作区的修改全部撤销，这里有两种情况：

一种是`readme.txt`自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；

一种是`readme.txt`已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

总之，就是让这个文件回到最近一次`git commit`或`git add`时的状态。

用命令`git reset HEAD file`可以把暂存区的修改撤销掉（unstage），重新放回工作区。`git reset`命令既可以回退版本，也可以把暂存区的修改回退到工作区。当我们用`HEAD`时，表示最新的版本

你通常直接在文件管理器中把没用的文件删了，或者用`rm`命令删了

Git知道你删除了文件，因此，工作区和版本库就不一致了，`git status`命令会立刻告诉你哪些文件被删除了

现在你有两个选择，一是确实要从版本库中删除该文件，那就用命令`git rm`删掉，并且`git commit`

`git checkout`其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”

关联后，使用命令`git push -u origin master`第一次推送master分支的所有内容

从现在起，只要本地作了提交，就可以通过命令：

```
$ git push origin master
```

要克隆一个仓库，首先必须知道仓库的地址，然后使用`git clone`命令克隆。

Git支持多种协议，包括`https`，但通过`ssh`支持的原生`git`协议速度最快

`git checkout`命令加上`-b`参数表示创建并切换

`git merge`命令用于合并指定分支到当前分支

查看分支：`git branch`

创建分支：`git branch <name>`

切换分支：`git checkout <name>`

创建+切换分支：`git checkout -b <name>`

合并某分支到当前分支：`git merge <name>`

删除分支：`git branch -d <name>`

当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。

用`git log --graph`命令可以看到分支合并图。



