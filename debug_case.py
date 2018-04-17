#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-10 16:34
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.cnblogs.com/')
try:
    el = driver.find_element_by_xpath("//a[text()='关于博客园1")
except:
    driver.get_screenshot_as_file("error_picture\\"+"xxxx"+".png")







