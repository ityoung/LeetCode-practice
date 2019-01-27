## 描述

- 使用Python3
- 解一道LeetCode题
- 使用TDD(Test Driven Development, 测试驱动开发)模式

## 题

Title: 3. 无重复字符的最长子串
Link: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
Description: 
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
     
> 使用官方解题的方法一: 暴力解法

## 工具

- pytest
- when-changed

### pytest

Python 第三方测试框架, 功能丰富

本次涉及知识:
1. 执行
2. 参数化测试用例

安装pytest:

```bash
pip install pytest
```

### when-changed

监控文件变化时执行脚本

安装:

```bash
pip install when-changed
```

写一个监控脚本`auto-runtest.sh`:

```bash
#!/bin/bash

when-changed -v -r -1 -s ./ "py.test -s $1"

```

添加执行权限:

```bash
chmod +x auto-runtest.sh 
```

运行:

```bash
./auto-runtest.sh p3-longest-substring-without-repeating-characters.py 
```

运行之后监控开始, 只要文件改变, 就会自动执行一下pytest

## 过程详解

1. 创建解题过程的方法/类
2. 创建测试方法/类
3. 测试用例分析, 写成测试代码
4. 创建文件变化监控, 当python文件变化时, 自动执行pytest

### 测试用例分析

在官方给的示例基础上, 添加几个用例:

输入: "abcabcbb"
输出: 3 

输入: "bbbbb"
输出: 1

输入: "pwwkew"
输出: 3

输入: ""
输出: 0

输入: "a"
输出: 1