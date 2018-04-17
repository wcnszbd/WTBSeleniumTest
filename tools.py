#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-15 13:20

from selenium.webdriver.common.action_chains import *
import random
from time import sleep

#封装selenium及相关工具
class uitool():

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # 打开浏览地址
    def Get(self, url):
        self.driver.get(url)

    # 定位单个元素
    def El(self, el):
        try:
            el = self.driver.find_element(*el)
        except:
            now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
            self.driver.get_screenshot_as_file('\\WTBSeleniumTest\\error_picture\\'+now+'.png')
        return el
    # 定位多个元素
    def Els(self, els):
        try:
            els = self.driver.find_elements(*els)
        except:
            now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
            self.driver.get_screenshot_as_file('\\WTBSeleniumTest\\error_picture\\'+now+'.png')
        return els

    # 运行js
    def Exejs(self, js):
        self.driver.execute_script(js)

    # 输入
    def Input(self, el, msg):
        el = self.El(el)
        el.clear()
        el.send_keys(msg)

    # 批量输入
    def Inputs(self, els, msg):
        els = self.Els(els)
        for el in els:
            el.clear()
            el.send_keys(msg)

    #  清除文本框内容
    def Clear(self, el):
        el = self.El(el)
        el.clear()
    # 点击
    def Click(self, el):
        el = self.El(el)
        el.click()

    # 获取单个标签内容
    def Text(self, el):
        el = self.El(el)
        text = el.text
        return text

    # 获取多个标签内容
    def Texts(self, els):
        els = self.Els(els)
        texts = []
        for el in els:
            texts.append(el.text)
        return texts

    # 鼠标悬停
    def Movreper(self, el):
        el = self.El(el)
        ActionChains(self.driver).move_to_element(el).perform()

    # 滚动到底部
    def Roolldown(self):
        self.driver.execute_script("window.scrollTo(0,document.body.clientHeight)")

    # 滚动窗口滑块
    def Rooll(self, a, b):
        self.driver.execute_script("window.scrollTo("+str(a)+","+str(b)+")")

    # 接受警告信息
    def Accept(self):
        self.driver.switch_to.alert.accept()
        sleep(3)

    # 取消警告信息
    def Dismiss(self):
        sleep(3)
        self.driver.switch_to.alert.dismiss()
        sleep(3)
    # 断言
    def AsEqual(self, shiji, yuche):
        assert shiji == yuche, '▇▇▇断言错误!'+'【实际值：'+shiji+"】►►►"+'【预测值：'+yuche+'】'

    # 获取随机数字
    def Randomint(self, start, stoup):
        rint = random.randint(start, stoup)
        return rint

    # 获取当前窗口句柄
    def Wdnow(self):
        nowhandle = self.driver.current_window_handle
        return nowhandle

    # 获取当前窗口句柄
    def Wdall(self):
       allhandles = self.driver.window_handles
       return allhandles

    # 进入窗口
    def Stchwd(self, handle):
        self.driver.switch_to.window(handle)

    # 关闭当前窗口
    def Clowd(self):
        self.driver.close()

    # 关闭当前窗口
    def Title(self):
        title = self.driver.title
        return title
