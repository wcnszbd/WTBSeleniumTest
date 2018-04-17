#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-15 15:30
import unittest
from keywords.keyword_01 import *
from keywords.public_keyword import *

# 用例
class Case_002(unittest.TestCase):
    u'''测试套件-002'''
    @classmethod
    def setUpClass(cls):
        u'''开始'''
        cls.driver = Browser.open(cls)
        cls.KeyWord01 = KeyWord01(cls.driver)
        cls.PublicKeyWord = PublicKeyWord(cls.driver)
        cls.PublicKeyWord.login()

    def test_001(self):
        u'''首页-首页菜单检查'''
        self.KeyWord01.inspecthome()

    def test_002(self):
        u'''首页-我的菜单按钮跳转检查'''
        self.KeyWord01.clickbuttoncd()

    def test_003(self):
        u'''首页-我的菜单按钮跳转检查'''
        self.KeyWord01.inspectsearch('足协背书 动量科技欲融资3000万')

    def test_004(self):
        u'''首页-标签选择功能'''
        self.KeyWord01.inspectlabel()




    @classmethod
    def tearDownClass(cls):
        u'''关闭浏览器'''
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
