#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-15 13:22


from time import sleep
from configs import LOGIN_URL, USER
from tools import uitool
from pages.page01 import *

# 关键字
class KeyWord01():

    def __init__(self, driver):
        self.driver = driver

    def inspecthome(self):
        """检查首页菜单按钮"""
        driver = self.driver
        tool = uitool(driver)
        tool.Get(LOGIN_URL + sy['url'])
        shouye = tool.Text(sy['首页菜单按钮'])
        tool.AsEqual(shouye, '首页')

    def clickbuttoncd(self):
        """点击我的菜单按钮"""
        driver = self.driver
        tool = uitool(driver)
        tool.Get(LOGIN_URL + sy['url'])
        tool.Click(sy['我的菜单按钮'])
        sleep(1)
        title = tool.Title()
        tool.AsEqual(title, '个人名片')
        sleep(1)

    def inspectsearch(self, msg):
        """检查搜索按钮"""
        driver = self.driver
        tool = uitool(driver)
        tool.Get(LOGIN_URL + sy['url'])
        tool.Click(sy['首页搜索框'])
        tool.Click(sy['顶部搜索框'])
        tool.Input(sy['顶部搜索框'], msg)
        tool.Click(sy['顶部搜索按钮'])
        jieguo = tool.Text(sy['搜索结果第一列标题'])
        tool.AsEqual(jieguo, msg)

    def inspectlabel(self):
        """检查标签筛选"""
        driver = self.driver
        tool = uitool(driver)
        tool.Get(LOGIN_URL + sy['url'])
        tool.Click(sy['行业标签'])
        tool.Click(sy['人工智能'])
        tool.Click(sy['大数据'])
        tool.Click(sy['所在城市'])
        tool.Click(sy['北京'])
        tool.Click(sy['上海'])
        tool.Click(sy['融资轮次'])
        tool.Click(sy['天使轮'])
        tool.Click(sy['Pre-A轮'])
        tool.Click(sy['标签确定按钮'])
        sleep(1)