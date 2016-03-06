# [0v0.link](http://0v0.link)

嘛，个人博客而已咯。

## 技术栈

- Apache(with mod_wsgi)
- Django(with SQLite)
- markdown.js
- GitHub Webhook
- 七牛云

## 已完成

前端部分：

- 导航栏
- Info Card
- 通过目录/Tag过滤文章
- 文章 TOC （客户端 JS 动态生成）
- 使用 markdown.js 渲染 md
- 文章图片标题（客户端 JS 动态生成，提取alt属性）

Django 后台部分：

- 任意级目录管理文章
- Tag 管理文章
- 文章修改记录
- 任意级评论
- 多作者支持

其他部分：

- 使用 Apache
- 使用 七牛云 CND 加速静态文件
- Github Webhook 自动部署

## 想到啥写啥的 TODO List

- 网站 icon
- GZip 压缩
- About 页面
- 站内搜索
- 评论
- RSS
- 前端美化
- 移动版
- 纯 CSS --> SASS + autoprefixer
- Django Admin --> 自己写后台
- 多作者支持
- API
- Android 客户端
- SEO
- deploy.sh 脚本重构

## 秘密

- 作为初学者，我不想被跨浏览器兼容的一些东西弄得太过迷糊，CSS 里能不写前缀的我都没写，也没做任何 IE 兼容测试，只在最新版 Chrome 和 Firefox 里测试了。
- 访问我博客的时候可能会出现各种各样的情况，因为这个项目估计最近我会更新的很勤快…………

## 部署？你确定？

**这不是个reuseable app！**，但是确实是有一些快速部署支持的，deploy.sh 和 deploy 文件夹就是干这个用的。

如果你想部署在自己的服务器上的话，基本上要以下，额……好多步：

- fork
- 安装 Python3，pip3，virtualenv，
- sudo apt-get install apache2 libapache2-mod-wsgi-py3
- clone 你的 repo
- 在 clone 出的目录旁建立一个 Python virtual env，名字自己定
- 在 env 里安装 django, pytz, django-gravatar2
- 把 depoly.sh 里 PYENV 变量里的 env-0v0.link 改成你的 env 名字
- 把 deploy/apache.conf.template 和 zvz/setting.py 里的 0v0.link 改成你的域名
- 把 zvz/setting.py 里的 Arbutus 改成你服务器的 hostname
- 按照你的个人信息编辑 blog/apps.py 里的 blog_settings 变量
- 运行 deploy.sh，然后祈祷它别出错。
- 访问你的域名(eg. example.com)，看看是不是正常
- 在 Github 上为 repo 添加 Webhook
- 访问 Django Admin (eg example.com/admin)，添加一项 GithubHookSecret 值为你的 Webhook Secret
- 搞定了~ 然后你往 repo 的 master 分支 push 代码的话，服务端就会自动更新。


## 感悟

2016.03.01 基本翻译完 Django 文档的教程部分（见[Django-intro-zh](https://github.com/7sDream/django-intro-zh)）之后，正式开始学着用 Django，顺便补一下我前端方面知识的不足（其实就是没有）。

一边看文档一边 Chrome F12 学前端……这几天算是对 Web 端多了些了解吧。

回想了一下最近几天学了这么多东西真是相当充实，Django 差不多算入门把，然后从 HTML CSS JS 这三个点都不会的渣渣，变得至少会一点了。

还学了好多其他知识，比如 Apache 配置文件，数据库并发，Linux 脚本，用户管理，Github Webhook。

顺便踩了一大堆坑，比如权限坑，CSRF坑，Apache www-data 用户组，Django 的 Bug。

当然，生命不息，学zhe习teng不止，这个项目应该会陪我很久吧。
