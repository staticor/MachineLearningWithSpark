# MachineLearningWithSpark

Book Note: <Spark机器学习> - Nick Pentreath

环境介绍, mac osx 10.12.6

Spark版本 2.2.0, Prebuild Hadoop
Scala版本 2.12.3


项目流程, 使用sbt编译/Package, 用Standalone的方式提交jar文件. 显示结果.


build.sbt示例:

```shell
name := "Simple project1"

version := "1.0"

scalaVersion := "2.11.8"

libraryDependencies += "org.apache.spark" %% "spark-core" % "2.1.0"

```

关于书的版本, 中文版本 2015年9月.

而目前英文版的第二版已经Publish了, 笔者在Safari BooksOnline上可以看到, 如果您没有用过, 也能在有限的几天试用期内进行阅读, 图书链接为
[https://www.safaribooksonline.com/library/view/machine-learning-with/9781785889936/4fd4690a-eb63-4f69-b0b3-67b9803a81c4.xhtml](https://www.safaribooksonline.com/library/view/machine-learning-with/9781785889936/4fd4690a-eb63-4f69-b0b3-67b9803a81c4.xhtml)

Github Repo of 2nd - Edition example code
https://github.com/staticor/Machine-Learning-with-Spark-Second-Edition



本项目简介:

project1 是第二章 Scala App, 实现了csv的简单描述统计, 包括: count, sum (distinct), count keys top one element.
     其中 App结果通过SBT完成package, 然后用 spark-submit 来提交 jar 文件.

project2 用到了公开数据源 movieLens, 由于使用到了 IPYTHON的方式, 因此这里只留存一个 chapter3.py 文件.
