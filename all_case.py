#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-10 16:34
import unittest
import HTMLTestRunner
import time

# 取test_case文件夹下所有用例文件
def creatsuitel(lists):
    testunit = unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(lists, pattern='start_*.py', top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit
list_1 = 'test_case'
alltestnames = creatsuitel(list_1)

#取前面时间加入到测试报告文件名中
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
filename = "report\\"+now+'result.html' #定义个报告存放路径，支持相对路径。
fp = open(filename, 'wb')
# 执行结果生成测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自 动 化 测 试 报 告', description='微投帮weixin_H5', tester='点点')
# runner = unittest.TextTestRunner()
if __name__ == "__main__":
    runner.run(alltestnames)
