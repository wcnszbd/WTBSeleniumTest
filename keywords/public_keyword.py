#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-15 13:22

from time import sleep
from configs import LOGIN_URL, USER, mobile_emulation
from tools import uitool
from pages.page01 import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 关键字
class Browser():
    """打开浏览器"""
    def open(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.maximize_window()
        return self.driver

class PublicKeyWord():

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        driver = self.driver
        tool = uitool(driver)
        tool.Get(LOGIN_URL + login['url'])
        sleep(1)
        tool.Click(login['密码登陆选择按钮'])
        tool.Inputs(login['用户名输入框'], USER['user']['账号'])
        tool.Inputs(login['密码输入框'], USER['user']['密码'])
        tool.Click(login['登陆按钮'])
        sleep(1)
        shouye = tool.Text(sy['首页菜单按钮'])
        tool.AsEqual(shouye, '首页')
